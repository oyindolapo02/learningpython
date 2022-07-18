# # vname = 'lade'
# # age = str(28)

# # print(type(vname))

# # result = vname + ' ' 'is' ' ' + age


# # print(result)

# # print('my name is oyindolapo')


# # num = 2
# # numm = 44

# # print(num*numm)

# # a = 4
# # b = 7
# # c = 3

# # numerator = -b + ((b**2) - (4*a*c)) 

# # denominator = 2*a

# # x = numerator/denominator
# # print(x)


# # if a man is two times the age of his son, how hold will the man be in few years

# # name = 'oyindolapo'
# # age = str(26)
# # status = 'new patient'

# # print('Your patiet name is ' + name + ' and he or she is ' + age + 'years old', ' he is a ' + status)

# # names = input('please enter your name ')
# # age = input('please enter in your age ')
# # gender = input('enter in your gender ')

# # person_info = ('your name is '+ names + ' you are ' + age + ' and your gender is ' + gender)

# # print(person_info)

# # name_info = input('enter your name ')
# # birth_year = int(input('enter in birth year '))

# # current_year = 2022 - birth_year

# # print(current_year)

# # result = ('ýour name is ' + name_info + 'and you are ' + current_year)

# # print(result)

# # print(type(current_year))

# # weight_lbs = float(input('Weight (lbs): '))
# # weight_kg = weight_lbs * 0.45

# # print(weight_kg)

# # word = 'bamijoko oyindolapo'

# # print(word[1:4])

# # these above print function access the value thing the index of the starting range down to its endrange

# # print(word[0:])

# # this index remove the from the biggining

# # print(word[:4])

# # this above basically remove from its ends


# # the next topic is formatted string

# # year_birth = int(input('enter year of birth: '))

# # present_year = 2022 - year_birth

# # result = f'Your birth year is {year_birth} so your present age should be {present_year}'

# # print(result)

# # color = ['red', 'green', 'blue', 'orange', 'yellow', 'white', 'purple', 'brown', 'grey']

# # print('red' in color)

# # color.insert(2, 'pink')

# # print(color)

# # print(len(color))

# # the above show the length of the value in a variable

# # color.append('black')
# # print(color)

# # this above code basically add an item to a list or any value

# # color.remove('blue')
# # print(color)

# # this above remove a value

# # items = 'love'

# # sent = 'what do you know about me'

# # print(sent.replace('me', 'our'))

# # x = 2.7

# # print(abs(-2.5))

# # abs always return a positive number

# # import math

# # print(math.ceil(2.3))

# # house_price = 1000000

# # has_goodcredit = True

# # if has_goodcredit:
# #     dpayment = 0.1 * house_price

# # else:
# #     dpayment = 0.2 * house_price

# # print(f'your downpaymen will be {dpayment}')


# # logical operator

# # has_high_income = True
# # has_good_credit = False


# # if has_good_credit and has_high_income:
# #     print('you are legible for loan')

# # elif has_good_credit or has_high_income:
# #     print('you need to have both both income as TRUE')

# # else:
# #     ('your command is not understood')


# # legible_score = 65

# # income = float(input('enter in your income range: '))
# # credit = float(input('enter in your credit score: '))

# # if income >= legible_score and credit >= legible_score:
# #     print(f'congratulation your income is {income} and your credit score is {credit} "YOU ARE LEGIBLE FOR A LOAN"')

# # elif income < legible_score and credit < legible_score:
# #     print('sorry your income and your credit score is less than the accredited range "you are not legible for LOAN" ')

# # elif income > legible_score or credit > legible_score:
# #     print(f'either your income or your credit is low ')

# # else:
# #     print('you operation is not accurate') 


# # full_name = input('enter your name: ')

# # nam_len = len(full_name)

# # if nam_len < 3:
# #     print('name must be at least 3 characters')

# # elif nam_len >= 50:
# #     print('name must be a maximum of 50 characters')

# # else:
# #     print('name looks good !!')

# # weight converter

# # weight = float(input('Weight: '))

# # lbs_kg = str(input('lbs or kg: '))

# # kg_converter = 2.2
# # lbs_coverter = 0.45

# # if lbs_kg == 'l':
# #     result = weight * lbs_coverter
# #     print(f'you are {result}Kg')

