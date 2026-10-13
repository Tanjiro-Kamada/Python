#if 20>100:
 #   print('twenty is greater')

age = 17

if age>18:
    print('Adult')

if age>=18 and age<=60:
    print('Allow Access')
else:
    print('Minor')

temperature = 29

if temperature>=30:
    print('Too Hot')
else:
    print('Normal Temperature')

marks = 40

if marks>=50:
    print('PASS')
else:
    print('Fail')


marks = 81

if marks>=80:
    print('A')
elif marks>=70:
    print('B')
elif marks>=60:
    print('C')
elif marks>=50:
    print('D')
else:
    print('E')


credit_score = int(input("Enter your credit score: "))

if credit_score > 700:
    income = int(input("Enter your annual income: "))

    # Nested if
    if income > 50000:
        print("Loan approved.")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")