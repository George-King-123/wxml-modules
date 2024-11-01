import unittest

from projective_utils import generate_tuples

class TestGenerateTuples(unittest.TestCase):
    
  def test_generate(self):
    tuples = generate_tuples(1, 3, 2)
    correct_ans = {(1, 1), (1, 2), (1, 3), 
                  (2, 1), (2, 2), (2, 3),
                  (3, 1), (3, 2), (3, 3)}
    self.assertEqual(tuples, correct_ans)

  def test_generate_2(self):
    tuples = generate_tuples(1, 2, 2)
    correct_ans = {(1, 1), (1, 2), (2, 1), (2, 2)}
    self.assertEqual(tuples, correct_ans)
    

  def test_generate_edge_cases(self):
    tuples1 = generate_tuples(1, 1, 5)
    correct_ans1 = {(1, 1, 1, 1, 1)}
    self.assertEqual(tuples1, correct_ans1)

    tuples2 = generate_tuples(1, 1, 1)
    correct_ans2 = {(1,)}
    self.assertEqual(tuples2, correct_ans2)

if __name__ == "__main__":
  unittest.main()