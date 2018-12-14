from grafos import grafo_prim

def criarMatriz(V, G):
  
  matriz_adjacente = []
  
  # Matriz N x N preenchida com peso 0 entre todas as vértices
  for i in range(0, V):
    matriz_adjacente.append([])
    for j in range(0, V):
      matriz_adjacente[i].append(0)
      
  # Popula a matriz com os pesos corretos
  for i in range(0, len(G)):
    matriz_adjacente[G[i][0]][G[i][1]] = G[i][2]
    matriz_adjacente[G[i][1]][G[i][0]] = G[i][2]
    
  return matriz_adjacente

def prims(V, G):
  
  # Cria a matriz a partir dos valores do grafo_prim
  matriz_adjacente = criarMatriz(V, G)
  
  # Vértice inicial
  vertice = 0
  
  
  MST = [] # Inicializa a árvore de extensão mínima vazia
  borda = [] # inicializa os vértices vazios
  visitados = [] 
  vertice_minimo = [None,None,float('inf')]
  
  # O algoritmo vai rodar até encrontrar a árvore de extensão mínima ideal que contém todos os vértices do grafo
  while len(MST) != V-1:
    
    # Marca o vértice como visitado
    visitados.append(vertice)
    
    # Adiciona à cada borda um vertice potencial
    for r in range(0, V):
      if matriz_adjacente[vertice][r] != 0:
        borda.append([vertice,r,matriz_adjacente[vertice][r]])
        
    # Encontra a borda com menor peso para um vértice 
    for e in range(0, len(borda)):
      if borda[e][2] < vertice_minimo[2] and borda[e][1] not in visitados:
        vertice_minimo = borda[e]
        
    # Remove a borda com peso mínimo da lista de bordas
    borda.remove(vertice_minimo)

    # Adiciona esse vértice à árvore de extensão mínima
    MST.append(vertice_minimo)
      
    # Inicia outro vértice e reseta a borda
    vertice = vertice_minimo[1]
    vertice_minimo = [None,None,float('inf')]
    
  return MST

# Passa como argumento a quantidade de bordas e o grafo
print('Árvore de extensão mínima:', prims(6, grafo_prim))