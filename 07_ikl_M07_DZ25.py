import os
import time

directory = r'proekt_DZ25'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(root, file) # полный путь к файлу
        filetime = os.path.getmtime(filepath) # время создания файла
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # перевожу в формат ДД.ММ.ГГГГ
        filesize = os.path.getsize(filepath) # определяю размер файла
        parent_dir = os.path.dirname(filepath) # определяю в какой папке находится файл
        print(f'\n {'*' * 30}')
        print(f'Обнаружен файл: {file} \nПуть: {filepath} \nРазмер: {filesize} '
              f'байт. Время изменения: {formatted_time} \nРодительская директория: {parent_dir}')
        print(f'\n {'*' * 30}')


