# vname = 'lade'
# age = str(28)

# print(type(vname))

# result = vname + ' ' 'is' ' ' + age


# print(result)

# print('my name is oyindolapo')


# num = 2
# numm = 44

# print(num*numm)

# a = 4
# b = 7
# c = 3

# numerator = -b + ((b**2) - (4*a*c)) 

# denominator = 2*a

# x = numerator/denominator
# print(x)


# if a man is two times the age of his son, how hold will the man be in few years

# name = 'oyindolapo'
# age = str(26)
# status = 'new patient'

# print('Your patiet name is ' + name + ' and he or she is ' + age + 'years old', ' he is a ' + status)

# names = input('please enter your name ')
# age = input('please enter in your age ')
# gender = input('enter in your gender ')

# person_info = ('your name is '+ names + ' you are ' + age + ' and your gender is ' + gender)

# print(person_info)

# name_info = input('enter your name ')
# birth_year = int(input('enter in birth year '))

# current_year = 2022 - birth_year

# print(current_year)

# result = ('ýour name is ' + name_info + 'and you are ' + current_year)

# print(result)

# print(type(current_year))

# weight_lbs = float(input('Weight (lbs): '))
# weight_kg = weight_lbs * 0.45

# print(weight_kg)

# word = 'bamijoko oyindolapo'

# print(word[1:4])

# these above print function access the value thing the index of the starting range down to its endrange

# print(word[0:])

# this index remove the from the biggining

# print(word[:4])

# this above basically remove from its ends


# the next topic is formatted string

# year_birth = int(input('enter year of birth: '))

# present_year = 2022 - year_birth

# result = f'Your birth year is {year_birth} so your present age should be {present_year}'

# print(result)

# color = ['red', 'green', 'blue', 'orange', 'yellow', 'white', 'purple', 'brown', 'grey']

# print('red' in color)

# color.insert(2, 'pink')

# print(color)

# print(len(color))

# the above show the length of the value in a variable

# color.append('black')
# print(color)

# this above code basically add an item to a list or any value

# color.remove('blue')
# print(color)

# this above remove a value

# items = 'love'

# sent = 'what do you know about me'

# print(sent.replace('me', 'our'))

# x = 2.7

# print(abs(-2.5))

# abs always return a positive number

# import math

# print(math.ceil(2.3))

# house_price = 1000000

# has_goodcredit = True

# if has_goodcredit:
#     dpayment = 0.1 * house_price

# else:
#     dpayment = 0.2 * house_price

# print(f'your downpaymen will be {dpayment}')


# logical operator

# has_high_income = True
# has_good_credit = False


# if has_good_credit and has_high_income:
#     print('you are legible for loan')

# elif has_good_credit or has_high_income:
#     print('you need to have both both income as TRUE')

# else:
#     ('your command is not understood')


# legible_score = 65

# income = float(input('enter in your income range: '))
# credit = float(input('enter in your credit score: '))

# if income >= legible_score and credit >= legible_score:
#     print(f'congratulation your income is {income} and your credit score is {credit} "YOU ARE LEGIBLE FOR A LOAN"')

# elif income < legible_score and credit < legible_score:
#     print('sorry your income and your credit score is less than the accredited range "you are not legible for LOAN" ')

# elif income > legible_score or credit > legible_score:
#     print(f'either your income or your credit is low ')

# else:
#     print('you operation is not accurate') 


# full_name = input('enter your name: ')

# nam_len = len(full_name)

# if nam_len < 3:
#     print('name must be at least 3 characters')

# elif nam_len >= 50:
#     print('name must be a maximum of 50 characters')

# else:
#     print('name looks good !!')

# weight converter

# weight = float(input('Weight: '))

# lbs_kg = str(input('lbs or kg: '))

# kg_converter = 2.2
# lbs_coverter = 0.45

# if lbs_kg == 'l':
#     result = weight * lbs_coverter
#     print(f'you are {result}Kg')

# elif lbs_kg == 'k':
#     show = weight / kg_converter
#     print(f'you are {show} pounds')

# seconds = 60

# secondss = 42



