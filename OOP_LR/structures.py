class StructureError(Exception):
    """Базовый класс для всех исключений структур данных"""
    pass

class EmptyStructureError(StructureError):
    """Ошибка при попытке операции с пустой структурой"""
    def __init__(self, structure_name, message="Structure is empty"):
        self.structure_name = structure_name
        super().__init__(f"{message}: {structure_name}")

class IndexError(StructureError):
    """Ошибка при обращении по несуществующему индексу"""
    def __init__(self, index, message="Index out of range"):
        self.index = index
        super().__init__(f"{message}: {index}")

class ValueNotFoundError(StructureError):
    """Ошибка при поиске несуществующего значения"""
    def __init__(self, value, message="Value not found"):
        self.value = value
        super().__init__(f"{message}: {value}")


class Node:
    """Класс, представляющий узел односвязного списка."""

    def __init__(self, data = 0, next = None):
        """
        Конструктор узла. 
        Поддерживает 0, 1 или 2 параметра благодаря значениям по умолчанию.
        """
        self.data = data
        self.next = next

    def clear(self):
        """Обнуляет данные и убирает ссылку на следующий узел."""
        self.data = 0
        self.next = None

    def __str__(self):
        """Строковое представление узла."""
        return f"Node({self.data})"
    
class SinglyLinkedList:
    """Односвязный список (композиция с классом Node)."""

    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, data):
        """Добавление элемента в начало списка."""
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1

    def append(self, data):
        """Добавление элемента в конец списка."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            self.size += 1

    def insert_after(self, index, data):
        """Добавление элемента после элемента с указанным индексом."""
        if (index < 0 or index >= self.size):
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node = Node(data, current.next)
            current.next = new_node
            self.size += 1

    def insert_before(self, index, data):
        """Добавление элемента перед элементом с указанным индексом."""
        if (index < 1 or index >= self.size):
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node = Node(data, current.next)
            current.next = new_node
            self.size += 1

    def remove_first(self):
        """Удаление первого элемента."""
        if (self.head is None):
            raise EmptyStructureError("SinglyLinkedList")
        else:
            data = self.head.data
            old_head = self.head
            self.head = self.head.next
            old_head.clear()
            self.size -= 1
            return data
    
    def remove_last(self):
        """Удаление последнего элемента."""
        if (self.head is None):
            raise EmptyStructureError("SinglyLinkedList")
        current = self.head
        while (current.next.next):
            current = current.next
        data = current.next.data
        current.next.clear()
        current.next = None
        self.size -= 1
        return data

    def remove_at(self, index):
        """Удаление элемента по индексу."""
        if (index < 0 or index >= self.size):
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            target = current.next
            data = target.data
            current.next = target.next
            target.clear()
            self.size -= 1
            return data
    
    def remove_value(self, value):
        """Удаление первого вхождения указанного значения."""
        current = self.head
        if (self.head is None):
            raise EmptyStructureError("SinglyLinkedList")
        
        if self.head.data == value:
            return self.remove_first()

        while (current.next):
            if current.next.data == value:
                target = current.next
                data = target.data
                current.next = target.next
                target.clear()
                self.size -= 1
                return data
            current = current.next
        raise ValueNotFoundError(value)

    def find(self, value):
        """Поиск индекса первого вхождения значения. Возвращает -1, если не найдено."""
        counter = 0
        current = self.head

        while (counter < self.size):
            if (current.data == value):
                return counter
            counter += 1
            current = current.next
        return -1

    def find_all(self, value): #список индексов
        """Поиск индексов всех вхождений значения."""
        counter = 0
        current = self.head
        index_arr = []

        while (counter < self.size):
            if (current.data == value):
                index_arr.append(counter)
            counter += 1
            current = current.next
        return index_arr

    def contains(self, value): #t/f
        """Проверка наличия значения в списке."""
        current = self.head

        while (current.next):
            if (current.data == value):
                return True
            current = current.next
        return False

    def get(self, index): #значение элемента по индексу
        """Получение значения элемента по индексу."""
        if (index < 0 or index >= self.size):
            raise IndexError(index)
        current = self.head

        for _ in range(index):
            current = current.next
        return current.data
    
    def __len__(self):
        return self.size

    def __str__(self):
        if (not self.head):
            return "None"
        else:
            stroke = ""
            current = self.head
            stroke += str(current.data) + " -> "
            while(current.next):
                current = current.next
                stroke += str(current.data) + " -> "
            stroke += "None"
            return stroke

    def __iter__(self):
        current = self.head
        while (current):
            yield current.data
            current = current.next

    def clear(self):
        """Очистка списка."""
        self.head = None
        self.size = 0

    def __getitem__(self, index):
        return self.get(index)
    
    def __setitem__(self, index, value):
        if (index < 0 or index >= self.size):
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.data = value
    
    def __contains__(self, value):
        return self.contains(value)
    
    def __add__(self, other):
        new_arr = SinglyLinkedList()

        for item in self:
            new_arr.append(item)

        for item in other:
            new_arr.append(item)
        return new_arr
    
    def __mul__(self, count):
        new_arr = SinglyLinkedList()

        for _ in range(count):
            for item in self:
                new_arr.append(item)
        return new_arr




class DoubleNode(Node):
    """Узел двусвязного списка (наследование от Node)."""
    def __init__(self, data=0, next=None, prev=None):
        super().__init__(data, next)
        self.prev = prev

class DoublyLinkedList(SinglyLinkedList):
    """Двусвязный список с поддержкой head и tail."""
    def __init__(self):
        super().__init__()
        self.tail = None

    def prepend(self, data):
        """Добавление элемента в начало списка."""
        new_node = DoubleNode(data, self.head)
        if (self.head):
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
        self.size += 1

    def append(self, data):
        """Добавление элемента в конец списка."""
        new_node = DoubleNode(data)
        if (not self.head):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1


    def insert_before(self, index, data):
        """Добавление элемента перед элементом с указанным индексом."""
        if index < 0 or index >= self.size:
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node = DoubleNode(data, current.next, current.prev)
            current.prev.next = new_node
            current.prev = new_node
            self.size += 1

    def insert_after(self, index, data):
        """Добавление элемента после элемента с указанным индексом."""
        if index < 0 or index >= self.size:
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node = DoubleNode(data, current.next, current)
            current.next.prev = new_node
            current.next = new_node
            self.size += 1
    
    def remove_first(self):
        """Удаление первого элемента."""
        if (self.head is None):
            raise EmptyStructureError("DoublyLinkedList")
        else:
            rm_data = self.head.data
            self.head = self.head.next
            self.head.prev = None
            self.size -= 1
            return rm_data

    def remove_last(self):
        """Удаление последнего элемента."""
        if self.tail is None:
            raise EmptyStructureError("DoublyLinkedList")
        else:
            rm_data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            self.size -= 1
            return rm_data
    
    def remove_at(self, index):
        """Удаление элемента по индексу."""
        if index < 0 or index >= self.size:
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            rm_data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return rm_data
    
    def remove_value(self, value):
        """Удаление первого вхождения указанного значения."""
        if self.head is None:
            raise EmptyStructureError("DoublyLinkedList")
        else:
            current = self.head
            while (current):
                if (current.data == value):
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.size -= 1
                    return value
                current = current.next
            raise ValueNotFoundError(value)

    def find(self, value):
        """Поиск индекса первого вхождения значения. Возвращает -1, если не найдено."""
        return super().find(value)
    
    def find_all(self, value):
        """Поиск индексов всех вхождений значения."""
        return super().find_all(value)
    
    def contains(self, value):
        """Проверка наличия значения в списке."""
        return super().contains(value)
    
    def get(self, index):
        """Получение значения элемента по индексу."""
        return super().get(index)
    
    def __len__(self):
        return super().__len__()
    
    def __str__(self):
        if (not self.head):
            return "None"
        else:
            stroke = ""
            current = self.head
            stroke += str(current.data) + " <-> "
            while(current.next):
                current = current.next
                stroke += str(current.data) + " <-> "
            stroke += "None"
            return stroke
    def __iter__(self):
        return super().__iter__()
    
    def clear(self):
        """Очистка списка."""
        return super().clear()
    
    def __getitem__(self, index):
        return self.get(index)
    
    def __setitem__(self, index, value):
        if (index < 0 or index >= self.size):
            raise IndexError(index)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            current.data = value
    
    def __contains__(self, value):
        return self.contains(value)
    
    def __add__(self, other):
        new_arr = DoublyLinkedList()

        for item in self:
            new_arr.append(item)

        for item in other:
            new_arr.append(item)
        return new_arr
    
    def __mul__(self, count):
        new_arr = DoublyLinkedList()

        for _ in range(count):
            for item in self:
                new_arr.append(item)
        return new_arr
    
class Stack:
    """Стек на основе односвязного списка (композиция)."""

    def __init__(self):
        self.items = SinglyLinkedList()

    def push(self, data):
        """Добавить элемент на вершину стека."""
        self.items.prepend(data)

    def pop(self):
        """Удалить и вернуть элемент с вершины стека."""
        try:
            return self.items.remove_first()
        except EmptyStructureError:
            raise EmptyStructureError("Stack")

    def peek(self):
        """Посмотреть элемент на вершине без удаления."""
        if self.is_empty():
            raise EmptyStructureError("Stack")
        else:
            return self.items.get(0)
    
    def is_empty(self):
        """Проверка, пуст ли стек."""
        if (self.items.size == 0):
            return True
        else:
            return False

    def size(self):
        """Количество элементов."""
        return self.items.size

    @staticmethod
    def from_queue(queue):
        """Статический метод. Переносит элементы из очереди в новый стек."""
        new_stack = Stack()
        while (not queue.is_empty()):
            new_stack.push(queue.dequeue())
        return new_stack

class Queue:
    """Очередь на основе односвязного списка (композиция)."""

    def __init__(self):
        self.items = SinglyLinkedList()

    def enqueue(self, data):
        """Добавить элемент в конец очереди."""
        self.items.append(data)

    def dequeue(self):
        """Удалить и вернуть элемент из начала очереди."""
        try:
            return self.items.remove_first()
        except EmptyStructureError:
            raise EmptyStructureError("Queue")

    def front(self):
        """Посмотреть первый элемент без удаления."""
        if self.is_empty():
            raise EmptyStructureError("Queue")
        return self.items.get(0)


    def is_empty(self):
        """Проверка, пуста ли очередь."""
        if (self.items.size == 0):
            return True
        else:
            return False

    def size(self):
        """Количество элементов."""
        return self.items.size

    @staticmethod
    def from_stack(stack):
        """Статический метод. Переносит элементы из стека в новую очередь."""
        new_queue = Queue()
        while not stack.is_empty():
            new_queue.enqueue(stack.pop())
        return new_queue