import string 

def get_p1(q):
  return [(0, 1)] + [(1, d) for d in range(0, q)]

# return a list of tuples (a_1, ... a_m) st
# a_i \in \{i, i + 1, ..., j - 1, j\}
# of course requires i <= j, m >= 0
def generate_tuples(i, j, m):
  all_tuples = set()

  def generate_recur(cur):
    if len(cur) == m:
      all_tuples.add(tuple(cur))
      return 

    for a_i in range(i, j + 1):
      cur.append(a_i)
      generate_recur(cur)
      cur.pop()
  
  generate_recur([])

  return all_tuples 

# generate all unique tuples of length m with entries in p1, 
# taking F_q to be the base field
def generate_all_length_m_tuples(q, m):
  all_tuples = []
  p1 = get_p1(q)

  def generate_recur(cur):
    if len(cur) == m:
      all_tuples.append(tuple(cur))
      return 

    for p in p1:
      cur.append(p)
      generate_recur(cur)
      cur.pop()
  
  generate_recur([])

  assert len(all_tuples) == (q + 1) ** m
  return all_tuples 

#  returns a readable view of the collection, associating each element of P1 with a letter
# and printing the M-tuples as words in this alphabet
def collection_to_string(c, q):
  letter_map = {pt: letter for pt, letter in zip(get_p1(q), string.ascii_uppercase)}

  def translate_tuple(tuple):
    return "".join(letter_map[t] for t in tuple)

  return '{' + ", ".join((translate_tuple(m_tuple) for m_tuple in c)) + '}'