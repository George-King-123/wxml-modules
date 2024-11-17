import string 
from functools import lru_cache

def get_p1(q):
  p1 = get_pd_of_fq(d=1, q=q)
  assert len(p1) == q + 1
  return p1

# returns all hypersurfaces of degree m in P^d(F_q)
def get_all_hypersurfaces(m, q, d=1):
  all_hypersurfaces = get_pd_of_fq(d=int((d+1)**m - 1), q=q)

  assert len(all_hypersurfaces) == int((q**((d+1)**m) - 1)/(q-1))

  return all_hypersurfaces 

# returns the projective space of dimension d associated with F_q, 
# i.e. the lines in F_q^{d+1}. This is represented by returning d + 1
# tuples that are exactly the representatives of the appropriate equivalence classes
def get_pd_of_fq(d, q):
  all_reps = generate_tuples(0, q-1, d + 1)

  rep_already_in = set()
  p_d_q = set()

  for r in all_reps:
    if r not in rep_already_in:
      # no representative of r is in our set yet 
      p_d_q.add(r)
      for i in range(q):
        rep_already_in.add(mul_tuple(i, r, q))
  
  assert len(p_d_q) == int((q**(d + 1) - 1)/(q-1))

  return p_d_q 

def mul_tuple(scalar, t, q):
  return tuple([(scalar * ti) % q for ti in t])

# return a list of tuples (a_1, ... a_m) st
# a_i \in \{i, i + 1, ..., j - 1, j\}
# of course requires i <= j, m >= 0
def generate_tuples(i, j, m):
  all_tuples = set()

  def generate_recur(cur):
    if len(cur) == m:
      all_tuples.add(tuple(cur))
      return 

    for a_i in range(i, j + 1):
      cur.append(a_i) 
      generate_recur(cur)
      cur.pop()
  
  generate_recur([])

  return all_tuples 

# generate all unique tuples of length m with entries in P^d, 
# taking F_q to be the base field
def generate_all_length_m_tuples(q, m, d=1):
  all_tuples = []
  pd_Fq = get_pd_of_fq(d=d, q=q)

  def generate_recur(cur):
    if len(cur) == m:
      all_tuples.append(tuple(cur))
      return 

    for p in pd_Fq:
      cur.append(p)
      generate_recur(cur)
      cur.pop()
  
  generate_recur([])

  assert len(all_tuples) == len(pd_Fq) ** m
  return all_tuples 

#  returns a readable view of the collection, associating each element of P1 with a letter
# and printing the M-tuples as words in this alphabet
def collection_to_string(c, q, d=1):
  letter_map = {pt: letter for pt, letter in zip(get_pd_of_fq(q=q, d=d), string.ascii_uppercase)}

  def translate_tuple(tuple):
    return "".join(letter_map[t] for t in tuple)

  return '{' + ", ".join((translate_tuple(m_tuple) for m_tuple in c)) + '}'


# returns true iff a set of mtuples is simple.
# Recall we say a set is simple if it contains a subset C st 
# there is an index i st all elements of C agree on indices other than i,
# and the points at index i run over all of P^d.
# fact: all simple sets are good
def is_set_simple(mtuples, d, q):
  m = len(next(iter(mtuples))) 

  # If the input is {"aaa", "aba", "def"}
  # one_star_to_completion_map will be
  # {('*', 'a', 'a'): {'aaa'}, 
  # ('a', '*', 'a'): {'aaa', 'aca'}, 
  # ('a', 'a', '*'): {'aaa'}, 
  # ('*', 'e', 'f'): {'def'}, 
  # ('d', '*', 'f'): {'def'}, 
  # ('d', 'e', '*'): {'def'}, 
  # ('*', 'c', 'a'): {'aca'}, 
  # ('a', 'c', '*'): {'aca'}}

  one_star_to_completion_map = {}
  pd_fq_size = len(get_pd_of_fq(d, q)) 

  for t in mtuples:
    for i in range(m):
      differ_at_i = t[0:i] + ("*",) + t[i+1:]
      if differ_at_i not in one_star_to_completion_map:
        one_star_to_completion_map[differ_at_i] = set() 
      one_star_to_completion_map[differ_at_i].add(t)

      if len(one_star_to_completion_map[differ_at_i]) == pd_fq_size:
        return True 

  return False

# when running sequence builder, this gives a MASSIVE improvement,
# and is better than any naive caching implemented by hand
# have to call it passing in mtuple as a big tuple of all the tuples,
# since sets aren't hashable
@lru_cache(maxsize=None)
def is_set_simple_cached(mtuples, d, q):
  return is_set_simple(mtuples, d, q)

# WARNING: THIS FUNCTION IS DEPRECATED, is_set_simple is strictly better
# just checks if the set has m-tuples which all agree except for on one coordinate, 
# and that that coordinate runs over all elements of P_d(F_q)
def is_good_set_all_coords_fixed(mtuples, d, q):
  m = len(next(iter(mtuples))) 

  if m == 1: 
    # just needs to contain all elements of P1
    return {t[0] for t in mtuples} == set(get_pd_of_fq(d, q))


  # to find the index of interest, need to take any two distinct elements 
  # and find the index at which they differ
  dif_elts = set(mtuples) 
  elt1 = dif_elts.pop()
  elt2 = dif_elts.pop()

  dif_indices = [i for i in range(m) if elt1[i] != elt2[i]]
  if len(dif_indices) != 1:
    return False

  dif_idx = dif_indices[0]

  # add the arbitrary elements back in before going over all m-tuples 
  # to ensure all points in p1 appear at dif_idx
  dif_elts.add(elt1)
  dif_elts.add(elt2) 

  pts_at_dif_idx = set()

  for elt in dif_elts: 
    if len([i for i in range(m) if elt1[i] != elt[i]]) > 1:
      return False
    pts_at_dif_idx.add(elt[dif_idx])
    
  return pts_at_dif_idx == set(get_pd_of_fq(d, q))

def sequence_to_string(d, q, seq):
  pd_fq = get_pd_of_fq(d, q)
  letter_map = {pt: letter for pt, letter in zip(pd_fq, string.ascii_uppercase)}
  
  translated_seq = "".join([letter_map[pt] for pt in seq])
  return translated_seq

def number_to_seq(d, q, letters):
  pd_fq = get_pd_of_fq(d, q)
  letter_to_pt = {letter: pt for letter, pt in zip([0, 1, 2], pd_fq)}
  return [letter_to_pt[letter] for letter in letters] 

