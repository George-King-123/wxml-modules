from check_good_set import is_good_collection
from projective_utils import get_p1
from math import comb

def are_all_collections_of_size_q_plus_1_good(q, m):
  all_collections = generate_collections(q, m)

  num_good = 0
  num_bad = 0
  for c in all_collections:
    
    if is_good_collection(pts=c, m=m, q=q):
      num_good += 1
    else:
      num_bad += 1
  
  print(f"good = {num_good}, bad = {num_bad}")
  # return all(is_good_collection(pts=c, m=m, q=q) for c in all_collections)

# generate the set of all collections C
# where |C| = q + 1, each element of C is a tuple of length m, 
# and each element of that tuple is a point in p1
def generate_collections(q, m):
  all_tuples = generate_all_length_m_tuples(q, m)
  all_collections = []

  def generate_collections_recur(i, cur_collection):
    if len(cur_collection) == q + 1:
      all_collections.append(tuple(cur_collection))
      return 
    
    if i == len(all_tuples):
      return
    
    # find all collections not containing all_tuples[i]
    generate_collections_recur(i + 1, cur_collection)

    # find all collections containing all_tuples[i]
    cur_collection.add(all_tuples[i])
    generate_collections_recur(i + 1, cur_collection)
    cur_collection.remove(all_tuples[i])

  generate_collections_recur(0, set())

  assert len(all_collections) == comb((q + 1) ** m, q + 1)

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
  for q in range(2, 4):
    for m in range(1, 4):
      print(f"q = {q}, m = {m}")
      are_all_collections_of_size_q_plus_1_good(q=q, m=m)
      print()

