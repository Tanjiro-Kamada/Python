def deposit():
    while True:
        amount = input('Enter the amount to deposit: $').strip()
        if amount.isdigit():
            amount =int(amount)
            if amount <= 0:
                print('Please enter a positive amount.')
            else:
                return amount
deposit_amount = deposit()           
