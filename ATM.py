print("Welcome to AIT Bank !!")
pin = 5050
chances = 3
balance = 30000
while chances !=0:
    user_pin= int(input("please enter the four digit pin :"))
    if user_pin != pin:
        chances -=1
        print("wrong pin")
        print(f" you have {chances} chnaces left")
    else:
        user_choice = input("B : Balance =, D :Deposite = , W: withdraw =")
        if user_choice == "B":
            print(f" your total balance is Rs.{balance}")

        if user_choice == "D":
            deposite_user = int(input("Please Enter the amount :"))

            total_balance = deposite_user + balance
            print(f"You have deposited Rs.{deposite_user}")
            print(f"Your total balance is Rs.{total_balance}")
        if user_choice == "W":
            withdraw_user = int(input("Enter the Amount you want to withdraw :"))
            total_balance = balance-withdraw_user
            print(f"You have withrawn Rs.{withdraw_user}")
            print(f"Your total balance is Rs.{total_balance}")

    user_exit = input("Would you like to exit? yes/no = ")
    if user_exit == "yes":
        print("Thank you for using AIT Bank !!")
        break
    else:
        continue










