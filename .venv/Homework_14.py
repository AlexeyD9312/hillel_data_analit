#EX1

def sort_prod_list(*args:str) -> str:
    sort_arg = sorted(*args, key= len, reverse= True)
    return sort_arg


prod_list = ["laptop","glases",'book',"car","bread"]

print(sort_prod_list(prod_list))


def rec_sort_prodlist(f_list) :
    if len(f_list) <= 1 :
        return f_list
    max_list = max( f_list , key= len)
    f_list.remove(max_list)
    return  [max_list] + rec_sort_prodlist(f_list)


sort2_prod_list = rec_sort_prodlist(prod_list)
print(sort2_prod_list)


def zam_len_prod():
    def pr_funk(products):
        return sorted(products, key= len)
    return pr_funk

prod_list3 = ["laptop","glases",'book',"car","bread"]
new_zam_len = zam_len_prod()
print(new_zam_len(prod_list3))


def gen_len_prod(funk):
    def inner_f(product):
        return sorted(product, key= len)
    return inner_f

@gen_len_prod
def simp_f(prod):
    return prod

print(simp_f(prod_list3))

#EX2
def leg_positiv_number(num_list):
    positiv_numb = [i for i in num_list if i > 0]
    return positiv_numb

nu_list = [1,2,-4,0,3,4,-4]
print(leg_positiv_number(nu_list))


def positive_numbers(number_list):
    if not number_list:
        return []
    if number_list[0] > 0:
        return [number_list[0]] + positive_numbers(number_list[1:])
    return positive_numbers(number_list[1:])

pos_num_list = positive_numbers(nu_list)
print(pos_num_list)


def lam_positive_numb(numb):
    return list(filter(lambda n: n>0, numb))

print(lam_positive_numb(nu_list))


def zam_posit_numb():
    def inside_f(nmbers):
        return [n for n in nmbers if n > 0]
    return inside_f

new_pos_num = zam_posit_numb()
print(new_pos_num(nu_list))


def dek_pos_num(func):
    def wraper(numbers):
        return [num for num in numbers if num > 0]
    return wraper


@dek_pos_num
def simp_funk(numbers):
    return numbers

print(simp_funk(nu_list))

#EX3
def upper_name(names):
    return list(map(lambda n: n.upper() , names))

name_list = ['Ira','Mari','vova','aNton']
print(upper_name(name_list))





def rec_upper_name(names):
    if not names:
        return names
    first_name = names[0]
    names.remove(first_name)
    return [first_name.upper()] + rec_upper_name(names)

print(rec_upper_name(name_list))

def dec_upper_name(funk):
    def wrapper(names):
        return [name.upper() for name in funk(names)]
    return wrapper

@dec_upper_name
def procces_name(names):
    return names

name_list3  = ["arkadiy","iNoKentiy","Frosya"]
print(procces_name(name_list3))


def zam_upper_name():
    def upper_funk(names):
        return [name.upper() for name in names]
    return  upper_funk

new_upfunck = zam_upper_name()
print(new_upfunck(name_list3))



#EX4
name_list2 = ['Ira','Ashot','Bogdan','Denis']

def check_lam(name_list):
     check_name = list(map(lambda name: "a"  in name.lower() , name_list))
     return list(check_name)

print(check_lam(name_list2))

def check_a(name_list,latter):
    if not name_list:
        return name_list
    return [latter in name_list[0]] + check_a(name_list[1:], latter)


print(check_a(name_list2,"a"))


def checa_azam(later):
    def chek_a(names):
        return [later in name for name in names]
    return chek_a

first_funk = checa_azam('a')
sec_funk = first_funk(name_list2)
print(sec_funk)


def dec_check_a(func):
    def wrap(names,later):
        return [func(name, later) for name in names]
    return wrap

@dec_check_a
def has_letter(name,later):
    return later in name

result = has_letter(name_list2,"a")
print(result)





