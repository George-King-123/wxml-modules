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
