# note: this file is a work in progress, the indexing could be much cleaner

from projective_utils import get_pd_of_fq, is_good_set_all_coords_fixed, sequence_to_string, collection_to_string

def build_will_sequence(k, num_generators, q, length):
    d = num_generators - 1
    pd_fq = list(get_pd_of_fq(d=d, q=q))
    w = len(pd_fq)
    print(w)

    # seq_indices will be the indices of the elements in pd_fq
    seq_indices = []

    for i in range(1, length + 1):
        if i % k == 0:
            # python lists are 0-indexed, the sequence is 1-indexed
            seq_indices.append((seq_indices[i//k -1] + 1) % w)
        else:
            seq_indices.append((i % k) % w) 
    
    seq = [pd_fq[i] for i in seq_indices]
    return seq

def check_will_sequence_with_restricted_good_sets(seq, d, q, k):
    n = int(k ** len(get_pd_of_fq(d=d, q=q)))

    for endpoint in range(1, len(seq) + 1):
        # check that everything in seq[0:endpoint]
        # satisfies all constraints that make sense
        m = 1
        while m * n <= endpoint:
            # creates all tuples except for the last one, python quirk
            length_m_tuples = [tuple(seq[endpoint-m*(j+1) : endpoint-m*j]) for j in range (0, n)]
            if not is_good_set_all_coords_fixed(length_m_tuples, d=d, q=q):
                print(collection_to_string(c=length_m_tuples, q=q, d=d))
                return False
            
            m *= k
    
    return True

def build_and_check_will_sequence(k, num_generators, q, length): 
    will_seq = build_will_sequence(k, num_generators, q, length)
    print(sequence_to_string(d=num_generators-1, q=q, seq=will_seq))
    is_good = check_will_sequence_with_restricted_good_sets(seq=will_seq, d=num_generators-1, q=q, k=k) 
    print(is_good)

if __name__ == "__main__":
    build_and_check_will_sequence(k=2, num_generators=2, q=2, length=10000)
        

