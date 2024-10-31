def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = 0
    strings_number = 0
    #slovar = {}
    for i in strings:
        strings_number += 1
        file.write(i+'\n')
        a = (strings_number, strings_positions, i)
        print(a)
        strings_positions = file.tell()
    file.close()
    #return slovar

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
# for elem in result.items():
#   print(elem)