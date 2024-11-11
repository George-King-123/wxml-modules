from projective_utils import generate_tuples, get_all_hypersurfaces
from functools import lru_cache

# represents the set of all hypersurfaces of degree m in P1(q)
class HyperSurfaceSet:

  def __init__(self, m, q, num_generators=2):
    self.m = m
    self.q = q
    self.num_generators = num_generators

    self.monomial_indices = generate_tuples(0, num_generators - 1, m) 
    self.hyper_surfaces = get_all_hypersurfaces(q=q, m=m, d=num_generators-1)

    # pt_cache[i] is a list of length num_generators**m, 
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
  
class CachedHyperSurfaceSet(HyperSurfaceSet):
  def is_good_collection(self, pts):
    # sets aren't hashable, so we tuple them
    return self.is_good_collection_cached(tuple(pts))

  @lru_cache(maxsize=None)
  def is_good_collection_cached(self, pts):
    return super().is_good_collection(pts)