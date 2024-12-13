import numpy as np

print(np.empty(2)) #создает массив из рандомных чисел в указанном количестве (2)
print(np.arange(4)) #создает массив по порядку в указанном количестве (4), начиная с 0
print(np.arange(10,100,10)) #создает массив от числа а до числа b с шагом c
print(np.zeros(5)) #создает массив из 0
print(np.linspace(0, 100, num=5)) #создает массив отрезков из длины между а и b с интервалом с
arr = np.array ([5,6,2,9,7])
print(np.sort(arr)) #сортирует массив
print(arr.size) #длина массив
print(arr.dtype) #тип данных массива
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
print(np.concatenate((arr1,arr2))) #объединяет два массива в один

