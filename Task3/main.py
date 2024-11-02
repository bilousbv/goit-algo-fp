import heapq


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, u, v, weight):
        """Додає орієнтоване ребро з вершини u в вершину v з вагою weight"""
        if u not in self.nodes:
            self.nodes[u] = []
        if v not in self.nodes:
            self.nodes[v] = []
        self.nodes[u].append((v, weight))
        # Якщо граф неорієнтований, розкоментуйте наступний рядок
        # self.nodes[v].append((u, weight))

    def dijkstra(self, start):
        """Алгоритм Дейкстри для знаходження найкоротших шляхів від вершини start"""
        distances = {node: float('inf') for node in self.nodes}  # Відстані до всіх вершин
        distances[start] = 0  # Відстань до початкової вершини
        priority_queue = [(0, start)]  # Мінімальна купа (відстань, вершина)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Пропускаємо вершину, якщо ми знайшли кращий шлях
            if current_distance > distances[current_node]:
                continue

            # Перевіряємо сусідів поточної вершини
            for neighbor, weight in self.nodes[current_node]:
                distance = current_distance + weight

                # Якщо знайдено коротший шлях до сусіда
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def main():
    # Приклад використання
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'E', 3)
    graph.add_edge('E', 'D', 4)
    graph.add_edge('D', 'F', 11)

    # Знаходимо найкоротші шляхи від вершини 'A'
    start_node = 'A'
    distances = graph.dijkstra(start_node)
    print(f"Найкоротші відстані від вершини '{start_node}':")
    for node, distance in distances.items():
        print(f"{start_node} -> {node}: {distance}")


if __name__ == "__main__":
    main()
