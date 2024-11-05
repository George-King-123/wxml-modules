from HyperSurfaceSet import HyperSurfaceSet, CachedHyperSurfaceSet
from which_collections_are_good import generate_collections
from projective_utils import get_p1

# returns a set of all tuples of length d having elements in
# {0, 1, ..., d-1} representing bijections
def make_s_d(d:int):
  def select(cur, all_elts:set, available_nums:set):
    if len(available_nums) == 0:
      all_elts.add(tuple(cur))
      return
    
    for i in available_nums:
      cur.append(i)
      select(cur, all_elts, available_nums.difference({i}))
      cur.remove(i)
  
  res = set()
  select([], res, {i for i in range (0, d)})
  return res 


def apply_perm(perm, m_tuple, q):
  p1_to_int = {p:a for p, a in zip(get_p1(q), range(q+1))}
  int_to_p1 = {a:p for a, p in zip(range(q+1), get_p1(q))}

  return tuple([
    int_to_p1[perm[p1_to_int[t_i]]] for t_i in m_tuple
  ])

def permute_collection(perm, collection, q):
  return [apply_perm(perm, elt, q) for elt in collection]

def check(m , q, size):
  # first, find all the good sets
  all_collections = generate_collections(q, m, size)
  checker = CachedHyperSurfaceSet(q=q, m=m)

  good_collections = [c for c in all_collections if checker.is_good_collection(c)]

  s_q_plus_1 = make_s_d(q+1)
  
  return all(checker.is_good_collection(permute_collection(perm, c, q)) 
                 for perm in s_q_plus_1 for c in good_collections)

if __name__ == "__main__":
  print(check(q = 2, m = 3, size = 5))
