# note: this file is a work in progress, the indexing could be much cleaner

from projective_utils import get_pd_of_fq, is_good_set_all_coords_fixed, sequence_to_string, collection_to_string, is_set_simple


def max_power(n, k):
  power = 0
  while n % k == 0:
    power += 1
    n //= k
  return power

def build_will_sequence(k, num_generators, q, length):
    d = num_generators - 1
    pd_fq = list(get_pd_of_fq(d=d, q=q))
    w = len(pd_fq)

    # seq_indices will be the indices of the elements in pd_fq
    seq_indices = []

    for i in range(1, length + 1):
        if i % k == 0:
            # python lists are 0-indexed, the sequence is 1-indexed
            seq_indices.append((seq_indices[i//k -1] + 1) % w)
        else:
            seq_indices.append(((i-1) % k) % w) 
    
    seq = [pd_fq[i] for i in seq_indices]
    return seq

def check_will_sequence_with_restricted_good_sets(seq, d, q, k):
    n = int(k ** len(get_pd_of_fq(d=d, q=q)))

    for endpoint in range(1, len(seq) + 1):
        # check that everything in seq[0:endpoint]
        # satisfies all constraints that make sense
        m = 1
        while m * n <= endpoint:
            length_m_tuples = [tuple(seq[endpoint-m*(j+1) : endpoint-m*j]) for j in range (0, n)]
            if not is_set_simple(length_m_tuples, d=d, q=q):
                return False
            
            m *= k
        
    return True

# only checks the given m value, using the value of N. Typically N = Jn 
# for some natural number J
def check_will_sequence_works_particular_m(num_generators, q, k, m, N, num_offsets_to_check):
    # first we need to determine the length of the sequence required to check the number 
    # of offsets requested. We can check one offset is length = N * m, two if length is N * m + 1, 
    # etc. In general we should have length N * m + num_offsets_to_check - 1 
    seq_length = N * m + num_offsets_to_check - 1
    will_seq = build_will_sequence(k=k, num_generators=num_generators, q=q, length=seq_length)

    d = num_generators - 1
    # sanity check
    assert len(will_seq) == seq_length 

    print(seq_length)

    for endpoint in range(N * m, seq_length): 
        length_m_tuples = [tuple(will_seq[endpoint-m*(j+1) : endpoint-m*j]) for j in range (0, N)]

        assert len(length_m_tuples) == N

        if not is_set_simple(length_m_tuples, d=d, q=q):
            return False 
    
    return True

def find_multiple_of_k_w_required_for_m(num_generators, q, k, m, num_offsets_to_check, max_multiple_to_check):
    d = num_generators - 1
    w = len(get_pd_of_fq(d=d, q=q))
    k_w = int(k**w)

    for multiple in range(1, max_multiple_to_check + 1):
        if check_will_sequence_works_particular_m(num_generators, q, k, m, multiple * k_w, num_offsets_to_check):
            print(f"{multiple} * k^w works for m = {m}")
            return multiple
        else: 
            print(f"{multiple} * k^w does NOT work for m = {m}")
    
    print(f"No multiple found for m = {m}, checked up to {max_multiple_to_check}")
    return -1

def get_multiple_for_each_m(num_generators, q, k, m_min, m_max, num_offsets_to_check, max_multiple_to_check):
    results = {}
    for m in range(m_min, m_max + 1): 
        if m % k == 0:
            continue 
        mult_required = find_multiple_of_k_w_required_for_m(num_generators, q, k, m, num_offsets_to_check, max_multiple_to_check)
        results[m] = mult_required 

    for m in results:
        # print(f"For m = {m}, J_m = {results[m]}")
        print(f"{m} & {results[m]} \\\\")
    

def will_sequence_works(k, num_generators, q, length): 
    will_seq = build_will_sequence(k, num_generators, q, length)

    # print(sequence_to_string(d=num_generators-1, q=q, seq=will_seq))
    return check_will_sequence_with_restricted_good_sets(seq=will_seq, d=num_generators-1, q=q, k=k) 
    
def check_many_values(k_min, k_max, gen_min, gen_max, q_set, length): 
    return all(
        will_sequence_works(k=k, num_generators=g, q=q, length=length)
        for k in range(k_min, k_max + 1) 
        for g in range(gen_min, gen_max + 1)
        for q in q_set
    )


if __name__ == "__main__":
    get_multiple_for_each_m(num_generators=2, q=2, k=3, m_min=30, m_max=60, num_offsets_to_check=1000, max_multiple_to_check=50)
        

