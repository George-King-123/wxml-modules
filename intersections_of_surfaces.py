from HyperSurfaceSet import HyperSurfaceSet
from projective_utils import generate_all_length_m_tuples
import itertools 

def find_intersection_sizes(m, q, intersection_size):
  h = HyperSurfaceSet(m=m, q=q)
  all_tuples = generate_all_length_m_tuples(m=m, q=q)

  intersection_size = 2
  surface_groups = itertools.combinations(h.hyper_surfaces, intersection_size)

  freq_count = {}
  for g in surface_groups:
    num_pts_in_intersection = len([p for p in all_tuples if 
                                  all(h.point_on_surface(p, s) for s in g)])
    freq_count[num_pts_in_intersection] = freq_count.get(num_pts_in_intersection, 0) + 1

  print(sorted([(num, freq_count[num]) for num in freq_count], key = lambda x:x[0]))

if __name__ == "__main__":
  find_intersection_sizes(m=2, q=5, intersection_size=3)
