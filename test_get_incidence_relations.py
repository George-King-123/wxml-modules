# WARNING: THIS JUST CHECKS THAT WE PRODUCE THE SAME DATA EACH TIME,
# THERE AREN'T MATHEMATICAL JUSTIFICATIONS FOR THESE VALUES. 

import unittest
from get_all_incidence_relations import get_incidence_histogram, get_all_incidence_relations

def get_histogram(q, m):
    return get_incidence_histogram(get_all_incidence_relations(q=q, m=m))

class TestGetIncidenceRelations(unittest.TestCase):
    
    # Will computed this by hand as well
    def test_q_2_m_2(self):
        expected = {3:6, 5: 9}
        self.assertEqual(get_histogram(2, 2), expected)

    def test_q_2_m_3(self):
        expected = {11: 54, 13: 108, 15: 54, 9: 12, 19: 27}
        self.assertEqual(get_histogram(2, 3), expected)
    
    @unittest.skip("takes about 10 seconds")
    def test_q_2_m_4(self):
        expected = {37: 12636, 39: 14472, 43: 7776, 33: 1944, 
                    47: 3888, 41: 9234, 49: 648, 
                    35: 5184, 45: 6732, 31: 648, 53: 1296, 
                    51: 648, 65: 81, 57: 324, 27: 24}

        self.assertEqual(get_histogram(2, 4), expected)

    def test_q_3_m_2(self):
        expected = {7: 16, 4: 24}
        self.assertEqual(get_histogram(3, 2), expected)

    def test_q_3_m_3(self):
        expected = {19: 768, 22: 1728, 16: 432, 28: 288, 37: 64}
        self.assertEqual(get_histogram(3, 3), expected)

if __name__ == "__main__":
    unittest.main()