# # elif lbs_kg == 'k':
# #     show = weight / kg_converter
# #     print(f'you are {show} pounds')

# # seconds = 60

# # secondss = 42



# # minute = seconds * 42

# # print(minute + 42)

# # print(type(seconds))


# # nums = '50'

# # num = 50

# # print(int(nums) + num)


# # question 3

# # book = 24.95

# # book_store_discount = 11.98

# # result_bookdiscount = book - book_store_discount

# # print(result_bookdiscount)


# # shipping_cos = 3

# # addd = result_bookdiscount - shipping_cos

# # print(addd)


# # book_store = 40


# # add_cost = 75

# # what is the whole sale cost of 60 copies

# # user_name = input('enter your first name: ')
# # user_suname = input('enter lastname: ')

# # user_name[:-4]
# # user_suname[:-3]

# # print(f'{user_name[0:4]}{user_suname[:-4]}')

# # combination = (f'{user_name} {user_suname}')

# # print(combination)

# # user_name[:]


# # human = 'temilade'

# # print(human[1:-3])


# # case = 'oyindolapo'

# # new_name = case.replace('oyindolapo', 'kemi')

# # print(new_name)

# # numss = ('o' in case)

# # print(type(numss))


# # print(case)

# # print(case.upper())

# # number_ff = 40

# # number_new = 40

# # user = 'damilare'

# # print('your name is '+ str(user) + ' your sum number is ' + str(number_ff + number_new))

# # print(result)


# # while loops in python


# # i = 1

# # while i <= 5:
# #     print(i)
# #     i = i + 1

# # print('done')

# # guessing game

# # secret_number = 9

# # guess = 0

# # guess_limit = 3

# # while guess < guess_limit:
# #     user_input = int(input('enter secret number: '))
# #     if secret_number == user_input:
# #         print('you won !!')

# #     elif user_input != secret_number:
# #         print('you fail')

# #     elif guess > guess_limit:
# #         print('you are out of chance')


# # second = 60
# # munites = 42

# # res = second * munites + 42

# # print(res)


# # one_mile = 1.61

# # ten_kilometer = 10

# # let = one_mile * ten_kilometer

# # print(let)



# # run_kilo = 42
# # run_second = 42

# # seconds = 60

# # bobby = run_kilo * 60

# # print(bobby + 42)

# # div = bobby / 60

# # print(div)


# # for x in a:
# #     print(x)
# # access = a.index(sub)


# # user_name = input('enter your name: ')
# # user_gender = input('Enter Your Gender: ')
# # user_age = int(input('Enter Your Age: '))

# # if user_gender == 'male' and user_age >= 18:
# #     print(f'Hello {user_name} your gender is {user_gender} and you are {user_age} yearold and you are legible to drive')

# # elif user_gender == 'male' and user_age < 18:
# #     print(f'Hello {user_name} you gender is {user_gender} and you are {user_age} yearold and you are not legible to drive')

# # elif user_gender == 'female' and user_age < 20:
# #     print(f'Hello {user_name} your gender is {user_gender} and you are {user_age}yearsold and you are not legible to drive')

# # elif user_gender == 'female' and user_age > 19:
# #     print(f'Hello {user_name} your gender is {user_gender} and you are {user_age}yearsold and you are legible to drive')

# # else:
# #     print(f'hello {user_name} i dont understand')


# # love = 'my baby'

# # print('b' in love)


# # numeric = float(input('enter any number: '))

# # conversion = numeric

# # print(type(conversion))

# # print(f'your number is {numeric}')


# # strings = 'this is oyindolapo he is crazy'

# # cap = strings.find('is')
# # print(f'is was found {cap} times')

# # print(strings.upper())

# # print(strings.upper()

# # print(strings.find('is'))



# # strings = 'this is a string'

# # conv = strings.replace(' ', '-')

# # print(conv)


# # nac = 'this, is a rabbit'

# # pap = 'God'

# # print(nac.split(','))


# # lists = ['oyindolapo', 'is', 'a', 'boy']

# # print(lists)


# # print(lists.joins)


# # functions

# # def add_number(a:int, b:int):
# #     # print(a+b)

# #     """this is a doc string and it also add number
# #     (a) is a int
# #     (b) is also a int


# #     """
# #     return a+b

