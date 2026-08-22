import time

username = "Alice"
password = "1234"

print("Client requests authentication")

user_password = input("Enter password: ")

if user_password == password:
    print("Authentication Successful")

    ticket = username + "-" + str(int(time.time()))

    print("Ticket Generated:", ticket)

    print("Client sends ticket to Server")

    if ticket.startswith(username):
        print("Ticket Valid")
        print("Access Granted")
    else:
        print("Ticket Invalid")
else:
    print("Authentication Failed")
