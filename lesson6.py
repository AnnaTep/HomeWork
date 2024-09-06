# словари
my_dict = {'Anna': 1987, 'Tanya': 1988, 'Sanya': 1986}
print(my_dict)
print(my_dict.get('Anna'))
print(my_dict.get('Manya', 'Такого элемента нет'))
my_dict.update({'Danya': 1988, 'Vanya': 1989})
year = my_dict.pop('Anna')
print(year)
print(my_dict)
# множества
my_set = {1, 2, 1, 2, 1, 'cat', 4.2}
print(my_set)
my_set.add('dog')
my_set.add(56.8)
my_set.discard(2)
print(my_set)