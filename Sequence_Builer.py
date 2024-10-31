GLOBAL_LOG_FLAG = False
def log(log_str):
  if GLOBAL_LOG_FLAG:
    print(log_str)


class SequenceBuilder:
  def __init__(self, q, num_tuples_per_window, max_build_length):
    self.q = q
    self.num_tuples_per_window = num_tuples_per_window
    self.max_build_length = max_build_length

    # successful_sequences[i] = a set of sequences of length i that meet the constraints 
    self.successful_sequences = [set() for _ in range(max_build_length + 1)]

  def satisfies_contraints(self, seq):
    '''
    for each degree m, there must be q + 1 distinct m-tuples in every 
    window of num_tuples_per_window many m-tuples. We check the window ending at the last element, 
    since all previous windows will have been checked before. We check for every m that stays in bounds.
    '''

    log(f"Seeing if sequence {seq} satisfies constraints with window_size = " + 
      f"{num_tuples_per_window} and q = {q}")

    # degree we are considering,aka size of the tuple 
    m = 1
    while m * self.num_tuples_per_window <= len(seq):
      # check that the window ending here works for degree m

      # creates all tuples except for the last one, python quirk
      length_m_tuples = {seq[-m*(j+1) : -m*j] for j in range (1, self.num_tuples_per_window)}

      # add the last one 
      length_m_tuples.add(seq[-m:])

      if len(length_m_tuples) < self.q + 1:
        log(f"failed to satisfy constraints at m = {m}")
        return False


      # log(f"There {len(length_m_tuples)} many length-m tuples in the past " + 
      #   f"window-size many {m}-tuples, they are {length_m_tuples}")

      m += 1

    return True

  def build_sequences(self):
    # start the sequence as 12...q(q+1)
    intial_sequence = "".join(str(j) for j in range(1, q+1))

    self.build_sequence_recur(intial_sequence)

  def build_sequence_recur(self, cur_sequence):
    if not self.satisfies_contraints(cur_sequence):
      return
    
    self.successful_sequences[len(cur_sequence)].add(cur_sequence)

    if len(cur_sequence) == self.max_build_length:
      return

    # try adding everything from 1 up to q+1 (inclusive) to the sequence
    for next_elt in range(1, q + 2):
      next_seq = cur_sequence + str(next_elt)
      self.build_sequence_recur(next_seq)

if __name__ == "__main__":
  # size of the finite field. Remember the projective space has 
  # size q + 1
  q = 2

  # this is the degree of nilpotency for each element as well
  num_tuples_per_window = q + 2

  max_build_length = 25

  sb = SequenceBuilder(q, num_tuples_per_window, max_build_length)

  sb.build_sequences()
  
  # for l in range(num_tuples_per_window, len(sb.successful_sequences)):
  #   print(f"There are {len(sb.successful_sequences[l])} good seqs of length {l}")

  # make markdown table 
  for l in range(num_tuples_per_window, len(sb.successful_sequences)):
    print(f"| {l} | {len(sb.successful_sequences[l])} |")
'''
q = 2, num_tuples_per_window = 4 we can do max_build_length = 25, get the following data:
There are 5 good seqs of length 4
There are 9 good seqs of length 5
There are 17 good seqs of length 6
There are 31 good seqs of length 7
There are 52 good seqs of length 8
There are 92 good seqs of length 9
There are 160 good seqs of length 10
There are 282 good seqs of length 11
There are 466 good seqs of length 12
There are 770 good seqs of length 13
There are 1297 good seqs of length 14
There are 2202 good seqs of length 15
There are 3724 good seqs of length 16
There are 6335 good seqs of length 17
There are 10770 good seqs of length 18
There are 18297 good seqs of length 19
There are 31028 good seqs of length 20
There are 52648 good seqs of length 21
There are 89324 good seqs of length 22
There are 151477 good seqs of length 23
There are 256868 good seqs of length 24
There are 435710 good seqs of length 25

It looks roughly O(2^n)
any bigger max_build_length is too slow

'''