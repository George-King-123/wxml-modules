# throughout q is the size of the field

# each point in pts is a point in (P^1)^m
def is_good_collection(pts, m, q):
  surfaces = get_all_hypersurfaces(m, q)
  return all(any((point_on_surface(pt, s, m, q) for pt in pts)) for s in surfaces)

# we will actually generate all tuples of length 2^m 
# with entries in F_q
def get_all_hypersurfaces(m, q):
  return generate_tuples(0, q-1, 2 ** m)

# is the given point in (P^1)^m on the hypersurface of degree m
# pt is a matrix where pt[i] = (\beta^i_1, \beta^i_2)
def point_on_surface(pt, surface, m, q):
  tuples = generate_tuples(0, 1, m) 
  tot_sum = 0
  for idx, t in enumerate(tuples):
    # t = (i_1, ... i_m)
    prod = 1
    for j in range(m):
      prod *= pt[j][t[j]]
      prod %= q 
    tot_sum += prod * surface[idx]
    tot_sum %= q 
  return tot_sum == 0


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
