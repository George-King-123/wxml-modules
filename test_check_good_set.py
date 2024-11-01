import unittest

from HyperSurfaceSet import HyperSurfaceSet
from projective_utils import get_p1

PRIMES = [2, 3, 5, 7]

class TestHyperSurfaceSet(unittest.TestCase):

  # we know that a_1, ..., a_{q+1} is a good set for m = 1
  def test_m_1(self):
    for q in PRIMES:
      with self.subTest("simplest_good_set", q=q):
        pts = [(pt,) for pt in get_p1(q)]
        c = HyperSurfaceSet(m=1, q=q)
        self.assertTrue(c.is_good_collection(pts=pts))

  # we know that any set of q + 1 points with repeats is bad for m = 1
  def test_m_1_one_dup(self):
    for q in PRIMES:
      with self.subTest("simples_bad_set", q=q):
        # set of size q + 1 with exactly one duplicate
        pts = [((0, 1),)] * 2 + [((1, d),) for d in range(1, q)]
        c = HyperSurfaceSet(m=1, q=q)
        self.assertFalse(c.is_good_collection(pts=pts))

  # we know that the set of all pairs (p_i, a) 
  # where the p_i run over all points in P1 and 
  # a is a fixed point in p1 is a good set for m = 2
  def test_quadratic_good_set(self):
    for q in PRIMES:
      with self.subTest("quadratic_good_set", q=q):
        fixed_pt = (0, 1)
        pts = [(p, fixed_pt) for p in get_p1(q)]
        c = HyperSurfaceSet(m=2, q=q)
        self.assertTrue(c.is_good_collection(pts=pts))

  # change the quadratic good set to have one dup
  def test_quadratic_bad_set(self):
    for q in PRIMES:
      with self.subTest("quadratic_bad_set", q=q):
        fixed_pt = (0, 1)
        not_all_pts = [(1, d) for d in range(1, q + 1)]
        pts = [(p, fixed_pt) for p in not_all_pts]

        c = HyperSurfaceSet(m=2, q=q)
        self.assertFalse(c.is_good_collection(pts=pts))

if __name__ == "__main__":
  unittest.main()