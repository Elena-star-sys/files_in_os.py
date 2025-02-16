import os
import time


directory = (os.getcwd())
print(directory)

for root, dirs, files in os.walk(directory):

   for file in files:
        filepath = os.path.join(directory)
        print(filepath)

        filetime = os.path.getmtime(directory)

        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        filesize = os.path.getsize(directory)

        parent_dir = os.path.dirname(directory)

        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
              f' {formatted_time}, Родительская директория: {parent_dir}')