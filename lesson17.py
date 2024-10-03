def calculate_structure_sum(data_structure):
    global calc_all
    for i in data_structure:
        if isinstance(i, str):
            calc_all += len(i)
        elif isinstance(i, int):
            calc_all += i
        elif isinstance(i, dict):
            val_ = i.values()
            key_ = i.keys()
            calculate_structure_sum(val_)
            calculate_structure_sum(key_)
        else:
            calculate_structure_sum(i)
    return calc_all


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
calc_all = 0
result = calculate_structure_sum(data_structure)
print(result)
