from itertools import count

import pandas as pd
from Homework_14 import nu_list

#EX5

product_list = [
    {"name" : "TV", "quant": 1 , "price" : 5000},
    {"name" : "laptop", "quant": 2 , "price" : 7000},
    {"name" : "phone", "quant": 3 , "price" : 4000}
]

print(*product_list)
names = [n["name"] for n in product_list]
values = product_list[0].values()
print(list(values))


def recurs_total_sum(rand_list):
    if not rand_list:
        return 0
    return rand_list[0]["quant"] * rand_list[0]["price"] + recurs_total_sum(rand_list[1:])

print(recurs_total_sum(product_list))


def decor_total_funk(funk):
    def wraper(rand_list):
        return sum(x["quant"] * x["price"] for x in rand_list)
    return wraper

@decor_total_funk
def sum_total(listic):
    return listic

print(sum_total(product_list))

def zam_total_funk():
    def wraper(rand_list):
        return sum(x["quant"] * x["price"] for x in rand_list)
    return wraper

new_zam_total = zam_total_funk()
print(new_zam_total(product_list))

df = pd.DataFrame(product_list)
print(df)
df["total"] = df["quant"] * df["price"]
print(df)
total_price_sum = sum(df["total"])
print(total_price_sum)


#EX6
text = "Hello this is simple text"



def quant_wor(a:str)->str:
    return len(a.split())

print(quant_wor("Hello , this is  : simple   text"))

import re

text = "Hello this is simple text"


def decor_total_w(func):
    def wrapp(text):
        if isinstance(text,str):
            only_words = re.findall(r'\b\w+\b', text)
        else:
            only_words = text
        return func(only_words)
    return wrapp


@decor_total_w
def count_words(words):
    if not words:
        return 0
    return 1 + count_words(words[1:])

text3 = "Hello , this is  : simple   text"
wor_co = count_words(text3)
print(f'{wor_co}')


#EX8
def dec_mid_numb(func):
    def wrapper(some_list):
        return sum(some_list)/len(some_list)
    return wrapper

@dec_mid_numb
def funck_mid_num(num_list):
    return num_list

nu_lists = [1,2,3,4,5,6,-8]
print(funck_mid_num(nu_lists))


def dec_mid_numb():
    def wrapper(some_list):
        return sum(some_list)/len(some_list)
    return wrapper

new_dec_mid = dec_mid_numb()
print(new_dec_mid(nu_lists))


def rec_midl_num(lists):
    if len(lists) <= 1:
        return lists








