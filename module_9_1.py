def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        if func == max:
            results.update({func.__name__: max(int_list)})
        if func == min:
            results.update({func.__name__: min(int_list)})
        if func == len:
            results.update({func.__name__: len(int_list)})
        if func == sum:
            results.update({func.__name__: sum(int_list)})
        if func == sorted:
            results.update({func.__name__: sorted(int_list)})
    return results


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
