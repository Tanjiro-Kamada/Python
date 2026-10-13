temperature = 16

if temperature>=30:
    print('The temperature is too high.')
elif temperature>=15:
    print('Normal temperature.')
else:
    print('Cold Temperature.')

x = 21
y = 100

if x>=10 and x<=20 or y>=101:
    print('Conditions met.')
else:
    print('Conditions not met')

password = 123

if password==123:
    print('Access Granted')
else:
    print('Access Denied')


start_date = '2024-01-01'
end_date = '2024-12-31'

if start_date<'2024-12-31':
    print('Valid Period')
elif start_date>'2024-12-31':
    print('Invalid Period')
elif start_date=='2024-12-31':
    print('One day Period')
else:
    print('Try Again')


valid_ids = [101,102,103]
user_id = 105

if user_id in valid_ids:
    print('Access Granted')
else:
    print('Access denied')


    



