# foo = 0

# def f1():
#     global foo
#     foo = 1

# f1()
# print(foo)

# s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}
# s.symmetric_difference_update({3, 4, 5})
# s.difference_update({2, 3, 8})
# print(s)

# restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
# unique_restaurants = sorted(set(restaurants))
# print(unique_restaurants)

# s = {frozenset({1, 2}), frozenset({3, 4})}
# print(s)

# fs = frozenset({"apple", "banana", "cherry"})
# print(fs)

# a_s = set()
# b_s = frozenset({})
# c_s = {1, 2, 3, 3, 4, 5}
# e_s = {1, 2, 2, 6, 7, 4, 3}
# d_s = {8, 9, 10, 11, 12,}

# a_s.update(e_s)
# c_s.intersection()
# e_s.update(c_s.union(d_s))
# print(a_s, c_s, e_s)

# a = {1, 2, 2, 3, 4}
# b = {3, 3, 4, 4, 5}
# c = set()
# d = set()
# a.intersection_update(b)
# a.symmetric_difference_update(b)
# c.update(a)
# b.difference_update(c)
# d.update(c, b, a)
# a.issubset(d)
# print(len(a))

# def calculate_structure_sum(data_structure, result=0, max_depth=None):
#     if max_depth is None or max_depth > 0:
#         for item in data_structure:
#             if isinstance(item, int):
#                 result += item
#             elif isinstance(item, str):
#                 result += len(item)
#             elif isinstance(item, (list, tuple)):
#                 result += calculate_structure_sum(item, result, max_depth - 1)
#             elif isinstance(item, dict):
#                 result += sum(calculate_structure_sum(v, result, max_depth - 1) for v in item.values())
#     return result

# # Пример использования
# data_structure = [
#     [1, 2, 3],
#     {'a': 4, 'b': 5},
#     (6, {'cube': 7, 'drum': 8}),
#     "Hello",
#     ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]
# result = calculate_structure_sum(data_structure)
# print(result)




#  

# 

# data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]
# # print(len(data_structure))  узнаём количество элементов и тип данных каждого элемента с помощью 
# # for i in data_structure: 
# #   print(i, (type(i))) 

# # создаю тело функции calculate_structure_sum и добавляю к нему аргументы в виде переменных
# def calculate_structure_sum(data_structure, result = 0):
#     for i in data_structure:
#         if isinstance(i, int):
#             result += i
#         elif isinstance(i, dict):
#             result += i
#         elif isinstance(i, (list, tuple)):
#             result += i
#         elif isinstance(i, str):
#             result += i
#     return result

# result = calculate_structure_sum(data_structure) 
# print(result)



# узнаём количество элементов и тип данных каждого элемента
# print(len(data_structure)) 

# for i in data_structure: # print(i, (type(i))) узнаём тип каждого элемента 



#     if isinstance(i, list):
#         result += i
#     elif isinstance(i, dict):
#         result += i
#     elif isinstance(i, tuple):
#         result += i
#     elif isinstance(i, str):
#         result += i 
# print(*result)
# print(len(str(result)))

# print(len(str(data_structure)))

# print(dir(data_structure))
# print(help(data_structure)) 
# print(type(data_structure))






# for i in data_structure:
#     if data_structure == int:
#         print(int(data_structure))
#     else:
#         print(data_structure )



# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(5))

# print(len(data_structure[0]))

data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):
    if isinstance(data_structure, list):
        return [calculate_structure_sum(i) for i in data_structure]
    elif isinstance(data_structure, tuple):
        return calculate_structure_sum(data_structure[0:])
    elif isinstance(data_structure, dict):
        return {key: calculate_structure_sum(value) for key, value in data_structure.items()}
    elif isinstance(data_structure, str):
        return data_structure
    else:
        return data_structure

result = calculate_structure_sum(data_structure)
print(result)






