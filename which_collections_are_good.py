from HyperSurfaceSet import HyperSurfaceSet
from projective_utils import get_p1, generate_all_length_m_tuples
from math import comb
import itertools
import string

def investigate_collections(q, m, size):
  all_collections = generate_collections(q, m, size)
  checker = HyperSurfaceSet(q=q, m=m)
    
  # clumsy, but comprehensions would use more memory here
  num_good = 0
  for c in all_collections:    
    if checker.is_good_collection(c):
      num_good += 1
    
  return num_good

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

if __name__ == "__main__":

  def make_latex_table(q, m_min, m_max, size_min, size_max):
    header = " & ".join(["c \\backslash m"] + [str(m) for m in range(m_min, m_max + 1)]) + "\\\\"
    lines = []

    for c in range(size_min, size_max + 1):
      lines.append(" & ".join([str(c)] + [str(investigate_collections(q, m, c)) for m in range(m_min, m_max + 1)]))
    
    body = "\\\\ \n".join(lines)
    
    fst_line = "$$\n\\begin{array}" + '{' + "|".join(['c'] * (m_max - m_min + 2)) + '}'
    
    print(fst_line)
    print(header)
    print("\\hline")
    print(body)
    print('\\end{array}\n$$')


  make_latex_table(q=2, m_min=1, m_max=3, size_min=6, size_max=6)

