immutable_var=(1,5.5,'Строка', ['c', 'п', 'и','с','о','к'], True)
print(immutable_var)
#immutable_var[1]=23 #выдаёт ошибку, так как кортеж нельзя изменять

mutable_list=[1,3.4,'Строка', False]
mutable_list[2]=10
print(mutable_list)


