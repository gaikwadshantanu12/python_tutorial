class BankAccount:
    number = 845000

    def __init__(self,name,balance):
        BankAccount.number += 1
        self.account_no = BankAccount.number
        self.account_name = name.title()
        self.account_balance = balance

    def set_pin(self,pin):
        self.account_pin = int(pin)

    def get_pin(self):
        return self.account_pin

    def get_account_no(self):
        return self.account_no

    def deposit(self):
        print(f"Hello {self.account_name}")
        amount = float(input("Enter Amount To Deposit : "))
        self.account_balance += amount
        print(f"Rs.{amount} has been deposited")

    def withdraw(self):
        print(f"Hello {self.account_name}")
        amount = float(input("Enter Amount To Withdraw : "))
        if(self.account_balance < amount):
            print("Insufficient Funds")
            return
        self.account_balance -= amount
        print(f"Rs.{amount} has been withdrawn")

    def display(self):
        print(f"\nAccount No : {self.account_no}"
              f"\nName       : {self.account_name}"
              f"\nBalance    : {self.account_balance}")

accounts = []

while True:
    print(f"!!!!!!!!!!!!!!! MENU !!!!!!!!!!!!!!!"
          f"\n1. New Account"
          f"\n2. Deposit Money"
          f"\n3. Withdraw Money"
          f"\n4. Check Balance"
          f"\n5. Reset Pin"
          f"\n0. Exit")

    ch = int(input("Enter Your Choice : "))

    if ch == 0:
        break

    elif ch not in range(1,6):
        print("Invalid Choice !")

    elif ch == 1:
        name = input("Enter Account Holder Name : ")
        balance = float(input("Enter Opening Balance : "))
        b = BankAccount(name,balance)
        print(f"Account has been opened successfully"
              f"\nYour account number is {b.get_account_no()}")
        pin = int(input("Enter Your 4 Digit Pin : "))
        b.set_pin(pin)
        accounts.append(b)

    else:
        acc_no = int(input("Enter Account Number : "))

        if ch == 2:
            # flag = False
            for b in accounts:
                if b.get_account_no() == acc_no:
                    pin = int(input("Enter Your Account Pin : "))
                    if b.get_pin() == pin:
                        b.deposit()
                        # flag = True
                        break
                    else:
                        print("Incorrect Pin !")
                        break
            else:
                print("Invalid Account Number !")

        elif ch == 3:
            for b in accounts:
                if b.get_account_no() == acc_no:
                    pin = int(input("Enter Your Account Pin : "))
                    if b.get_pin() == pin:
                        b.withdraw()
                        break
                    else:
                        print("Invalid Pin !")
                        break
            else:
                print("Invalid Account Number !")

        elif ch == 4:
            for b in accounts:
                if b.get_account_no() == acc_no:
                    pin = int(input("Enter Your Account Pin : "))
                    if b.get_pin() == pin:
                        b.display()
                        break
                    else:
                        print("Invalid Pin !")
                        break
            else:
                print("Invalid Account Number !")

        else:
            for b in accounts:
                if b.get_account_no() == acc_no:
                    pin = int(input("Enter Your Old Account Pin : "))
                    if b.get_pin() == pin:
                        new_pin = int(input("Enter New Pin For Your Account : "))
                        b.set_pin(new_pin)
                        print("Pin Updated !")
                        break
                    else:
                        print("Invalid Pin !, Pin Not Matched !")
                        break
            else:
                print("Invalid Account Number !")

    input(">>> Hit Enter To Continue >>>\n")

print("Thank You !\tVisit Again !")