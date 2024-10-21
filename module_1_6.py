my_dict = {'Aleksandr': 1996, 'Vika;': 2003}
print("Dict:", my_dict)
my_dict.get('sasha', 'такого ключа нет')
existing_key = "Aleksandr"
print("Existing value:", my_dict.get(existing_key))
not_existing_key = "Sem"
print("Not existing value:", my_dict.get(not_existing_key))
my_dict.update({'Vasya': 1955 ,
                'Artem': 1976})
deleted_key = 'Vasya'
Deleted_value = my_dict.pop(deleted_key, None)
print("Deleted value:", Deleted_value)
print('Modified dictionary:' , my_dict)

my_set = {1, 'Авокадо' , 54.234, 1, 'Авокадо' , 2.34}
print("Set:", my_set)
my_set.add(77)
my_set.add((3, 8, 6.9))
my_set.remove(54.234)
print("Modified set:", my_set)