# # b = add_number(10, 10)
# # print(b)


# # def simple_intrest(number, time, place):
# #     """
# #     this function sums up the intrest of a given number

    


# #     """
# #     numbers = number * time * place

# #     div = numbers / 100



# #     return div

# # result = simple_intrest(20, 2, 3)
# # print(result)

# # def right_justify(s):
# #     return f'{s}'

# # result = right_justify('olamide')

# # print(len(result))


# # def characters(character, num):
# #     base = character[num:]
# #     return base

# # base = characters('oyindolapo', 5)
# # print(base)


# age = 44

# if age >= 55:
#     print(f'you are {age} yearsold and you are getting old')
# else:
#     print(f'i dont know what you are')


# first_num = int(input('enter the first number:   '))
# second_number = int(input('enter the second number:   '))
# third_num = int(input('enter the third number:   '))

# average = str((first_num + second_number + third_num)/2)
# print('the average of this number is ' + (average))

# print(type(average))

# sentence = input('word: ')

# print(sentence.capitalize())

# write = 'i am learning python'

# print(write.replace('i', 'you', 1))

# joy = 'i hope you had fun today in class'

# print(joy.count('a'))

# def check_fermat(a, b, c, n):
#     if n > 2 and (a**n + b**n == c**n):
#         print('fja;lsdfjld,fdaofu;')
#     else:
#         print('euroe, rtrt')

# check_fermat(a, b, c, n)

# def check_fermatt(a, b, c, n):
# #     # a = 48639
# #     # b = 87864
# #     # c = 74
# #     n = 900563
#     if n > 2 and a**n + b ** n == c ** n:
#         print('holy smoke, fermat was wrong')
#     else:
#         print('No that "dosent work"')


#         final = (a**n + b**n == c**n)
#         return final

# check_fermatt(45, 23, 2, 900563)




# def check_numbers():
#     a = int(input('enter ur 1st value:   '))
#     b = int(input('enter ur 2nd value:   '))
#     c = int(input('enter ur 3rd value:    '))
#     n = int(input('enter ur value:        '))
    

#     if n > 2 and a**n + b ** n == c ** n:
#         print('holy smoke, fermat was wrong')
#     else:
#         print('No that "dosent work"')

#         final = int(a**n + b**n == c**n)
#         return final

# check_numbers()


# def check_format(a, b, c, n):
#     n = 4

#     new_value = (a**n + b**n)
#     cee = c**n

#     if n > 4:
#         print('holy smokes format was wrong')

#     else:
#         print('no, that does not work')

# check_format(40, 56, 6, 5)


# def user ():
#     user_one = input('enter your number: ')
#     user_two = input('enter your second number: ')
#     user_three = input('enter your third number: ')    

# user(use)


# recursion

# def factorial(n):
#     if n == 1:
#         return 1

#     return n * factorial(n-1)

# print(factorial(7))


# mmy_list = [2, 3, 5, 7, 9, 10]

# mmy_list[2] = 67

# print(mmy_list)

# print(sorted(mmy_list, reverse=True))

# import random

# this_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# random.shuffle(this_list)


# print('selection game')

# comp_input = int(random.choice(this_list))

# user_input = int(input('enter your number: '))

# random.choice(this_list)

# if user_input in this_list:
#     print('this number is not within that range')
#     if user_input == comp_input:
#         print('you win')

#     else:
#         if user_input > comp_input:
#             print('too high')
#         else:
#             print('to low')

# else:
#     print('you are missing something')


# import random

# print('guessing game')

# numeric = list(range(40, 60))

# computer = int(random.choice(numeric))
# print(computer)


# print('guess the number your computer choose')

# player = int(input('enter your number: '))

# if player in numeric:
#     if player == computer:
#         print('you won')

#     elif player > computer:
#         print(f'{player} is greater than what the computer picked')

#     elif player < computer:
#         print(f'{player} is less than the computer picked')

#     else:
#         print(f'this {player} is invalid')

# else:
#     print(f'invalid input {player}')



# naming = 'what is your name '

# counting = naming[:4]

# print(counting.capitalize())

# import random

# computers = 'rock'

# users = 'scissors'

# userss = 'paper'

# lisst = ['rock', 'paper', 'scissors']

# computer = random.choice(lisst)

