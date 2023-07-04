from utils.utils import *

file = 'operations.json'

sorted_f = dict_oper(file)

k = sort(sorted_f)

for i in k:
    print(i['date'], i['description'])
    print(format_from_number(i['from']), '->', format_to_number(i['to']))
    print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
    print('')
