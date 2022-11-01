# This is the starting file for the 80-Point version of Lab05.
# The ATM Program
# Evin Lodder 11/2/22
loDebitCardNbr: int = 4444333322221111
hiDebitCardNbr: int = 4444333322229999
bankBalance: float = eval(input("Enter Bank Balance ==> "))
dailyLimit: int = eval(input("Enter Daily Limit ==> "))
storedPin: int = 1234
withdrawal: float = 0
#

# Evaluate card number
number: int = eval(input("Enter Debit Card Number: "))
while number < loDebitCardNbr or number > hiDebitCardNbr:
    print("Invalid Debit Card")
    number = eval(input("Enter Debit Card Number: "))
print("Valid Debit Card")

# Evaluate PIN
enteredPin: int = eval(input("Enter PIN "))
tries: int = 0
while enteredPin != storedPin:
    print("Invalid PIN")
    tries += 1
    if tries == 3:
        print("You have exceeded the 3-try limit.\nYour account is locked.\nPlease contact a bank officer.")
        exit()
    enteredPin = eval(input("Enter PIN "))
print("Valid PIN")

# Evaluate inputted withdrawal amount
amount: float = eval(input("Enter withdrawal amount "))
if amount > bankBalance or amount > dailyLimit:
    print("Transaction canceled.\nYou have insufficient balance or exceeded daily limit.")
    exit()
print("Printing receipt...\nPlease take your cash.")
