#EX1
from operator import index

my_list = [0,23,-43,86,965,-73,245]
sum_my_list = sum(my_list)
print(sum_my_list)


#EX2
my_list1 = [1,2,3,3,4,5,5,6,7,8,8,9,0]
print(list(set(my_list1)))

uniq_list1 = []
for num in my_list1:
    if num not in uniq_list1:
        uniq_list1.append(num)
print(uniq_list1)


#EX3
my_tuple = (0,1,4,5,6,7,8,9)
my_tuple_index5 = my_tuple.index(5)
print("Tuple index 5 :",my_tuple_index5)


#EX4
my_set1 = {0,1,2,3,4,5,6,7}
my_set2 = {1,3,4,5,7,8,9}
inter_set = my_set1.intersection(my_set2)
print(inter_set)
inter_set1 = my_set1 & my_set2
print(inter_set1)


#EX5
my_dict = {
    "Ivan" : 98,
    "Andrey" : 76,
    "Inna": 88,
    "Donald" : 72,
    "Alina" : 93
}
my_dict ["Anton"] = 80
print(my_dict)



#EX6
my_list1 = [1,2,3,3,4,5,5,6,7,8,8,9,0]
rev_my_list1 = my_list1[::-1]
print(rev_my_list1)

reversed_my_list1 = list(reversed(my_list1))
print(reversed_my_list1)

my_list1.reverse()
print(my_list1)

reverse_my_list1 = []
for num in reversed(my_list1):
   reverse_my_list1.append(num)
print(reverse_my_list1)


#EX7
my_list2 = [1,2,3,4,5]
my_list3 = ['a','b','c','d','e']

comb_list =[]

for i_2 in my_list2:
    for i_3 in my_list3:
        comb_list.append((i_2,i_3))
print(comb_list)


from itertools import product
comb_list2 = list(product(my_list2,my_list3))
print(comb_list2)


#EX8
my_set3 = {53,35,35,7,45,89,3,52,789,3,534,-3,4}
my_set3.remove(3)
my_set3.discard(777)
print(my_set3)


#EX9
my_dict1 = {
    "laptop HP EliteBook" : 10000,
    "Laptop acer Aspire 5" : 12000,
    "Iphone 15" : 30000,
    "TV samsung 51" : 15000,
    "XBox X1" : 12000,
    "Headsets Airpods" : 8000
}
sort_my_dict = dict(sorted(my_dict1.items(), key=lambda  item: item[1]))
print(sort_my_dict)

sortrevers_my_dict = dict(sorted(my_dict1.items(), key=lambda  item: item[1], reverse=True))
print(sortrevers_my_dict)

def get_price(item):
    return item[1]
sortdef_my_dict = dict(sorted(my_dict1.items(), key=get_price ))
print(sortdef_my_dict)



#EX10
my_list_1 = [1,3,4,5,6,7,0]
my_list_2 = [2,3,5,7,8,9]
union_list = my_list_1 + my_list_2
print(union_list)

my_list_1.extend(my_list_2)
print(my_list_1)

my_tuple_1 = (1,2,3,4,5,6)
union1_list = [*my_list_2,*my_tuple_1]
print(union1_list)

import itertools

union_list33 = list(itertools.chain(my_list_2,my_tuple_1))
print(union_list33)


#EX11
mixed_list = [1,3.14,"World",True,54,False,0,"HP",7.62,-4,True,"python"]
str_list = []
int_list = []
float_list = []
bool_list = []


for i in mixed_list:
    if isinstance(i,str):
        str_list.append(i)
    elif isinstance(i,int) and not isinstance(i,bool):
        int_list.append(i)
    elif isinstance(i,float):
        float_list.append(i)
    elif isinstance(i,bool):
        bool_list.append(i)

print(str_list)
print(int_list)
print(float_list)
print(bool_list)


typy_dict = {
    "int" : [],
    "float" : [],
    "str" : [],
    "bool" : []
}

for i in mixed_list:
    if isinstance(i,str):
        typy_dict["str"].append(i)
    elif isinstance(i,int) and not isinstance(i,bool):
        typy_dict["int"].append(i)
    elif isinstance(i,float):
        typy_dict["float"].append(i)
    elif isinstance(i,bool):
        typy_dict["bool"].append(i)

print(typy_dict)
