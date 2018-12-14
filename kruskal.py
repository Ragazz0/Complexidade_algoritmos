from grafos import grafo_kruskal

pai = dict()
rank = dict()

def criar_ponto(vertice):
    pai[vertice] = vertice
    rank[vertice] = 0

def procurar(vertice):
    if pai[vertice] != vertice:
        pai[vertice] = procurar(pai[vertice])
    return pai[vertice]

def uniao(vertice1, vertice2):
    raizA = procurar(vertice1)
    raizB = procurar(vertice2)
    
    if raizA != raizB:
    
        if rank[raizA] > rank[raizB]:
            pai[raizB] = raizA
    else:
	    pai[raizA] = raizB

    if rank[raizA] == rank[raizB]: rank[raizB] += 1

def kruskal(grafo_kruskal, show_weight):
    for vertice in grafo_kruskal['vertices']:
        criar_ponto(vertice)
        minimum_spanning_tree = set()
        arestas = list(grafo_kruskal['arestas'])
        arestas.sort()

    for edge in arestas:
        weight, vertice1, vertice2 = edge

        if(show_weight):
            print('Weight: ', weight, vertice1, vertice2)

        if procurar(vertice1) != procurar(vertice2):
            uniao(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
	    
    return sorted(minimum_spanning_tree)

caminho = kruskal(grafo_kruskal, show_weight=False) # True : mostra o peso do caminho entre os vértices | False : mostra apenas o caminho percorrido

print('Caminho percorrido: ', caminho)