# print(computer)


# nuumeric = [1,2,6, 7, 8,9 ,5 ,45]

# second = [45, 67, 82, 24, 1]

# ziiped = zip(iter1)


# enumerate zips an index with the item

# # a labda function is an anonynous function which can have as many elemenet as desired but expression, the syntax is to say example: 

# lambda x: x.lower()


# a = range(1, 10)

# add = list(filter(lambda x: x % 2==0, a))
# print(add)


# turple is a collecction of data that is enclosed in a collection parenthesis haveing each entry seprated by coma they are orther therefore elemenet in the turple can be access by index they are immutable howeaver they allow duplicate value
# method that we use are 1. index, 

# set: a set is a collection of data that is enclosed in a curly brases haveing each entry seprated by coma, they do not contain duplicate value and the are also unordered

# set method: 1. discard: this is used to remove a specific item from the set

# my_set = {1, 2, 3, 4, 5, 6, 7, 8}

# my_set.add(200)
# print(my_set)

# my_set = {1, 2, 3, 4, 5, 6, 7, 8}
# my_set = {1, 2, 3, 4, 5, 6, 20, 8}

# DICTIONARY IN PYTHON`


# dic = {
#     'name': 'oyindolapo',
#     'age': 'any',
#     'jod': 'backend',
#     'score': [1,2,4,6,3,3],

#     'address':{
#         'str_num': 2,
#         'str_name': 'montgomery',
#         'city':'yabe',
#     }
# }

# dic['ages'] = dic.pop('age')

# print(dic)
# print(dic.get('jod', 'false'))



# print(max(d['girl']))

# dic['score']

# write a program that lets the value in the dictionary to a descending other

# data = {
#     '5':8,
#     '3':10,
#     '4':2,
#     '9':3,
#     '2':7,
#     '0':5
# }

# sorted_x = sorted(data.items(),
# key=lambda x: x[1], reverse=True)

# print(dict(sorted_x))

# list_one = ['names', 'age', 'class', 'seq']

# list_two = ['oyindolapo', 'plate', True, 'pave']

# collect = dict(zip(list_one, list_two))

# print(collect)


# diction = {
#     'v': '5001',
#     'vi':'5002',
#     'vii': '5001',
#     'viii':'5005',
#     'viv':'5005',
#     'vv':'5009',
#     'vvi':'5007'
# }

# crazy = diction.values()
# print(set(crazy))


# while True:
#     right_number = 5

#     ques = int(input('enter the right number:'))
#     print(ques)
#     if ques == right_number:
#         print(f'this number is the right number {ques}')
#         bre


# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1
# print('done')

# import random

# list_number = list(range(5, 15))

# print(list_number)

# computer = random.choice(list_number)

# user_collection = int(input('enter the correct number the computer choose :'))

# if user_collection == computer:
#     print(f'you won the right number is {computer}')

# else:
#     print('you lost at the first stage')

# print(computer)


# i = 1

# while i <= 7:
#     print(i)
#     i = i + 1

# import random

# choices = ['p', 'r', 's']

# computer_choice = random.choice(choices)

# number_of_trail = 5

# guess = 0

# point = 5

# condition = 'stop'

# while guess < number_of_trail:
#     print("welcome to my gues game, you can use the key words P, R, S, to play with computer")
#     user_input = input('enter gues choices to play: ')
#     guess += 1

#     if user_input == 's' and computer_choice == 'p':
#         print('you won')
#         print(f'your score is {point}')
#         break

#     elif user_input == condition:
#         print('game stoped'.upper())
#         break

#     elif user_input == 'p' and computer_choice == 'r':
#         print('you win')
#         print(f'your score is {point}')
#         break

#     elif user_input == 'r' and computer_choice == 's':
#         print('you win')
#         print(f'your score is {point}')
#         break

#     elif user_input == computer_choice:
#         print('its a tie')

#     elif user_input == 'r' and computer_choice == 'p':
#         print('you lose')

#     elif user_input == 's' and computer_choice == 'r':
#         print('you lose')

#     elif user_input == 'p' and computer_choice == 's':
#         print('ýou lose')

#     else:
#         print('you entered incorect input')

#     print(computer_choice)

# else:
#     print('you are out of choices')








