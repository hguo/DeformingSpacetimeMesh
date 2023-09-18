from nodeElimination import *

if __name__ == "__main__":
    with open("dataGen/syn_mesh.pickle", "rb") as f:
        nodes_coor, cells = pickle.load(f)
    with open("dataGen/next_nodes.pickle", "rb") as f:
        next_nodes = pickle.load(f)

    edges_to_draw = [((695, 'l'), (778, 'l')), ((959, 'l'), (960, 'l')), ((867, 'l'), (960, 'l')),
                     ((866, 'l'), (867, 'l')), ((779, 'l'), (867, 'l')), ((866, 'l'), (959, 'l')),
                     ((865, 'l'), (959, 'l')), ((865, 'l'), (866, 'l')), ((695, 'l'), (779, 'l')),
                     ((778, 'l'), (779, 'l')), ((694, 'l'), (778, 'l')), ((867, 'l'), (959, 'l')),
                     ((694, 'l'), (695, 'l')), ((778, 'l'), (866, 'l')), ((778, 'l'), (867, 'l')),
                     ((783, 'u'), (871, 'u')), ((783, 'u'), (872, 'u')), ((871, 'u'), (965, 'u')),
                     ((872, 'u'), (873, 'u')), ((873, 'u'), (966, 'u')), ((871, 'u'), (872, 'u')),
                     ((699, 'u'), (700, 'u')), ((872, 'u'), (966, 'u')), ((784, 'u'), (872, 'u')),
                     ((872, 'u'), (965, 'u')), ((699, 'u'), (783, 'u')), ((699, 'u'), (784, 'u')),
                     ((783, 'u'), (784, 'u')), ((965, 'u'), (966, 'u')), ((784, 'u'), (873, 'u')),
                     ((700, 'u'), (784, 'u')), ((694, 'l'), (699, 'u')), ((695, 'l'), (700, 'u')),
                     ((778, 'l'), (783, 'u')), ((779, 'l'), (873, 'u')), ((865, 'l'), (871, 'u')),
                     ((866, 'l'), (783, 'u')), ((867, 'l'), (873, 'u')), ((959, 'l'), (965, 'u')),
                     ((960, 'l'), (966, 'u')), ((694, 'l'), (700, 'u')), ((695, 'l'), (784, 'u')),
                     ((779, 'l'), (784, 'u')), ((867, 'l'), (966, 'u')), ((959, 'l'), (966, 'u')),
                     ((865, 'l'), (965, 'u')), ((866, 'l'), (871, 'u')), ((694, 'l'), (783, 'u'))]
    adjacency_list = {}
    for e in edges_to_draw:
        try:
            adjacency_list[e[0]].append(e[1])
        except:
            adjacency_list[e[0]] = [e[1]]
        try:
            adjacency_list[e[1]].append(e[0])
        except:
            adjacency_list[e[1]] = [e[0]]
    boundary_triangles = [((694, 'l'), (695, 'l'), (700, 'u')), ((694, 'l'), (699, 'u'), (700, 'u')),
                          ((695, 'l'), (700, 'u'), (784, 'u')), ((695, 'l'), (779, 'l'), (784, 'u')),
                          ((779, 'l'), (784, 'u'), (873, 'u')), ((779, 'l'), (867, 'l'), (873, 'u')),
                          ((867, 'l'), (873, 'u'), (966, 'u')), ((867, 'l'), (960, 'l'), (966, 'u')),
                          ((959, 'l'), (960, 'l'), (966, 'u')), ((959, 'l'), (965, 'u'), (966, 'u')),
                          ((865, 'l'), (959, 'l'), (965, 'u')), ((865, 'l'), (871, 'u'), (965, 'u')),
                          ((865, 'l'), (866, 'l'), (871, 'u')), ((866, 'l'), (783, 'u'), (871, 'u')),
                          ((778, 'l'), (866, 'l'), (783, 'u')), ((694, 'l'), (778, 'l'), (783, 'u')),
                          ((694, 'l'), (699, 'u'), (783, 'u'))]
    all_tetrahedra = nodeElimination(adjacency_list, boundary_triangles, nodes_coor)
    print(all_tetrahedra)

    # a = [[(554, 'u'), (628, 'u'), (553, 'u'), (549, 'l')], [(549, 'l'), (552, 'u'), (553, 'u'), (627, 'u')],
    #      [(549, 'l'), (553, 'u'), (627, 'u'), (628, 'u')], [(548, 'l'), (549, 'l'), (552, 'u'), (627, 'u')]]
