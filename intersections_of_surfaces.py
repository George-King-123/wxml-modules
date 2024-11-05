from HyperSurfaceSet import HyperSurfaceSet
from which_collections_are_good import generate_all_length_m_tuples
import itertools 

def f(m, q):
  h = HyperSurfaceSet(m=m, q=q)
  all_tuples = generate_all_length_m_tuples(m=m, q=q)

  intersection_size = 2
  surface_groups = itertools.combinations(h.hyper_surfaces, intersection_size)

  freq_count = {}
  for g in surface_groups:
    num_pts_in_intersection = len([p for p in all_tuples if 
                                  all(h.point_on_surface(p, s) for s in g)])
    freq_count[num_pts_in_intersection] = freq_count.get(num_pts_in_intersection, 0) + 1

  print(freq_count)

if __name__ == "__main__":
  f(2, 2)
