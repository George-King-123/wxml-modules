import string 

def get_p1(q):
  p1 = get_pd_of_fq(d=1, q=q)
  assert len(p1) == q + 1
  return p1

# returns all hypersurfaces of degree m in P^d(F_q)
def get_all_hypersurfaces(m, q, d=1):
  all_hypersurfaces = get_pd_of_fq(d=int((d+1)**m - 1), q=q)

  assert len(all_hypersurfaces) == int((q**((d+1)**m) - 1)/(q-1))

  return all_hypersurfaces 

# returns the projective space of dimension d associated with F_q, 
# i.e. the lines in F_q^{d+1}. This is represented by returning d + 1
# tuples that are exactly the representatives of the appropriate equivalence classes
def get_pd_of_fq(d, q):
  all_reps = generate_tuples(0, q-1, d + 1)

  rep_already_in = set()
  p_d_q = set()

  for r in all_reps:
    if r not in rep_already_in:
      # no representative of r is in our set yet 
      p_d_q.add(r)
      for i in range(q):
        rep_already_in.add(mul_tuple(i, r, q))
  
  assert len(p_d_q) == int((q**(d + 1) - 1)/(q-1))

  return p_d_q 

def mul_tuple(scalar, t, q):
  return tuple([(scalar * ti) % q for ti in t])

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