from projective_utils import generate_all_length_m_tuples, collection_to_string
from HyperSurfaceSet import HyperSurfaceSet 

# returns a dictionary which maps surfaces 
# to a list of points lying on that surface, 
# referred to as an "incidence_map" in this file
def get_all_incidence_relations(q, m):
    all_tuples = generate_all_length_m_tuples(q=q, m=m)
    surface_set = HyperSurfaceSet(q=q, m=m)

    return {s:[pt for pt in all_tuples if surface_set.point_on_surface(pt=pt, surface=s)]
                 for s in surface_set.hyper_surfaces}


def print_all_incidence_relations(incidence_map, q):
    # label the surfaces with numbers, the equations don't mean much
    i = 0 
    print("Surface label | points")
    print(" --- | ---")
    for s in incidence_map:
        print(f"{i} | {collection_to_string(incidence_map[s], q=q)}")
        i += 1


def print_incidence_hisogram(incidence_map):
    freq_map = {} 
    for s in incidence_map:
        num_pts_on_s = len(incidence_map[s])
        freq_map[num_pts_on_s] = freq_map.get(num_pts_on_s, 0) + 1
    
    sorted_freqs = sorted([(size, freq_map[size]) for size in freq_map], key = lambda x: x[0])
    for size, freq_of_size in sorted_freqs:
        print(f"Number of surfaces with {size} points on them: {freq_of_size} \\")

if __name__ == "__main__":
    q = 2
    m = 3

    relations = get_all_incidence_relations(q=q, m=m)
    print_all_incidence_relations(relations, q)
    print()
    print_incidence_hisogram(relations)