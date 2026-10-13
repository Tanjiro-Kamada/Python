#Given x = 7 and y = 14, write nested conditional statements that print:
#"x and y are both even" if both x and y are even numbers.
#"Only y is even" if only y is even.
#"Neither x nor y are even" if both are odd.

x = 21
y = 14

if x % 2 == 0:
    if y % 2 == 0:
        print("x and y are both even")
    else:
        print("Only x is even")
else:
    if y % 2 == 0:
        print("Only y is even")
    else:
        print("Neither x nor y are even")


#2
#Write a program that:

#- Takes a transaction amount and account type ("Standard" or "Premium") as input.
#- If the account type is "Standard":
#- Check if the amount is above 500:
#- If it is, print "Transaction exceeds the limit for Standard accounts."
#- If not, print "Transaction approved."
#- If the account type is "Premium":
#- Check if the amount is above 1,000:
#- If it is, print "Transaction exceeds the limit for Premium accounts."
#- If not, print "Transaction approved."
#- Otherwise “Wrong account type”     

             
amount = float(input("Enter transaction amount: "))
account_type = input("Enter account type (Standard or Premium): ")

if account_type == "Standard":
    if amount > 500:
        print("Transaction exceeds the limit for Standard accounts.")
    else:
        print("Transaction approved.")

elif account_type == "Premium":
    if amount > 1000:
        print("Transaction exceeds the limit for Premium accounts.")
    else:
        print("Transaction approved.")

else:
    print("Wrong account type")


#3
#Write a Python program that checks if a variable student_score is greater than 90. If true, check if the attendance is greater than 80. If both conditions are true, print "Excellent student", otherwise print "Good score, but attendance needs improvement" 

student_score = 95
attendance = 85

if student_score > 90:
    if attendance > 80:
        print("Excellent student")
    else:
        print("Good score, but attendance needs improvement")