# user_input = input('enter computer guess to win: ')

# if user_input == 's' and computer_choice == 'p':
#     print('you won')

# elif user_input == 'p' and computer_choice == 'r':
#     print('you win')

# elif user_input == 'r' and computer_choice == 's':
#     print('you win')

# elif user_input == computer_choice:
#     print('its a tie')

# elif user_input == 'r' and computer_choice == 'p':
#     print('you lose')

# elif user_input == 's' and computer_choice == 'r':
#     print('you lose')

# elif user_input == 'p' and computer_choice == 's':
#     print('ýou lose')

# print(computer_choice)


import random

listing = ['r', 's', 'p']

computer_selection = random.choice(listing)

print(computer_selection)

number_try = 3
user_number = 0
point = 5
stop_game = 'stop'

while user_number <= number_try:
    print('welcome to a random selection game')
    print(user_number)

    user_number += 1

    user_select = input('>: ')
    if computer_selection == 's' and user_select == 'p':
        print('you lose')

    elif user_number == 'r' and computer_selection == 'p':
        print('you lose')


    elif user_select == 's' and computer_selection == 'r':
        print('you lose')


    elif user_select == computer_selection:
        print('its is a draw')

    elif user_select == 's' and computer_selection =='p':
        print(f'you won, you point is {point}')
        points = point
        userinfo = 'you have an extra trial'
        print(userinfo)
        user_selectagain = input('enter random selection again: ')
        if user_selectagain == 's' and computer_selection == 'p':
            points = point * 2
            print(f'you won again, your point is now {points} ')
            break

        elif user_selectagain == 'p' and computer_selection == 'r':
            print(f'you won again, your point is now {points} ')
            break

        elif user_selectagain == 'r' and computer_selection == 's':
            print(f'you won again, your point is now {points} ')
            break

        elif computer_selection == 's' and user_selectagain == 'p':
            print('you lose')

        elif user_selectagain == 's' and computer_selection == 'r':
            print('you lose')

        elif computer_selection == 's' and user_selectagain == 'p':
            print('you lose')

        elif user_selectagain == computer_selection:
            print('its a draw')

        elif user_selectagain == game_stop:
            print('game stoped')
            break

        else:
            print('you lose')

    elif user_select == 'p' and computer_selection =='r':
        print(f'you won your point is {point}')
        points = point * 2
        userinfo = 'you have an extra trial'
        print(userinfo)
        user_selectagain = input('enter random selection again: ')
        if user_selectagain == 's' and computer_selection == 'p':
            print(f'you won again, your point is now {points} ')
            break

        elif user_selectagain == 'p' and computer_selection == 'r':
            print(f'you won again, your point is now {points} ')
            break

        elif user_selectagain == 'r' and computer_selection == 's':
            print(f'you won again, your point is now {points} ')
            break

        elif computer_selection == 's' and user_selectagain == 'p':
            print('you lose')

        elif user_selectagain == 's' and computer_selection == 'r':
            print('you lose')

        elif computer_selection == 's' and user_selectagain == 'p':
            print('you lose')

        elif user_selectagain == computer_selection:
            print('its a draw')

        elif user_selectagain == game_stop:
            print('game stoped')
            break

        else:
            print('you lose')

    elif user_select == 'r' and computer_selection =='s':
        print(f'you won your point is {point}')
        points = point * 2
        userinfo = 'you have an extra trial'
        print(userinfo)
        user_selectagain = input('enter random selection again: ')
        if user_selectagain == 's' and computer_selection == 'p':
            print('you won again')

        elif user_selectagain == 'p' and computer_selection == 'r':
            print('you won again')

        elif user_selectagain == 'r' and computer_selection == 's':
            print('you won again')

        elif computer_selection == 's' and user_selectagain == 'p':
            print('you lose')

        elif user_selectagain == 's' and computer_selection == 'r':
            print('you lose')

        elif computer_selection == 's' and user_selectagain == 'p':
            print('you lose')

        elif user_selectagain == computer_selection:
            print('its a draw')

        elif user_selectagain == game_stop:
            print('game stoped')
            break

        else:
            print('you lose')

    elif user_select == 'stop':
        print('game stoped')
        break

    else:
        print('invalid input')


# player = input('do you still still want to play again ?')
# if player == 'yes':
