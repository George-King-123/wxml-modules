from HyperSurfaceSet import HyperSurfaceSet
from projective_utils import get_p1
from math import comb
import itertools

def investigate_collections(q, m, size):
  all_collections = generate_collections(q, m, size)
  checker = HyperSurfaceSet(q=q, m=m)

  # clumsy, but comprehensions would use more memory here
  num_good = 0
  for c in all_collections:    
    if checker.is_good_collection(c):
      num_good += 1
    
  print(f"good = {num_good}, bad = {len(all_collections) - num_good}")

  # mostly for testing
  return num_good

def print_collection(c):
  def format_tuple(tuple):
    return '[' + ", ".join(str(t) for t in tuple) + ']'

  print('{' + "; ".join((format_tuple(m_tuple) for m_tuple in c)) + '}')

# generate the set of all collections C
# where |C| = q + 1, each element of C is a tuple of length m, 
# and each element of that tuple is a point in p1
def generate_collections(q, m, size):
  all_tuples = generate_all_length_m_tuples(q, m)
  all_collections = list(itertools.combinations(all_tuples, size))

  assert len(all_collections) == comb((q + 1) ** m, size)
  return all_collections


# generate all unique tuples of length m with entries in p1, 
# taking F_q to be the base field
def generate_all_length_m_tuples(q, m):
  all_tuples = []
  p1 = get_p1(q)

  def generate_recur(cur):
    if len(cur) == m:
      all_tuples.append(tuple(cur))
      return 

    for p in p1:
      cur.append(p)
      generate_recur(cur)
      cur.pop()
  
  generate_recur([])

  assert len(all_tuples) == (q + 1) ** m
  return all_tuples 

if __name__ == "__main__":
  for q in {2, 3, 5}:
    for m in {1, 2, 3}:
      print(f"q = {q}, m = {m}")
      investigate_collections(q=q, m=m, size=q+1)
      print()

  # for q in {2, 3, 5}:
  #   for m in {2, 3}:
  #     for size in {q + 2, q + 3}:
  #       print(f"q = {q}, m = {m}, size = {size}  ")
  #       investigate_collections(q=q, m=m, size=size)
  #       print()