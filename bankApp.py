'''
@author Sebastian @Date:17/10/22 @Course&Section: CPAN-214-0ND
The following program is a bank application. It contains functions that are called
within a class. Comments are provided for clarity and understanding.
'''

# Task 12, In short most operations contain validity
# Task 13, Every balance displayed is in 2 decimal places
# Task 15, All 3 bank operations(Display, Withdraw, Deposit) contain functions which are called in the
# parent class

# Things to Note:
# Correct Pin: 3881
# Initial Balance: $1,000

# Task: 1, Prints Introduction
print("Hello and welcome to Humber Bank!")

# Task: 4, Display the balance
# Function: Displays the current users balance
def display_option(balance):
    print("Your current balance is: $","{:.2f}".format(balance))

# Function: Let the user withdraw money from their account. Some options are presented
# or the user can enter their own amount. Some precautions are taken so that the user
# doesn't withdraw money they don't have
def withdrawl_option(balance):
    # Task: 9, Default options/Custom options
    print("Please select the amount you wish to withdraw from your account, or enter a custom value")
    print("Default options:")
    print("[1]: 20")
    print("[2]: 40")
    print("[3]: 60")
    print("[4]: 80")
    print("[5]: 100")
    print("[6]: Custom Amount")
    try:
        value = int(input('Enter option:'))
    except (ValueError, NameError):
        print('Characters should not be entered')
        print('Returning card...')
        exit()
    # Task: 10, Depending on what the user entered it will be deducted from their account
    # As well a new balance will be displayed
    match value:
        case 1:
            # Task 14, If statements are put in place to ensure the user has enough money
            if (20 > balance):
                print('You cannot withdraw more than you have in your account!')
                print('Returning card...')
                exit()
            else:
                balance = balance - 20
                print("Your new balance is: $", "{:.2f}".format(balance))
                return balance
        case 2:
            if (40 > balance):
                print('You cannot withdraw more than you have in your account!')
                print('Returning card...')
                exit()
            else:
                balance = balance - 40
                print("Your new balance is: $", "{:.2f}".format(balance))
                return balance
        case 3:
            if (60 > balance):
                print('You cannot withdraw more than you have in your account!')
                print('Returning card...')
                exit()
            else:
                balance = balance - 60
                print("Your new balance is: $", "{:.2f}".format(balance))
                return balance
        case 4:
            if (80 > balance):
                print('You cannot withdraw more than you have in your account!')
                print('Returning card...')
                exit()
            else:
                balance = balance - 80
                print("Your new balance is: $", "{:.2f}".format(balance))
                return balance
        case 5:
            if (100 > balance):
                print('You cannot withdraw more than you have in your account!')
                print('Returning card...')
                exit()
            else:
                balance = balance - 100
                print("Your new balance is: $", "{:.2f}".format(balance))
                return balance
        case 6:
            amount = float(input('Enter custom amount: '))
            if (amount > balance or amount < 0):
                print('You cannot withdraw more than you have in your account!')
                print('Also you cannot withdraw a negative amount!')
                print('Returning card...')
                exit()
            else:
                balance = balance - amount
                print("Your new balance is: $", "{:.2f}".format(balance))
                return balance

            balance = balance - 20
            return balance
        case _:
            print('Option not available')
            print('Returning card...')
            exit()

# Function: Asks the user to deposit a certain amount of money to their account
# and the balance will display right away.
def deposit_option(balance):
    # Task: 11, Asks the user how much and shows the amount right after
    print("Please enter the amount you wish to deposit into your account")
    try:
        amount = float(input('Amount: '))
    except (ValueError, NameError):
        print('Characters should not be entered')
        print('Returning card...')
        exit()
    if (amount < 0):
        print('You cannot deposit a negative amount!')
        print('Returning card...')
        exit()
    else:
        balance = balance + amount
        print("Your new balance is: $","{:.2f}".format(balance))
        return balance

# Task: 8, Asks the user to perform another option
# Function: If user types N program exits. If user types anything other than capital Y
# program exits. If the user types Y program runs.
def exit_option():
    continueTransaction = input("Continue? (Y/N)")
    if (continueTransaction == 'N'):
        print('Returning card...')
        quit()
    elif(continueTransaction != 'Y'):
        print('Must be either Y/N')
        print('Returning card...')
        quit()

# Parent class which is the base functionality of the program
class bankApplication:

    balance = 1000
    pinChecker = 0
    validPin = 3881

    while pinChecker < 3:
        try:
            # Task: 1, Asks user to enter 4-digit pin
            enteredPin = int(input('Please input your 4-digit pin number: '))
        except (ValueError, NameError):
            print('Characters should not be entered')
            print('Returning card...')
            exit()
        # Task: 2, User has 3 chances to enter the correct otherwise progrom exits
        if enteredPin != validPin:
            print("Wrong pin entered try again")
            pinChecker += 1
            if(pinChecker == 3):
                print('Failed to enter pin 3 times. Returning card...')
                quit()
        # Task: 3, When the correct Pin is entered the main menu will become accessible
        elif int(enteredPin) == validPin:
            print('Valid Pin')
            # After this break executes will move onto menu
            break
        else:
            print('Returning card...')
            exit()
    while True:
        print('Please select the following options for your account')
        # Task: 4, Display balance
        print("Entering 1 will display your balance")
        # Task: 5, Make a withdraw
        print("Entering 2 will allow you to make a withdrawal")
        # Task: 6, Make a deposit
        print("Entering 3 will allow you to make a deposit")
        # Task: 7, Exit program
        print("Entering 4 will exit the program")
        try:
            # Here is where the user makes the option
            menu_num = int(input('Enter Number: '))
        except (ValueError, NameError):
            print('Characters should not be entered')
            print('Returning card...')
            exit()
        if menu_num == 1:
            # Display/Continue
            display_option(balance)
            exit_option()
        elif menu_num == 2:
            # Withdraw/Continue
            balance = withdrawl_option(balance)
            exit_option()
        elif menu_num == 3:
            # Deposit/Continue
            balance = deposit_option(balance)
            exit_option()
        elif menu_num == 4:
            # Purely exit the program
            print('Returning card...')
            exit()
        else:
            print('Option not available')
            print('Returning card...')
            exit()