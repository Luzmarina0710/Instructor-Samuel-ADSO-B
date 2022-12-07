list1 = [5,3,8,1,9,2]
print(list1)
list2 = [0,4,3,7,9,2]
print(list2)
print('los numeros repetidos son:')
for i in list1:
    for j in list2:
        if i == j:
            print(i,end=",")
