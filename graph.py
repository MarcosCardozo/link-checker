import json
import networkx as nx
import matplotlib.pyplot as plt

# Cargar los datos desde el archivo JSON
with open('output.json') as f:
    data = json.load(f)

# Crear un grafo dirigido
graph = nx.DiGraph()

# Agregar nodos y aristas al grafo
for entry in data:
    url = entry['url']
    status = entry['estado']
    links = entry['enlaces']

    graph.add_node(url, status=status)

    # Se agrega la arista a los nodos que tienen un 'enlace'
    for link in links:
        graph.add_edge(url, link)

pos = nx.spring_layout(graph)

# Dibujar los nodos
nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=500)

# Dibujar las aristas
nx.draw_networkx_edges(graph, pos, edge_color='gray', width=1.0)

# Dibujar las etiquetas de los nodos, en este caso las url
nx.draw_networkx_labels(graph, pos, font_size=8, font_color='black')

# Mostrar el grafo
plt.axis('off')
plt.show()




