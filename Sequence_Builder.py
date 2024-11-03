from HyperSurfaceSet import HyperSurfaceSet
from projective_utils import get_p1
import string

class SequenceBuilder:
  # q = size of the base field
  # n = the nilpotentcy degree for all elements, also the number of tuples per window
  def __init__(self, q, n, max_build_length):
    self.q = q
    self.n = n
    self.max_build_length = max_build_length
    self.p1 = get_p1(q)

    # successful_sequences[i] = a set of sequences of length i that meet the constraints 
    self.successful_sequences = [set() for _ in range(max_build_length + 1)]

    # map from m to the set of all hypersurfaces of degree m
    self.surface_sets = {}

  def satisfies_contraints(self, seq):
    # degree we are considering,aka size of the tuple 
    m = 1
    while m * self.n <= len(seq):
      # check that the window ending here works for degree m

      # creates all tuples except for the last one, python quirk
      length_m_tuples = {tuple(seq[-m*(j+1) : -m*j]) for j in range (1, self.n)}

      # add the last one 
      length_m_tuples.add(tuple(seq[-m:]))

      if m not in self.surface_sets:
        self.surface_sets[m] = HyperSurfaceSet(m=m, q=q)

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

    # try adding everything from 1 up to q+1 (inclusive) to the sequence
    for next_elt in self.p1:
      cur_sequence.append(next_elt)
      self.build_sequence_recur(cur_sequence)
      cur_sequence.pop()

  def print_seq(self, seq):
    letter_map = {pt:letter for pt, letter in zip(self.p1, string.ascii_uppercase)}

    letter_seq = "".join(letter_map[pt] for pt in seq) + "\\"

    print(letter_seq)

if __name__ == "__main__":
  # size of the finite field. Remember the projective space has 
  # size q + 1
  q = 2

  # this is the degree of nilpotency for each element as well
  num_tuples_per_window = q + 4

  max_build_length = 16

  sb = SequenceBuilder(q=q, n=num_tuples_per_window, max_build_length=max_build_length)

  sb.build_sequences()

  def print_all(l):
    num_successful = len(sb.successful_sequences[l])

    print(f"There are {num_successful} successful seqs of length {l}, given below\\")
    for seq in sb.successful_sequences[l]:
      sb.print_seq(seq)
    print()

  for l in range(num_tuples_per_window, len(sb.successful_sequences)):
    num_successful = len(sb.successful_sequences[l])
    print(f"There are {num_successful} successful seqs of length {l}, given below\\")
    # print_all(l)