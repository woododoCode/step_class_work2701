from pprint import pprint
import sys

import json

countries = {
    'Гватемала': 'Гватемала',
    'Куба': 'Гавана',
    'Аргентина': 'Буенос-Айрес',
    'Бельгія': 'Брюссель',
}


def save_storage_to_file(**kwargs):
    file_name = kwargs.get('file_name')
    storage = kwargs.get('storage')
    if file_name and storage:
        with open(file_name, 'a', encoding='utf-8') as fw:
            fw.write(json.dumps(storage, ensure_ascii=False, indent=2))
        return 'Storage written successfully'
    else:
        return f'There is no argument {"file_name" if not kwargs.get("file_name") else None} ' \
               f'{"storage" if not kwargs.get("storage") else None}'


def read_data_from_storage(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as fr:
            data = fr.read()
            return json.loads(data)
    except FileNotFoundError as e:
        print(e)
        sys.exit(0)
        return e
    except OSError as va:
        print(va)
        return va
    finally:
        print('Good buy!')


# print(save_storage_to_file(file_name='test.json', storage=countries))
storage: dict = read_data_from_storage('asd')
storage = {'Украина': 'Киев'}
# storage.pop('Гватемала')
print(storage)
# save_storage_to_file(file_name='test.json', storage=storage)
