from structures import (
    SinglyLinkedList, 
    DoublyLinkedList, 
    Stack, 
    Queue, 
    EmptyStructureError, 
    IndexError, 
    ValueNotFoundError
)

def main():
    print("=" * 50)
    print("ЧАСТЬ 1: Демонстрация работы односвязного списка")
    print("=" * 50)
    lst = SinglyLinkedList()
    print(f"Создаем список: []")
    
    lst.prepend(1)
    print(f"Добавляем в начало (prepend 1): {lst}")
    lst.append(2)
    print(f"Добавляем в конец (append 2): {lst}")
    lst.insert_after(0, 3)
    print(f"Вставляем после индекса 0 (значение 3): {lst}")
    lst.insert_before(1, 4)
    print(f"Вставляем перед индексом 1 (значение 4): {lst}")
    lst.append(1)
    print(f"Добавляем еще 1 в конец: {lst}")

    print("\n--- Поиск элементов ---")
    print(f"Индекс первого значения 2 (find): {lst.find(2)}")
    print(f"Все индексы значения 1 (find_all): {lst.find_all(1)}")
    print(f"Проверка наличия 5 (contains / in): {5 in lst}")
    print(f"Получение элемента по индексу 2 (get / []): {lst[2]}")

    print("\n--- Удаление элементов ---")
    print(f"Удаление первого ({lst.remove_first()}): {lst}")
    print(f"Удаление последнего ({lst.remove_last()}): {lst}")
    print(f"Удаление элемента с индекса 1 ({lst.remove_at(1)}): {lst}")
    print(f"Удаление значения 4 ({lst.remove_value(4)}): {lst}")

    print("\n" + "=" * 50)
    print("ЧАСТЬ 2: Демонстрация работы перегруженных операторов")
    print("=" * 50)
    lst1 = SinglyLinkedList()
    lst1.append(1); lst1.append(2)
    lst2 = SinglyLinkedList()
    lst2.append(3); lst2.append(4)
    
    print(f"Список 1: {lst1}")
    print(f"Список 2: {lst2}")
    
    lst3 = lst1 + lst2
    print(f"Конкатенация (Список 1 + Список 2): {lst3}")
    
    lst4 = lst1 * 3
    print(f"Повторение (Список 1 * 3): {lst4}")
    
    lst3[0] = 10
    print(f"Изменение по индексу (lst3[0] = 10): {lst3}")

    print("\n" + "=" * 50)
    print("ЧАСТЬ 3: Двусвязный список")
    print("=" * 50)
    dlst = DoublyLinkedList()
    dlst.append("A")
    dlst.append("B")
    dlst.prepend("Start")
    dlst.insert_after(1, "A.5")
    print(f"Двусвязный список после добавлений: {dlst}")
    dlst.remove_last()
    print(f"Удалили с конца: {dlst}")

    print("\n" + "=" * 50)
    print("ЧАСТЬ 4: Демонстрация работы стека")
    print("=" * 50)
    stack = Stack()
    stack.push(5)
    stack.push(10)
    stack.push(15)
    print(f"Добавили 5, 10, 15. Текущий размер стека: {stack.size()}")
    print(f"Верхний элемент (peek): {stack.peek()}")
    print(f"Удалили (pop): {stack.pop()}")
    print(f"Верхний элемент после удаления: {stack.peek()}")

    print("\n" + "=" * 50)
    print("ЧАСТЬ 5: Демонстрация работы очереди")
    print("=" * 50)
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Очередь (добавили 1, 2, 3). Текущий размер: {queue.size()}")
    print(f"Первый элемент (front): {queue.front()}")
    print(f"Извлекли (dequeue): {queue.dequeue()}")
    print(f"Первый элемент после извлечения: {queue.front()}")

    print("\n" + "=" * 50)
    print("ЧАСТЬ 6: Демонстрация преобразования")
    print("=" * 50)
    q_to_convert = Queue()
    q_to_convert.enqueue(10); q_to_convert.enqueue(20); q_to_convert.enqueue(30)
    print(f"Исходная очередь: размер {q_to_convert.size()}")
    
    new_stack = Stack.from_queue(q_to_convert)
    print(f"Создан стек из очереди. Извлекаем из стека:")
    while not new_stack.is_empty():
        print(new_stack.pop(), end=" ")
    print()
    
    s_to_convert = Stack()
    s_to_convert.push(100); s_to_convert.push(200); s_to_convert.push(300)
    new_queue = Queue.from_stack(s_to_convert)
    print(f"Создана очередь из стека. Извлекаем из очереди:")
    while not new_queue.is_empty():
        print(new_queue.dequeue(), end=" ")
    print()

    print("\n" + "=" * 50)
    print("ЧАСТЬ 7: Обработка исключений")
    print("=" * 50)
    
    try:
        print("Попытка получить элемент из пустого списка...")
        empty = SinglyLinkedList()
        item = empty[0]
    except IndexError as e:
        print(f"-> Ошибка перехвачена: {e}")

    try:
        print("\nПопытка удалить из пустой очереди...")
        empty_q = Queue()
        empty_q.dequeue()
    except EmptyStructureError as e:
        print(f"-> Ошибка перехвачена: {e}")

    try:
        print("\nПопытка найти несуществующее значение для удаления...")
        lst = SinglyLinkedList()
        lst.append(1)
        lst.remove_value(99)
    except ValueNotFoundError as e:
        print(f"-> Ошибка перехвачена: {e}")

    print("\nВсе тесты успешно завершены!")

if __name__ == "__main__":
    main()