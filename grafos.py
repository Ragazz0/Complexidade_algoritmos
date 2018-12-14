grafo = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

grafo_kruskal = {
'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
'arestas': set([
(7, 'A', 'B'),
(5, 'A', 'D'),
(7, 'B', 'A'),
(8, 'B', 'C'),
(9, 'B', 'D'),
(7, 'B', 'E'),
(8, 'C', 'B'),
(5, 'C', 'E'),
(5, 'D', 'A'),
(9, 'D', 'B'),
(7, 'D', 'E'),
(6, 'D', 'F'),
(7, 'E', 'B'),
(5, 'E', 'C'),
(15, 'E', 'D'),
(8, 'E', 'F'),
(9, 'E', 'G'),
(6, 'F', 'D'),
(8, 'F', 'E'),
(11, 'F', 'G'),
(9, 'G', 'E'),
(11, 'G', 'F'),
])
}

# Vértices do grafo são representados como números
a, b, c, d, e, f = 0, 1, 2, 3, 4, 5
grafo_prim = [
  [a,b,2],
  [a,c,3],
  [b,d,3],
  [b,c,5],
  [b,e,4],
  [c,e,4],
  [d,e,2],
  [d,f,3],
  [e,f,5]
]

grafo_dijkstra = {'s': {'a': 2, 'b': 1},
        'a': {'s': 3, 'b': 4, 'c':8},
        'b': {'s': 4, 'a': 2, 'd': 2},
        'c': {'a': 2, 'd': 7, 't': 4},
        'd': {'b': 1, 'c': 11, 't': 5},
        't': {'c': 3, 'd': 5}}