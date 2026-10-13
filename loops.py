fruits = ['mango', 'oranges', 'apple', 'lemon', 'grapes']
for i in fruits:
    print(i)

numbers = [10,20,30,40,50]
for b in numbers:
    print('hello')

names = [1,2,3,4,5,6,7,8,9,10]
for a in names:
    print('Benson Mikingo')


nums = list(range(1,101))
for q in nums:
    print('Ben')




list = list(range(10,51))
odd_numbers = []
for i in list:
    if i % 2 == 0:
        odd_numbers.append(i)
print(odd_numbers)


# last = list(range(100,151))
# for num in last:
#     if num % 5 == 0:
#         print(num)

# lest = list(range(30,101))
# even_numbers = []
# for n in lest:
#     if n % 2 != 0:
#         even_numbers.append(n)
# print(even_numbers)

# lost = list(range(1,101))
# by_3 = []
# by_5 = []
# for num in lost:
#     if num % 3 == 0 and num % 5 == 0:
#         by_3.append(num)
#         by_5.append(num)
#     elif num % 3 == 0:
#         by_3.append(num)
#     elif num % 5 == 0:
#         by_5.append(num)
    
# print('Numbers divisible by 3:', by_3)
# print('Numbers divisible by 5:', by_5)






# lust = list(range(1,4))
# print('lust')
# attempt = 3
# for a in lust:
#     pin = int(input('Enter your pin: '))
#     correct_pin = 1234
#     if pin == correct_pin:
#         print('Access granted')
#         break
#     else:
#         rem_att=attempt - a
#         print('Access denied. You have', rem_att, 'attempts left.')
#         if rem_att == 0:
#             print('Account locked. Please try again later.')
#         else:
#             print(f'You have {rem_att} attempts left. Please try again.')