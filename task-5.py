import uuid
import networkx as nx
import matplotlib.pyplot as plt
import time
from matplotlib import colors as mcolors


class Node:
    def __init__(self, key, color="#D3D3D3"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root, pause=1.0):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.clf()
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.pause(pause)


def get_colormap(n):
    return [mcolors.to_hex(mcolors.to_rgb(f'#0000{format(100 + int(i * (155 / n)), "02x")}')) for i in range(n)]


def dfs(node, visited, colors, counter):
    if node is None or node.id in visited:
        return counter
    visited.add(node.id)
    node.color = colors[counter]
    draw_tree(root)
    counter += 1
    counter = dfs(node.left, visited, colors, counter)
    counter = dfs(node.right, visited, colors, counter)
    return counter


def bfs(node, colors):
    from collections import deque
    queue = deque()
    queue.append(node)
    visited = set()
    i = 0
    while queue:
        current = queue.popleft()
        if current.id in visited:
            continue
        visited.add(current.id)
        current.color = colors[i]
        draw_tree(root)
        i += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)



root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)


plt.ion()


all_nodes = [root, root.left, root.left.left, root.left.right, root.right, root.right.left]
dfs_colors = get_colormap(len(all_nodes))

print("DFS:")
dfs(root, set(), dfs_colors, 0)
time.sleep(2)

# reset color
for node in all_nodes:
    node.color = "#D3D3D3"

bfs_colors = get_colormap(len(all_nodes))

print("BFS:")
bfs(root, bfs_colors)
plt.ioff()
plt.show()
