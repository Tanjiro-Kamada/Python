#1. Write a program that prompts the user to enter the base and height of a triangle and returns its area.
def triangle_area(base, height):
    area = 0.5 * base * height
    return area
t1 = triangle_area(5, 10)
print(t1)

#2. Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")



#3. Write a program which gets a phone number from a form input or terminal. Validates the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or  1.. Convert the number to start with +254… 
# e.g if a user enters “0712345678”, the program should display “+254712345678”
# e.g if a user enters “0112345678”, the program should display “+254112345678”
# e.g if a user enters “712345678”, the program should display “+254712345678”
phone_number = input("Enter your phone number: ")
if phone_number.startswith("+254"):
    print(phone_number)
elif phone_number.startswith("07"):
    print("+254" + phone_number[1:])
elif phone_number.startswith("7"):
    print("+254" + phone_number)
elif phone_number.startswith("254"):
    print("+" + phone_number)
elif phone_number.startswith("01"):
    print("+254" + phone_number[2:])
elif phone_number.startswith("1"):
    print("+254" + phone_number[1:])
else:
    print("Invalid phone number format.")





#4. Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
email = input("Enter your email: ")
if "@" in email and "." in email:
    print("Valid email")
else:
    print("Invalid email")



#5. Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("The largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The largest number is:", num2)
else:
    print("The largest number is:", num3)


#6. Write a program that lets the user input a password. Give them only 4 attempts to check the passwords entered against “admin@123”. If the password is correct access is granted. After you show them a message , the account is blocked.
password = input("Enter your password: ")
attempts = 0
while attempts < 4:
    if password == "admin@123":
        print("Access granted.")
        break
    else:
        print("Invalid password.")
        password = input("Enter your password: ")
        attempts += 1
if attempts == 4:
    print("Account blocked.")



#7. Write that prompts the user to input student marks. The input should be between 0 and 100.Then output the correct grade: 
# A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40

marks = int(input("Enter student marks (0-100): "))
if 0 <= marks <= 100:
    if marks > 79:
        print("Grade: A")
    elif 60 <= marks <= 79:
        print("Grade: B")
    elif 50 <= marks <= 59:
        print("Grade: C")
    elif 40 <= marks <= 49:
        print("Grade: D")
    else:
        print("Grade: E")


#8. Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....

rows = int(input("Enter a number: "))
for i in range(1, rows + 1):
    print("*" * i)


#9. Write a program that calculates the total stock in a company from the array/list below if we know that the stock is the last digit in every array/list.
# prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
# NB: ONCE YOU COPY AND PASTE THE LIST ABOVE,REWRITE THE SINGLE QUOTES AS THE ABOVE LIST WILL GIVE YOU AN ERROR.

prods = [['omo', '30kshs', '300'],
         ['milk', '50kshs', '200'],
         ['bread', '45kshs', '359'],
         ['coffee', '5kshs', '79']]

total_stock = 0

for product in prods:
    total_stock += int(product[-1])

print("Total stock:", total_stock)

