from bibgrafo.grafo_lista_adjacencia import GrafoListaAdjacencia
from meu_grafo import MeuGrafo

paraiba=MeuGrafo()

l_cidades=['J','C','E','P','M','T','Z']
l_arestas=['a1','a2','a3','a4','a5','a6','a7','a8','a9']
l_ax=['JC','CE','CE','CP','CP','CM','CT','MT','TZ']

for aresta in range(len(l_arestas)):
    if aresta==0:
        for cidade in l_cidades:
            paraiba.adicionaVertice(cidade)

    paraiba.adicionaAresta(l_arestas[aresta], l_ax[aresta][0], l_ax[aresta][1])

print(paraiba)

