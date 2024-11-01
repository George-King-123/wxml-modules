from CollectionChecker import CollectionChecker
from test_utils import print_test

def generate_test():
  tuples = CollectionChecker.generate_tuples(1, 3, 2)
  correct_ans = {(1, 1), (1, 2), (1, 3), 
                 (2, 1), (2, 2), (2, 3),
                 (3, 1), (3, 2), (3, 3)}
  print_test("generate_test", tuples == correct_ans)

def generate_test_basic():
  tuples = CollectionChecker.generate_tuples(1, 2, 2)
  correct_ans = {(1, 1), (1, 2), (2, 1), (2, 2)}
  
  print_test("generate_test_basic", tuples == correct_ans)

def generate_test_edge_cases():
  tuples1 = CollectionChecker.generate_tuples(1, 1, 5)
  correct_ans1 = {(1, 1, 1, 1, 1)}

  tuples2 = CollectionChecker.generate_tuples(1, 1, 1)
  correct_ans2 = {(1,)}

  print_test("generate_test_edge_cases", 
             (tuples1 == correct_ans1 and 
             tuples2 == correct_ans2))



if __name__ == "__main__":
  generate_test()
  generate_test_basic()
  generate_test_edge_cases()