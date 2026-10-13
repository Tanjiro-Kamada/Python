# 1.Write a program that displays a numbers 1 to 50 inside a list.
numbers = list(range(1, 51))

print(numbers)

# 2.From 1 above display the ones divisible by 7 or 5 inside a list.

divisible_by_7_or_5 = []
for num in numbers:
    if num % 7 == 0 or num % 5 == 0:
        divisible_by_7_or_5.append(num)

print(divisible_by_7_or_5)

# 3.Find sum and average of values in the range between 10 to 40.
sum_values = sum(range(10, 41))
average_values = sum_values / len(range(10, 41))
print(f"Sum: {sum_values}, Average: {average_values}")

# 4.Put in a list the first 10 odd numbers between 10 to 50. 
odd_numbers = []
for num in range(10, 51):
    if num % 2 != 0:
        odd_numbers.append(num)
        if len(odd_numbers) == 10:
            break
print(odd_numbers)

# 5.write a program that takes a number as input and prints its multiplication table up to 10 using a for loop.
num = int(input("Enter a number: "))
for i in range(1, 101):
    print(f"{num} x {i} = {num * i}")

# 6.write a program that counts and prints the number of even numbers between 1 and 50 using a for loop
even_count = 0
for num in range(1, 51):
    if num % 2 == 0:
        even_count += 1
print(f"Number of even numbers between 1 and 50: {even_count}")

# 7.ls1 = [ (“Jay”, ‘20’), (“Mo”, ‘30’), (“Mya”, ‘32’) ]
#     Display the total quantity of the 3 above.
ls1 = [("Jay", '20'), ("Mo", '30'), ("Mya", '32')]
total_quantity = sum(int(quantity) for _, quantity in ls1)
print(f"Total quantity: {total_quantity}")

# 8.Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
correct_password = "admin@123"
for attempt in range(4):
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print(f"Incorrect password. You have {3 - attempt} attempts left.")
else:
    print("Account blocked.")