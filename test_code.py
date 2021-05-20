from collections import deque


employee_list = ["Soumik", "Jamie", "Smith"]

employee_list_deque = deque(employee_list)

# O(1) time performance
employee_list_deque.appendleft("Sunehra")
print(list(employee_list_deque))