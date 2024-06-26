my_dict={'Inna': 48, 'Masha': 17}
print(my_dict)
print(my_dict['Inna'])
print(my_dict['Inna'], my_dict.get('Vasya', 'Таких нет'))
my_dict.update({'Peter': 15, 'Ivan': 48})
a=my_dict.pop('Masha')
print(a)
print(my_dict)


my_set={1,2,4,5,4,3,'слива', 'слива'}
print(my_set)
my_set.add('макарошки')
my_set.add(7)
print(my_set)
my_set.remove(3)
print(my_set)