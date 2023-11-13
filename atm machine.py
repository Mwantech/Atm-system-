#define data
account_balance=0

#initialize pin
pin=input("Enter your pin: ")
if pin=='1305':
    while True:
        print("***options***")
        print("1.send money")
        print("2.withdraw money")
        print("3.deposit money")
        print("4.change pin")
        print("5.check balance")
        print("6.exit")
    
        choice=input("enter your choice: ")
        if choice=='1':
            accountnumber=input("account number: ")
            amount=float(input("enter amount: "))
            if amount > account_balance:
                print("insufficcient balance!")
            else:
                print(f"you have successfully transferred {amount} to {accountnumber}")

        elif choice=='2':
            withdraw=float(input("enter amount to withdraw: "))
            if withdraw > account_balance:
                print("insufficcient balance!")
            else:
                account_balance-=withdraw
                print(f"your have successfully withdrawn {withdraw}")

        elif choice=='3':
            deposit=float(input("deposit: "))
            account_balance +=deposit
            print(f"amount {deposit} has been successfully deposited into your account")
        elif choice=='4':
            newpin=input("enter new pin: ")
            print("your pin has been successfully changed! ")
        elif choice=='5':
            print(f"your balance is: {account_balance}")
        elif choice=='6':
            print("Goodbye!!!")
            break
        else:
            print("invalid option! please try again.....")
else:
    print("wrong pin! please try again.....")