#10. Write a program that takes the date of birth of a person and the program outputs the age in terms of years,months,days TODAY.datetime
date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ")
from datetime import datetime
current_date = datetime.now()
age = current_date - datetime.strptime(date_of_birth, "%Y-%m-%d")
print("Age:", age.days // 365, "years,", (age.days % 365) // 30, "months,", (age.days % 365) % 30, "days")


#11. Write a program that prints the largest of 4 inputs taken as input from a user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
num4 = float(input("Enter fourth number: "))
largest = max(num1, num2, num3, num4)
print("The largest number is: ", largest)

#12. Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.
email = input("Enter email: ")
password = input("Enter password: ")
tries = 0
while tries < 3:
    if email == "admin@mail.com" and password == "Admin@123":
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")
        tries += 1
        if tries < 3:
            email = input("Enter email: ")
            password = input("Enter password: ")
else:
    print("You have been blocked")

#13. Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print("The sum is:", result)
        break
    except ValueError:
        print("Invalid character entered. Please enter numbers only.")


#14. Write a program that takes input of someone's basic salary and benefits, adds them to find the gross salary then uses  the gross salary to find the NHIF. 
# To find the Kenya NHIF Rate using THIS LINK:
# https://www.nhif.or.ke/index.php/2020/07/01/nhif-contribution-rates/

basic_salary = float(input("Enter your basic salary: "))
benefits = float(input("Enter your benefits: "))

gross_salary = basic_salary + benefits

if gross_salary < 6000:
    nhif = 150
elif gross_salary < 8000:
    nhif = 300
elif gross_salary < 12000:
    nhif = 400
elif gross_salary < 15000:
    nhif = 500
elif gross_salary < 20000:
    nhif = 600
elif gross_salary < 25000:
    nhif = 750
elif gross_salary < 30000:
    nhif = 850
elif gross_salary < 35000:
    nhif = 900
elif gross_salary < 40000:
    nhif = 950
elif gross_salary < 45000:
    nhif = 1000
elif gross_salary < 50000:
    nhif = 1100
elif gross_salary < 60000:
    nhif = 1200
elif gross_salary < 70000:
    nhif = 1300
elif gross_salary < 80000:
    nhif = 1400
elif gross_salary < 90000:
    nhif = 1500
elif gross_salary < 100000:
    nhif = 1600
else:
    nhif = gross_salary * 0.017

print("Gross salary: ", gross_salary)
print("NHIF: ", nhif)


#15. Continue with the program above, then use  the gross salary to find the NSSF. 
# To find the Kenya NSSF Rate  using 6% of the Gross Salary. BUT ONLY A MINIMUM OF 18,000 Gross Salary CAN BE USED IN NSSF.

nssf = max(gross_salary * 0.06, 18000)
print("NSSF: ", nssf)

#16. Continue with the same program and calculate an individual’s NHDF using:
#  i.e NHDF = gross_salary *  0.015

nhdf = gross_salary * 0.015
print("NHDF: ", nhdf)


#17. Calculate the taxable income.
# i.e taxable_income = gross salary - (NSSF + NHDF + NHIF)
# taxable_income = gross_salary - (nssf + nhdf + nhif)
taxable_income = gross_salary - (nssf + nhdf + nhif)
print("Taxable income: ", taxable_income)


#18. Continue with the same program and find the person's PAYEE using the taxable income above.
# Find the Kenya PAYEE Tax Rate using THIS LINK

payee = 0
if taxable_income <= 12298:
    payee = taxable_income * 0.1
elif taxable_income <= 23885:
    payee = (taxable_income - 12298) * 0.15 + (12298 * 0.1)
elif taxable_income <= 35472:
    payee = (taxable_income - 23885) * 0.2 + (23885 - 12298) * 0.15 + (12298 * 0.1)
elif taxable_income <= 47059:
    payee = (taxable_income - 35472) * 0.25 + (35472 - 23885) * 0.2 + (23885 - 12298) * 0.15 + (12298 * 0.1)
elif taxable_income <= 58646:
    payee = (taxable_income - 47059) * 0.3 + (47059 - 35472) * 0.25 + (35472 - 23885) * 0.2 + (23885 - 12298) * 0.15 + (12298 * 0.1)
elif taxable_income <= 70233:
    payee = (taxable_income - 58646) * 0.35 + (58646 - 47059) * 0.3 + (47059 - 35472) * 0.25 + (35472 - 23885) * 0.2 + (23885 - 12298) * 0.15 + (12298 * 0.1)
elif taxable_income <= 81820:
    payee = (taxable_income - 70233) * 0.4 + (70233 - 58646) * 0.35 + (58646 - 47059) * 0.3 + (47059 - 35472) * 0.25 + (35472 - 23885) * 0.2 + (23885 - 12298) * 0.15 + (12298 * 0.1)
elif taxable_income <= 93407:
    payee = (taxable_income - 81820) * 0.45 + (81820 - 70233) * 0.4 + (70233 - 58646) * 0.35 + (58646 - 47059) * 0.3 + (47059 - 35472) * 0.25 + (35472 - 23885) * 0.2 + (23885 - 12298) * 0.15 + (12298 * 0.1)
elif taxable_income > 93407:
    payee = (taxable_income - 93407) * 0.5 + (93407 - 81820) * 0.45 + (81820 - 70233) * 0.4 + (70233 - 58646) * 0.35 + (58646 - 47059) * 0.3 + (47059 - 35472) * 0.25 + (35472 - 23885) * 0.2 + (23885 - 12298) * 0.15 + (12298 * 0.1)
print("PAYEE: ", payee)


#19. Continue with the same program and calculate an individual’s Net Salary using:
# net_salary = gross_salary - (nhif + nhdf +  nssf + payee)
net_salary = gross_salary - (nhif + nhdf + nssf + payee)
print("Net Salary: ", net_salary)
