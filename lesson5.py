immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
mutable_list = [1, 2, 'a', 'b']
mutable_list.extend('c')
print(mutable_list)
mutable_list.remove(2)
print(mutable_list)
mutable_list.append('Modified')
print(mutable_list)