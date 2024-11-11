from projective_utils import generate_all_length_m_tuples, collection_to_string
from HyperSurfaceSet import HyperSurfaceSet 

# returns a dictionary which maps surfaces 
# to a list of points lying on that surface, 
# referred to as an "incidence_map" in this file
def get_all_incidence_relations(q, m, d=1):
    all_tuples = generate_all_length_m_tuples(q=q, m=m, d=d)
    surface_set = HyperSurfaceSet(q=q, m=m, d=d)

    return {s: [pt for pt in all_tuples if surface_set.point_on_surface(pt=pt, surface=s)]
                 for s in surface_set.hyper_surfaces}

# mostly for testing
def get_incidence_histogram(incidence_map):
    freq_map = {} 
    for s in incidence_map:
        num_pts_on_s = len(incidence_map[s])
        freq_map[num_pts_on_s] = freq_map.get(num_pts_on_s, 0) + 1
    print(freq_map)
    return freq_map

def print_all_incidence_relations(incidence_map, q, d=1):
    # label the surfaces with numbers, the equations don't mean much
    i = 0 
    print("Surface label | points \n --- | ---")
    for s in incidence_map:
        print(f"{i} | {collection_to_string(incidence_map[s], q=q, d=d)}")
        i += 1


def print_incidence_hisogram(incidence_map):
    freq_map = get_incidence_histogram(incidence_map)
    
    sorted_freqs = sorted([(size, freq_map[size]) for size in freq_map], key = lambda x: x[0])
    for size, freq_of_size in sorted_freqs:
        print(f"Number of surfaces with {size} points on them: {freq_of_size} \\")

if __name__ == "__main__":
    cur_q = 2
    cur_m = 2
    cur_d = 2

    relations = get_all_incidence_relations(q=cur_q, m=cur_m, d=cur_d)
    print_all_incidence_relations(relations, cur_q, d=cur_d)
    print()
    print_incidence_hisogram(relations)