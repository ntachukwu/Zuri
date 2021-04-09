''' A modified bank ATM system for Zuri Bank '''
import random
import time

from datetime import datetime

bank_database = {}  # A database for all our users


def main():
    """ Main body of the App. """

    try:
        # Catch inputs that are not numerical
        enquire_account = int(
            input("Do you have account with us? \nEnter (1) to Login or (2) to Register a new account ->  "))
    except:
        print("\nOnly numbers are allowed. Please try again")
        main()

    if(enquire_account == 1):
        login()
    elif(enquire_account == 2):
        register()
    else:
        print("Please select either 1 or 2")
        main()


def login():

    print()
    print("*"*100)
    print(" Login ".center(100, "-"))

    print()
    try:
        user_account_number = int(input("Enter your account number? \n"))
    except:
        print("Account Number can't be letters. Please try again.")
        login()
    password = input("Enter your password \n")

    for account_number, user_details in bank_database.items():
        if(account_number == user_account_number):
            if(user_details[3] == password):
                return atm(user_details)

    print('Invalid account or password')
    print()
    login()


def register():
    print()
    print("*"*100)
    print(" Register ".center(100, "-"))

    email = input("Enter a valid email address? \n")
    first_name = input("Enter your first name? \n")
    last_name = input("Enter your last name? \n")
    password = input("Enter a password.\n")

    account_number = account_number_generator()

    bank_database[account_number] = [first_name, last_name, email, password]

    print()
    print("WARNING: Please avoid revealing your password to any one.")
    print("-"*100)
    print("Your ACCOUNT NUMBER number has been created and your data saved to the database.".center(100))
    string1 = "Your account number is: {} ".format(account_number)
    print(("-"*len(string1)).center(100))
    print(string1.center(100))
    print(("="*len(string1)).center(100))
    print()
    print(" Welcome to the Zuri Family. ".center(100, "^"))
    print("*"*100)

    login()


def atm(user):

    if datetime.now().hour <= 12:
        am = "AM"
    else:
        am = "PM"
    print()
    print("-"*100)
    print()
    print((" Welcome {} {} ".format(user[0], user[1])).center(100))
    print()
    print(("The time is {}:{} {} \n".format(
        datetime.now().hour, datetime.now().minute, am)).center(100))
    print("These are the available options: ".rjust(65))
    print("1: Withdrawal".rjust(50))
    print("2: Cash Deposit".rjust(52))
    print("3: Complaint".rjust(49))
    print("4: Logout".rjust(46))
    print("5: Exit".rjust(44))

    try:
        selected_option = int(input("Please select an option:  "))
    except:
        print("Only numbers are allowed.")
        atm(user)
    if(selected_option == 1):
        withdrawal()
    elif(selected_option == 2):
        deposit()
    elif(selected_option == 3):
        complaint()
    elif(selected_option == 4):
        logout()
    elif(selected_option == 5):
        exiter()
    else:
        print("Please enter a valid number")
        atm(user)


def withdrawal():
    op1 = int(input("How much would you like to withdraw? \n"))
    print()
    print(" Please wait while your transaction is processing.".center(100))
    print()
    for i in range(1, 5):
        print(("*"*i*3).center(100))
        time.sleep(1)
    print()
    print(("Take you Cash of N{}. ".format(op1)).center(100))
    print()
    print("*"*100)
    another_transaction()


def deposit():
    op2 = int(input("How much would you like to deposit:  "))
    print()
    print(" Please wait while your transaction is processing.".center(100))
    print()
    for i in range(1, 5):
        print(("*"*i*3).center(100))
        time.sleep(1)
    print()
    print(("Your current balance is: N{}".format(op2)).center(100))
    print()
    print("*"*100)
    another_transaction()


def complaint():
    op3 = input("What issue will you like to report:  ")
    print()
    print("Your complaint has bee documented. Thank you for contacting us.".center(100))
    print()
    print("*"*100)
    another_transaction()


def another_transaction():

    print()
    print(" Would you like to perform another transaction? ".center(100))
    try:
        opp = int(input("Enter (1) for YES and (2) to exit the app -> "))
    except:
        print("Only numbers are allowed. Please try again.")
        another_transaction()
    if opp == 1:
        login()
    elif opp == 2:
        exiter()
    else:
        print("Please enter a valid Number.")
        another_transaction()


def account_number_generator():

    return random.randrange(1111111111, 9999999999)


def logout():
    login()


def exiter():
    ''' This exits the program '''
    print()
    print("  Thank you for banking with us. ".center(100, "-"))
    time.sleep(2)
    exit()


# This calles the Main app to execute first.
if __name__ == "__main__":
    print()
    print("*"*100)
    print()
    print("  Welcome to Zuri Bank  ".center(100, "-"))
    print()
    main()
