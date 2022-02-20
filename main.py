Main_pwd = input("What is the main password?" + "\n")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            print (line.rstrip())


def add():
    username = input("What is your username?" + "\n")
    pwd = input("What is your password?" + "\n")

    with open("passwords.txt", "a") as f:
        f.write("Username =" + username + "  ,    " + "Password =" + pwd + "\n")

while True:
    mode = input("Would you like to add a new password or view your passwords?  (view/add)\n or q to quit" + "\n").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("That is not a valid option")
        continue
