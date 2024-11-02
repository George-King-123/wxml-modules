from projective_utils import generate_tuples

# represents the set of all hypersurfaces of degree m in P1(q)
class HyperSurfaceSet:

  def __init__(self, m, q):
    self.m = m
    self.q = q

    self.monomial_indices = generate_tuples(0, 1, m) 
    self.hyper_surfaces = HyperSurfaceSet.get_all_hypersurfaces(q=q, m=m)

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
    return generate_tuples(0, q-1, 2 ** m)