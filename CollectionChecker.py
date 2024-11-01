# throughout q is the size of the field


class CollectionChecker:

  def __init__(self, m, q):
    self.m = m
    self.q = q

    self.monomial_indices = CollectionChecker.generate_tuples(0, 1, m) 
    self.hyper_surfaces = CollectionChecker.get_all_hypersurfaces(q=q, m=m) 

  # each point in pts is a point in (P^1)^m
  def is_good_collection(self, pts):
    return all(any((self.point_on_surface(pt=pt, surface=s) for pt in pts))
                for s in self.hyper_surfaces)

  # is the given point in (P^1)^m on the hypersurface of degree m
  # pt is a matrix where pt[i] = (\beta^i_1, \beta^i_2)
  def point_on_surface(self, pt, surface):
    tot_sum = 0
    for idx, t in enumerate(self.monomial_indices):
      # t = (i_1, ... i_m)
      prod = 1
      for j in range(self.m):
        prod *= pt[j][t[j]]
        prod %= self.q 
      tot_sum += prod * surface[idx]
      tot_sum %= self.q 
    return tot_sum == 0

  # we will actually generate all tuples of length 2^m 
  # with entries in F_q
  @staticmethod
  def get_all_hypersurfaces(m, q):
    return CollectionChecker.generate_tuples(0, q-1, 2 ** m)

  # return a list of tuples (a_1, ... a_m) st
  # a_i \in \{i, i + 1, ..., j - 1, j\}
  # of course requires i <= j, m >= 0
  @staticmethod
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
