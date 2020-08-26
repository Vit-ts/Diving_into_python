from collections import OrderedDict

import argparse
import tempfile
import os
import json
 
 
parser = argparse.ArgumentParser()
parser.add_argument('--key', help="dict key")
parser.add_argument('--val', help='dict value')
args = parser.parse_args()
if not os.path.exists('/tmp/storage.data'):
    f = open('/tmp/storage.data', 'tw', encoding='utf-8')
    f.close()
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
data = {}
if args.key and args.val:
    if os.stat(storage_path).st_size != 0:
        # Читаем словарь из файла
        with open(storage_path, 'r') as f:
            data = json.loads(str(f.read()))

    if args.key in data:
        data[args.key].append(args.val)
    else:
        data[args.key] = []
        data[args.key].append(args.val)


    # Сохраняем словарь в файл
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))

if os.stat(storage_path).st_size != 0:
    if args.key and not args.val:
        # Читаем словарь из файла
        with open(storage_path, 'r') as f:
            data_new = json.loads(str(f.read()))
        if args.key in data_new:
            data_print = {}
            data_print[args.key] = data_new[args.key]
            for key, value in data_print.items():
                print(', '.join(str(num) for num in value), sep='')
        else:
            print(None)
else:
    print(None)
        
        