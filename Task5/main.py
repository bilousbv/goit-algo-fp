import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.colors import to_hex


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def build_graph(tree_root):
    """Побудова графа для дерева без рекурсії."""
    graph = nx.DiGraph()
    pos = {}
    queue = deque([(tree_root, 0, 0, 1)])  # черга з кореневим вузлом і його позицією
    while queue:
        node, x, y, layer = queue.popleft()
        if node is not None:
            graph.add_node(node.id, label=node.val)
            pos[node.id] = (x, y)

            # Додаємо лівого нащадка
            if node.left:
                graph.add_edge(node.id, node.left.id)
                queue.append((node.left, x - 1 / 2 ** layer, y - 1, layer + 1))

            # Додаємо правого нащадка
            if node.right:
                graph.add_edge(node.id, node.right.id)
                queue.append((node.right, x + 1 / 2 ** layer, y - 1, layer + 1))

    return graph, pos


def draw_tree(graph, pos, visited_nodes=None):
    """Візуалізація дерева з кольорами для відвіданих вузлів."""
    colors = []
    labels = {node[0]: node[1]['label'] for node in graph.nodes(data=True)}
    for node in graph.nodes():
        colors.append(visited_nodes.get(node, "#991B1B"))  # Червоний колір для невідвіданих вузлів

    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors, font_color="#ffffff")
    plt.show()


def generate_colors(steps):
    """Генерує градієнт кольорів від темного до світлого на основі кількості кроків."""
    colors = []
    for i in range(steps):
        intensity = 0.1 + (0.9 * i / steps)  # Інтенсивність від 0.1 до 1
        color = to_hex((0.2 * intensity, 0.5 * intensity, 1.0 * intensity))  # Градієнт від синього до світлого
        colors.append(color)
    return colors


def dfs(tree_root, graph, pos):
    """Обхід в глибину (DFS) з використанням стека."""
    stack = [tree_root]
    visited_nodes = {}
    colors = generate_colors(15)  # Генеруємо достатню кількість кольорів

    step = 0
    while stack:
        node = stack.pop()
        if node and node.id not in visited_nodes:
            visited_nodes[node.id] = colors[step]
            step += 1
            draw_tree(graph, pos, visited_nodes)  # Відображення поточного стану дерева
            stack.append(node.right)  # Додаємо правого нащадка в стек
            stack.append(node.left)   # Додаємо лівого нащадка в стек
    return visited_nodes


def bfs(tree_root, graph, pos):
    """Обхід в ширину (BFS) з використанням черги."""
    queue = deque([tree_root])
    visited_nodes = {}
    colors = generate_colors(15)  # Генеруємо достатню кількість кольорів

    step = 0
    while queue:
        node = queue.popleft()
        if node and node.id not in visited_nodes:
            visited_nodes[node.id] = colors[step]
            step += 1
            draw_tree(graph, pos, visited_nodes)  # Відображення поточного стану дерева
            queue.append(node.left)   # Додаємо лівого нащадка в чергу
            queue.append(node.right)  # Додаємо правого нащадка в чергу
    return visited_nodes


def main():
    # Створення дерева
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    # Побудова графа
    graph, pos = build_graph(root)

    # Виклик DFS і BFS з візуалізацією
    print("DFS Traversal:")
    dfs(root, graph, pos)

    print("BFS Traversal:")
    bfs(root, graph, pos)


if __name__ == "__main__":
    main()
