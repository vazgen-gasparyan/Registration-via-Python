'''

In this program your username and password is saved in the json
file as a dictionary and from there every time the program reads
and finds everyone's data, then and when you register it checks 
the contents of the json file and if there is no such user adds, 
and the password the program determines through the generator 
and sends the username together to the e-mail address you
entered, later you can log in with the same password.

'''


import json, smtplib
from string import ascii_lowercase as al, ascii_uppercase as au
from re import search
from random import sample

data = json.load(open('data.json')) # usernames and passwords are stored here
pattern = '^[a-z 0-9]+[\_.]?[a-z 0-9]+[@]\w+[.]\w{2,3}$' # for validate email

login = int(input('Enter 1 for \"sign up\" or 2 for \"sign in\"  -  '))
while login not in (1,2):
    login = int(input('please enter 1 for \"sign up\" or 2 for \"sign in\"  -  '))

# sign up
if login==1:
    print('''
Attention!
Before registering, I would like to inform you
that your username and password will always be
stored, with which you can log in later. Please
note that we do not use your data.
''')

    char = '1234567890_.'+al
    username=input('username  -  ').lower()
    # validate username
    while (all([i if i in char else False for i in username])==False or len(username)<1 or username[0]=="." or username[-1]=="." or username in data):
        print('''Such a username already exists or this username invalid, it must contain at least one character.
Characters from a to z, 1,2,...9..., . and _.''')
        username=input('valid username  -  ')
        if (len(username)>=1 and username[0]!="." and username[-1]!="." and all([i if i in char else False for i in username]) and username not in data):
            break
    email=input('email  -  ').lower()
    # validate email
    while not search(pattern,email):
        email=input('''This email invalid.
Please enter valid email  -  ''').lower()

    # password generator
    password=''.join(sample(char+au+'?=.*\!$^',8))

    # add user in json data
    data[username]=password
    open('data.json',"w").write(json.dumps(data))
    # The username and password are sent to the email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.starttls
    server.login('Your gmail address','gmail password') # Please write your gmail address and password
    server.sendmail('Your gmail address',email, f'Subject: Your Python code password \n\nWelcome to my program and thank you for registering.\n\nYour credentials:\nUsername - {username}\nPassword - {password}\n\nThank you again for your registration. If you have any questions, I am here to help you!\nSincerely,\nYour full name') # Write your full name
    server.quit()
    print(f'''
Your password has been sent to your email address.

Hello {username}, you have successfully sign up.''')

else:
    # sign in
    username=input('username  -  ').lower()
    while username not in data:
		    username=input('''There is no such username or this username invalid.
Please enter valid username  -  ''')
    
    password=input('password  -  ')
    while password != data[username]:
		    password=input('''There is no such password or this password invalid.
Please enter valid password  -  ''')
    print(f'\nHello {username}, you have successfully sign in.')



# code by Vazgen Gasparyan
# Facebook: https://bit.ly/3zhk3PO

# Thank you!
