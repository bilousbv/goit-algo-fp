class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Додає елемент у кінець списку"""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        """Виводить список"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print(" -> ".join(map(str, elements)))

    def reverse(self):
        """Реверсує однозв'язний список, змінюючи посилання між вузлами"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        """Сортування однозв'язного списку методом злиття"""
        if not self.head or not self.head.next:
            return

        self.head = self.merge_sort(self.head)

    def merge_sort(self, head):
        """Рекурсивна функція сортування злиттям для однозв'язного списку"""
        if not head or not head.next:
            return head

        # Знаходимо середину списку
        middle = self.get_middle(head)
        next_to_middle = middle.next
        middle.next = None

        # Рекурсивно сортуємо обидві половини
        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        # Зливаємо відсортовані половини
        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        """Знаходить середину списку для сортування злиттям"""
        if not head:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sorted_merge(self, left, right):
        """Зливає два відсортовані списки"""
        if not left:
            return right
        if not right:
            return left
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result

    def merge_with(self, other):
        """Об'єднує поточний список з іншим відсортованим списком"""
        self.head = self.sorted_merge(self.head, other.head)

def main():
    # Створення списків
    list1 = LinkedList()
    list1.append(3)
    list1.append(1)
    list1.append(4)
    list1.append(2)

    print("Список 1 до сортування:")
    list1.display()

    # Сортування списку 1
    list1.sort()
    print("Список 1 після сортування:")
    list1.display()

    # Реверсування списку 1
    list1.reverse()
    print("Список 1 після реверсування:")
    list1.display()

    # Створення та сортування другого списку
    list2 = LinkedList()
    list2.append(5)
    list2.append(7)
    list2.append(6)

    print("Список 2:")
    list2.display()

    # Об'єднання двох списків
    list1.sort()  # Повертаємо порядок
    list1.merge_with(list2)
    print("Об'єднаний відсортований список:")
    list1.display()

if __name__ == "__main__":
    main()