# WARNING: THIS JUST CHECKS THAT WE PRODUCE THE SAME DATA EACH TIME,
# THERE AREN'T MATHEMATICAL JUSTIFICATIONS FOR THESE VALUES. 

import unittest
from which_collections_are_good import investigate_collections
from test_check_good_set import PRIMES

class TestInvestigateCollections(unittest.TestCase):

    def test_m_1(self):
        for q in PRIMES:
            with self.subTest("m=1 should have one good collection of size q+1",q=q):
                self.assertEquals(investigate_collections(q=q, m=1, size=q+1), 1)
    
    # tests when size = q + 1
    def test_q_2_m_2(self):
        self.assertEquals(investigate_collections(q=2, m=2, size=3), 6)
    
    def test_q_3_m_2(self):
        self.assertEquals(investigate_collections(q=3, m=2, size=4), 8)

    # tests when size \neq q + 1
    def test_q_3_m_2(self):
        self.assertEquals(investigate_collections(q=3, m=2, size=5), 96)
        self.assertEquals(investigate_collections(q=3, m=2, size=6), 528)




if __name__ == "__main__":
    unittest.main()