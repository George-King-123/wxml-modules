from HyperSurfaceSet import HyperSurfaceSet, CachedHyperSurfaceSet
from projective_utils import get_pd_of_fq
import string

class SequenceBuilder:
  # q = size of the base field
  # n = the nilpotentcy degree for all elements, also the number of tuples per window
  def __init__(self, q, n, max_build_length, d=1, max_m = None):
    self.q = q
    self.n = n
    self.max_build_length = max_build_length
    self.d = d
    self.pd = get_pd_of_fq(d=d, q=q)
    self.max_m = max_m

    # successful_sequences[i] = a set of sequences of length i that meet the constraints 
    self.successful_sequences = [set() for _ in range(max_build_length + 1)]

    # map from m to the set of all hypersurfaces of degree m
    self.surface_sets = {}

  def satisfies_contraints(self, seq):
    # degree we are considering,aka size of the tuple 
    m = 1
    while m * self.n <= len(seq) and (self.max_m is None or m <= self.max_m):
      # check that the window ending here works for degree m

      # creates all tuples except for the last one, python quirk
      length_m_tuples = {tuple(seq[-m*(j+1) : -m*j]) for j in range (1, self.n)}

      # add the last one 
      length_m_tuples.add(tuple(seq[-m:]))

      if m not in self.surface_sets:
        self.surface_sets[m] = CachedHyperSurfaceSet(m=m, q=self.q)

      if not self.surface_sets[m].is_good_collection(length_m_tuples):
        return False

      m += 1

    return True

  def build_sequences(self):
    self.build_sequence_recur([])

  def build_sequence_recur(self, cur_sequence):
    if not self.satisfies_contraints(cur_sequence):
      return
    
    self.successful_sequences[len(cur_sequence)].add(tuple(cur_sequence))

    if len(cur_sequence) == self.max_build_length:
      return

    for next_elt in self.pd:
      cur_sequence.append(next_elt)
      self.build_sequence_recur(cur_sequence)
      cur_sequence.pop()

  def print_seq(self, seq):
    letter_map = {pt:letter for pt, letter in zip(self.pd, string.ascii_uppercase)}

    letter_seq = "".join(letter_map[pt] for pt in seq) + "\\"

    print(letter_seq)
  
# returns a map {len: num} which maps a sequence length 
# to the number of successful sequences. Deletes all mappings of 0 after 
# the first one. If there are no lengths which map to 0 in the range [0, max_build_length]
# then it will return a map with size max_build_length, where all values are positive
def get_length_histogram(q, n, max_build_length=40, d=1):
  sb = SequenceBuilder(q=q, n=n, max_build_length=max_build_length, d=d)
  sb.build_sequences()
  length_to_num = {}
  for length in range(len(sb.successful_sequences)):
    num_successful = len(sb.successful_sequences[length])
    length_to_num[length] = num_successful
    if num_successful == 0: 
      break
  return length_to_num

def print_seq_length_histogram(hist):
  sorted_hist = sorted([(length, hist[length]) for length in hist], key = lambda x: x[0])
  for len, num_good in sorted_hist:
    print(f"# of good length {len} sequences: {num_good}")

if __name__ == "__main__":
  pass
