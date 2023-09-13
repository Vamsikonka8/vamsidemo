user_name = 'vamsi'
user_password = 1234
amount = 5000
max_attempt = 3

import mysql.connector as c
mydb = c.connect(
    host = 'localhost',
    user = 'root',
    password = '1234',
    database = 'sampledb'
)
mycursor = mydb.cursor()
 
for attempt in range(max_attempt):
    c_name = input('Enter the name:')
    c_pass = int(input('Enter the pin'))

    if c_name == user_name and c_pass == user_password:
        while True:
            print('''
                1. View balance
                2. Desposit
                3. Withdraw
                4.Exit
                '''
            )
            option = int(input ('Enter the option'))
            if option == 1:
                print('your are balance is ', amount)
            elif option == 2:
                dep = int(input('Deposite the amount'))
                b = amount + dep
                # mycursor.execute('select salary from customer')
                print(f'is your are balance is :{b}')
                mycursor.execute(f'update customer set salary = {b} where emp_id = 3')
                mydb.commit()
                # print('your deposit amount and balance is ',amount)
            elif option == 3:
                withd =int(input('Enter your amount'))
                amount -= withd
                print('your are balance is ',amount)
            elif option == 4:
                print('======== ATM=======')
                print('Username :',user_name)
                print('Total amount:', amount)
                print('Thank for Visiting')
                break
            else:
                print(' invalid option ,please select valid option')
    else:
        print(f'Invalid credentials! Attempts left:{max_attempt - attempt-1}')
print('Maximum login attempts reached.Exiting....')        
               
    


