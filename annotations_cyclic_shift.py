def cyclic_shift(numbers: list[int | float], step: int) -> None:
    for _ in range(abs(step)):
        if step > 0:
            numbers.insert(0, numbers.pop())
        else:
            numbers.reverse()
            numbers.insert(0, numbers.pop())
            numbers.reverse()


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)

# Класс collections.deque() это обобщение стеков и очередей и представляет собой двустороннюю очередь.
# Двусторонняя очередь deque() поддерживает поточно-ориентированные, эффективные по памяти операции добавления и
# извлечения элементов последовательности с любой стороны с примерно одинаковой производительностью O(1) в любом
# направлении.
#
# Списки поддерживают аналогичные операции, но они оптимизированы только для быстрых операций с последовательностями
# фиксированной длины и требуют затрат O(n) на перемещение памяти для операций pop(0) и insert(0, v), которые изменяют
# как размер, так и положение базового представления данных.
# from collections import deque
#
# def cyclic_shift(numbers_: list[int | float], step: int) -> None:
#     global numbers
#     numbers = deque(numbers)
#     numbers.rotate(step)
#     numbers = list(numbers)
