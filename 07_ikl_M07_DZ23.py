file_01 = open('07_ikl_M07_dz23.txt')
print(file_01.read()) # вывожу на консоль содержимое файла
print(file_01.tell()) # проверяю, где корретка находится.
#file_01.seek(0) # перевод корретки на начало файла
#print(file_01.read()) # вновь вывожу на консоль содержимое файла. Внимание, корретка по умолчанию всегда в конце файла

file_01.close()
# print(file_01.read()) # проверил закрытие файла, действительно выдает ошибку ("операция над закрытым файлом")