#EXERSISE 1
#
for n in range(1,101):
    if n % 5 == 0:
        print(n, end=' ')
print()

#
n = 1
while n < 101:
    if n % 5 == 0:
      print(n, end=' ')
    n +=1
print()

#EXERSISE 2
for n in range(1,21):
    if n % 2 == 0:
        print(n, end=' ')
print()

#EXERSISE 3
user_number = input("Enter your number :")

try:
    int_number = int(user_number)
    if int_number %2 == 0:
       print(f"{int_number} - even number")
    else :
       print(f"{int_number} - odd number")
except ValueError:
    print("incorrect data")

#EXERSISE 4
total_sum = sum(range(1,51))
print(total_sum)



#EXERSISE 5
for i in range(1,11):
    if i > 5:
        print(i,end =" ")
print()

#EXERSISE 6
number = float(input("Enter number :"))
if number > 10 :
    print(f"{number} > 10")
else:
    print(f"{number} < 10")


#EXERSISE 7
for i in range(1,11):
    print(i*3, end=" ")
print()

n = 3
i = 1
while i*n:
    if i == 11:
     break
    print(i*3, end=" ")
    i +=1

#EXERSISE 8
user_name = input("Whot is your name :")
user_name = user_name.capitalize()
print(f"Hello {user_name}")


#EXERSISE 9

for n in range(1,101):
    if n % 3 != 0 and n % 5 != 0:
        print(n, end=' ')
print()

n = 1
while n < 101 :
    if n % 3 != 0 and n % 5 != 0:
        print(n, end=' ')
    n +=1
print()


#EXERSISE 10
str_value = "Hello world and python"
str_value = str_value.replace(" ","")  #
print(str_value.isalpha())


#EXERSISE 11
n = 1
while n < 51 :
    if n % 7 == 0 :
        print(n, end=' ')
    n +=1
print()


#EXERSISE 12
ent_number = int(input("Enter your number :"))
if ent_number > 0:
    print(f"{ent_number} - positive number")
elif ent_number < 0 :
     print(f"{ent_number} - negative number")
else:
    print("Your number is 0")


#EXERSISE 13
user_number2 = int(input("Enter your number :"))
for i in range(1,11):
    print(i,"*",user_number2,"=",i*user_number2)


#EXERSISE 14
user_numbers = input(" by space :")
user_numbers_list = [float(num) for num in user_numbers.split(" ")]
print("sum enter numbers",sum(user_numbers_list))


#Enter number, to finish enter 'stop'
sum_numb = 0
while True:
    user_numb = input("Enter number : ")
    if user_numb == 'stop':
        break
    else:
        user_numb = float(user_numb)
        sum_numb += user_numb
        print("Sum your numbers = ",sum_numb)


#EXERSISE 15

us_number = int(input("Enter number :"))
if us_number > 1:

  for i in range(2,us_number):
    if us_number % i == 0:
        print(f'{us_number} - composite number')
        break
    elif us_number == 0:
        print(f'{us_number} - composite number')
  else:
        print(f'{us_number} - prime number')
else:
    print(f'{us_number} - composite number')