# minute = seconds * 42

# print(minute + 42)

# print(type(seconds))


# nums = '50'

# num = 50

# print(int(nums) + num)


# question 3

# book = 24.95

# book_store_discount = 11.98

# result_bookdiscount = book - book_store_discount

# print(result_bookdiscount)


# shipping_cos = 3

# addd = result_bookdiscount - shipping_cos

# print(addd)


# book_store = 40


# add_cost = 75

# what is the whole sale cost of 60 copies

# user_name = input('enter your first name: ')
# user_suname = input('enter lastname: ')

# user_name[:-4]
# user_suname[:-3]

# print(f'{user_name[0:4]}{user_suname[:-4]}')

# combination = (f'{user_name} {user_suname}')

# print(combination)

# user_name[:]


# human = 'temilade'

# print(human[1:-3])


# case = 'oyindolapo'

# new_name = case.replace('oyindolapo', 'kemi')

# print(new_name)

# numss = ('o' in case)

# print(type(numss))


# print(case)

# print(case.upper())

# number_ff = 40

# number_new = 40

# user = 'damilare'

# print('your name is '+ str(user) + ' your sum number is ' + str(number_ff + number_new))

# print(result)


# while loops in python


# i = 1

# while i <= 5:
#     print(i)
#     i = i + 1

# print('done')

# guessing game

# secret_number = 9

# guess = 0

# guess_limit = 3

# while guess < guess_limit:
#     user_input = int(input('enter secret number: '))
#     if secret_number == user_input:
#         print('you won !!')

#     elif user_input != secret_number:
#         print('you fail')

#     elif guess > guess_limit:
#         print('you are out of chance')


# second = 60
# munites = 42

# res = second * munites + 42

# print(res)


# one_mile = 1.61

# ten_kilometer = 10

# let = one_mile * ten_kilometer

# print(let)



# run_kilo = 42
# run_second = 42

# seconds = 60

# bobby = run_kilo * 60

# print(bobby + 42)

# div = bobby / 60

# print(div)


# for x in a:
#     print(x)
# access = a.index(sub)


# user_name = input('enter your name: ')
# user_gender = input('Enter Your Gender: ')
# user_age = int(input('Enter Your Age: '))

# if user_gender == 'male' and user_age >= 18:
#     print(f'Hello {user_name} your gender is {user_gender} and you are {user_age} yearold and you are legible to drive')

# elif user_gender == 'male' and user_age < 18:
#     print(f'Hello {user_name} you gender is {user_gender} and you are {user_age} yearold and you are not legible to drive')

# elif user_gender == 'female' and user_age < 20:
#     print(f'Hello {user_name} your gender is {user_gender} and you are {user_age}yearsold and you are not legible to drive')

# elif user_gender == 'female' and user_age > 19:
#     print(f'Hello {user_name} your gender is {user_gender} and you are {user_age}yearsold and you are legible to drive')

# else:
#     print(f'hello {user_name} i dont understand')


# love = 'my baby'

# print('b' in love)


# numeric = float(input('enter any number: '))

# conversion = numeric

# print(type(conversion))

# print(f'your number is {numeric}')


# strings = 'this is oyindolapo he is crazy'

# cap = strings.find('is')
# print(f'is was found {cap} times')

# print(strings.upper())

# print(strings.upper()

# print(strings.find('is'))



# strings = 'this is a string'

# conv = strings.replace(' ', '-')

# print(conv)


# nac = 'this, is a rabbit'

# pap = 'God'

# print(nac.split(','))


# lists = ['oyindolapo', 'is', 'a', 'boy']

# print(lists)


# print(lists.joins)


# functions

def add_number(a:int, b:int):
    # print(a+b)

    """this is a doc string and it also add number
    (a) is a int
    (b) is also a int


    """
    return a+b

b = add_number(10, 10)
print(b)


# def simple_intrest(number, time, place):
#     """
#     this function sums up the intrest of a given number

    


#     """
#     numbers = number * time * place

#     div = numbers / 100



#     return div

# result = simple_intrest(20, 2, 3)
# print(result)

