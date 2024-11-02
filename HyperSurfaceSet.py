from projective_utils import generate_tuples

# represents the set of all hypersurfaces of degree m in P1(q)
class HyperSurfaceSet:

  def __init__(self, m, q):
    self.m = m
    self.q = q

    self.monomial_indices = generate_tuples(0, 1, m) 
    self.hyper_surfaces = HyperSurfaceSet.get_all_hypersurfaces(q=q, m=m)

    # pt_cache[i] is a list of length 2**m, 
    # where pt_cache[i][j] is the value of the jth monomial when you plug in point i
    self.pt_cache = {}


  # each point in pts is a point in (P^1)^m
  def is_good_collection(self, pts):
    return all(any((self.point_on_surface(pt=pt, surface=s) for pt in pts))
                for s in self.hyper_surfaces)

  # is the given point in (P^1)^m on the hypersurface of degree m
  # pt is a matrix where pt[i] = (\beta^i_1, \beta^i_2)
  def point_on_surface(self, pt, surface):
    if pt not in self.pt_cache:
      self.cache_pt(pt)

    
    length = 2 ** self.m
    assert len(self.pt_cache[pt]) == length 
    assert len(surface) == length 

    tot_sum = 0
    for j in range(length):
      tot_sum += (surface[j] * self.pt_cache[pt][j]) % self.q
      tot_sum %= self.q 

    return tot_sum == 0

  def cache_pt(self, pt):
    assert pt not in self.pt_cache

    self.pt_cache[pt] = []
    for t in self.monomial_indices:
      # t = (i_1, ... i_m)
      prod = 1
      for j in range(self.m):
        prod *= pt[j][t[j]]
        prod %= self.q 
      self.pt_cache[pt].append(prod)


  # we will actually generate all tuples of length 2^m 
  # with entries in F_q
  @staticmethod
  def get_all_hypersurfaces(m, q):
    all_reps = generate_tuples(0, q-1, 2 ** m)

    rep_already_in = set()
    all_hypersurfaces = set()

    for r in all_reps:
      if r not in rep_already_in:
        # no representative of r is in our set yet 
        all_hypersurfaces.add(r)
        for i in range(q):
          rep_already_in.add(HyperSurfaceSet.mul_tuple(i, r, q))
    
    assert len(all_hypersurfaces) == int((q**(2**m) - 1)/(q-1))

    return all_hypersurfaces 
  
  @staticmethod 
  def mul_tuple(scalar, t, q):
    return tuple([(scalar * ti) % q for ti in t])


HyperSurfaceSet.get_all_hypersurfaces(2, 2)