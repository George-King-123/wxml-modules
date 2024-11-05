from HyperSurfaceSet import HyperSurfaceSet
from projective_utils import get_p1
from math import comb
import itertools
import string

def investigate_collections(q, m, size):
  all_collections = generate_collections(q, m, size)
  checker = HyperSurfaceSet(q=q, m=m)

  def contains_good_sub_collection_of_size(collection, subsize):
    return any(checker.is_good_collection(c) for c 
               in itertools.combinations(collection, subsize))
    
  # clumsy, but comprehensions would use more memory here
  num_good = 0
  for c in all_collections:    
    if checker.is_good_collection(c):
      # if not contains_good_sub_collection_of_size(c, q + 1):
      #   print(f"The following good collection of size {size} does not contain a good subcollection of size q + 1 = {q + 1}")
      #   print_collection(c, q)
      #   print()
      # print_collection(c, q)
      num_good += 1
    
  print(f"good = ${num_good}$, bad = ${len(all_collections) - num_good}$")

  # mostly for testing
  return num_good

# prints the collection, associating each element of P1 with a letter
# and printing the M-tuples as words in this alphabet
def print_collection(c, q):
  letter_map = {pt: letter for pt, letter in zip(get_p1(q), string.ascii_uppercase)}

  def translate_tuple(tuple):
    return "".join(letter_map[t] for t in tuple)

  print('{' + ", ".join((translate_tuple(m_tuple) for m_tuple in c)) + '}\\')

# generate the set of all collections C
# where |C| = size, each element of C is a tuple of length m, 
# and each element of that tuple is a point in p1
def generate_collections(q, m, size):
  all_tuples = generate_all_length_m_tuples(q, m)
  all_collections = list(itertools.combinations(all_tuples, size))

  assert len(all_collections) == comb((q + 1) ** m, size)
  return all_collections

def letters_to_collection(word_set, q, m):
  letter_map = {letter:pt for pt, letter in zip(get_p1(q), string.ascii_uppercase)}
  return {tuple([letter_map[letter] for letter in word]) for word in word_set}

def is_collection_good(word_set, q, m):
  checker = HyperSurfaceSet(m=m, q=q)
  return checker.is_good_collection(letters_to_collection(word_set=word_set, q=q, m=m))

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
  will_collection = {'AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC', 'CD'}
  print(is_collection_good(will_collection, q=3, m=2))