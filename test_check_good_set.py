from check_good_set import is_good_collection
from test_utils import print_test
from projective_utils import get_p1

# we know that a_1, ..., a_{q+1} is a good set for m = 1
def test_simplest_good_set(q):
  pts = [(pt,) for pt in get_p1(q)]
  
  print_test(f"test_simplest_good_set({q})", is_good_collection(pts=pts, m=1, q=q))

def test_simplest_bad_set(q):
  # set of size q + 1 with exactly one duplicate
  pts = [((0, 1),)] * 2 + [((1, d),) for d in range(1, q)]

  print_test(f"test_simplest_bad_set({q})", not is_good_collection(pts=pts, m=1, q=q))

def test_quadratic_good_set(q):
  fixed_pt = (0, 1)
  pts = [(p, fixed_pt) for p in get_p1(q)]

  print_test(f"test_quadratic_good_set({q})", is_good_collection(pts=pts, m=2, q=q))

def test_size_q_fails(q):
  not_all_pts = [(1, d) for d in range(1, q + 1)]
  fixed_pt = (0, 1)
  pts = [(p, fixed_pt) for p in not_all_pts]

  print_test(f"test_size_q_fails({q})", not is_good_collection(pts=pts, m=2, q=q))

if __name__ == "__main__":
  for q in {2, 3, 5}:
    test_size_q_fails(q)
    test_quadratic_good_set(q)
    test_simplest_bad_set(q)
    test_simplest_good_set(q)
