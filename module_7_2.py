def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = 0
    strings_number = 0
    slovar = dict()
    for i in strings:
        strings_number += 1
        strings_positions = file.tell()
        slovar[(strings_number, strings_positions)]= i
        file.write(i+'\n')
    file.close()
    return slovar

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)