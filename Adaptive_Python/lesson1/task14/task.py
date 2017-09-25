login = str(100500)
password = str(424242)

user_input = input()
temp = user_input.split()


user_login = str(temp[0])
user_password = str(temp[1])

if user_login == login and user_password == password:
    print("Login success")
elif user_login == login:
    print("Wrong password")
else:
    print("No user with login %s found" % user_login)
