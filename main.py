# Напишите функцию, которая сереализует содержимое текущей директории в json-файл. В файле должен храниться список
# словарей, словарь описывает элемент внутри директории: имя, расширение, тип. Если элемент - директория,
# то только тип и имя. Пример результата для папки, где лежит файл test.txt и директория directory_test:

import json
import pathlib
import os


def current_directory_info():
    """Функция сереализует содержимое текущей директории в json-файл."""

    _directory_info = []
    _abs_path = os.getcwd()

    if pathlib.Path(_abs_path).suffix == '':
        name = pathlib.Path(_abs_path).name
        # print("File Extension:", name, "; Type:", type_object)
        _directory_info.append({
            'name': name,
            'type': 'directory'
        })
    else:
        name = pathlib.Path(_abs_path).name
        file_extension = pathlib.Path(_abs_path).suffix
        # print("File name:", name, "; Type:", type_object, "; File Extension:", file_extension)
        _directory_info.append({
            'name': name,
            'extention': file_extension,
            'type': 'file'
        })
    with open('current_directory_info.json', 'w') as i:
        json.dump(_directory_info, i, indent=2)


if __name__ == '__main__':
    current_directory_info()
