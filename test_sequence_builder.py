# WARNING: THIS JUST CHECKS THAT WE PRODUCE THE SAME DATA EACH TIME,
# THERE AREN'T MATHEMATICAL JUSTIFICATIONS FOR THESE VALUES. 

import unittest
from Sequence_Builder import get_length_histogram

class TestSequenceBuilder(unittest.TestCase):
    
    def test_q_2_n_3(self):
        expected = {0: 1, 1: 3, 2: 9, 3: 6, 4: 6, 5: 6, 6: 0}
        self.assertEqual(get_length_histogram(2, 3), expected)
    
    def test_q_2_n_4(self):
        expected = {0: 1, 1: 3, 2: 9, 3: 27, 4: 36, 5: 72, 6: 132, 7: 240, 8: 36, 9: 0}
        self.assertEqual(get_length_histogram(2, 4), expected)
    
    def test_q_2_n_5(self):
        expected = {0: 1, 1: 3, 2: 9, 3: 27, 4: 81, 5: 150, 6: 366, 7: 870, 8: 2022, 
                    9: 4686, 10: 3252, 11: 1932, 12: 1920, 13: 2442, 14: 2832, 15: 102, 16: 0}
        self.assertEqual(get_length_histogram(2, 5), expected)

    def test_q_3_n_4(self):
        expected = {0: 1, 1: 4, 2: 16, 3: 64, 4: 24, 5: 24, 6: 24, 7: 24, 8: 0}
        self.assertEqual(get_length_histogram(3, 4), expected)
    
    def test_q_3_n_5(self):
        expected = {0: 1, 1: 4, 2: 16, 3: 64, 4: 256, 5: 240, 6: 528, 7: 1032, 8: 1968, 9: 3768, 10: 0}
        self.assertEqual(get_length_histogram(3, 5), expected)
        
    
    # @unittest.skip("takes about 10 seconds")
    # def test_q_2_n_6(self):
    #     expected = {37: 12636, 39: 14472, 43: 7776, 33: 1944, 
    #                 47: 3888, 41: 9234, 49: 648, 
    #                 35: 5184, 45: 6732, 31: 648, 53: 1296, 
    #                 51: 648, 65: 81, 57: 324, 27: 24}

    #     self.assertEqual(get_length_histogram(2, 4), expected)

    # def test_q_3_n_2(self):
    #     expected = {7: 16, 4: 24}
    #     self.assertEqual(get_length_histogram(3, 2), expected)

    # def test_q_3_n_3(self):
    #     expected = {19: 768, 22: 1728, 16: 432, 28: 288, 37: 64}
    #     self.assertEqual(get_length_histogram(3, 3), expected)

if __name__ == "__main__":
    unittest.main()