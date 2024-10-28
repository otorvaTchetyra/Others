data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(data_structure):
    if isinstance(data_structure, list):
        return sum([calculate_structure_sum(item) for item in data_structure])
    elif isinstance(data_structure, tuple):
        return calculate_structure_sum(data_structure[0]) + calculate_structure_sum(data_structure[1:])
    elif isinstance(data_structure, dict):
        return sum({key: calculate_structure_sum(value) for key, value in data_structure.items()})
    elif isinstance(data_structure, str):
        return int(data_structure) if data_structure.isdigit() else data_structure
    else:
        return data_structure

result = calculate_structure_sum(data_structure)
print(result)