# Example of using classes and objects

class BankAccount:
    num = 1000

    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.pin = int(input(f"{self.name} You are making a new account! What is your pin number:"))

        self.accountNum = BankAccount.num
        BankAccount.num = BankAccount.num + 1
        self.transaction = []

    def withdraw(self):
        check = int(input(f"Hello {self.name}, what is your pin:"))
        if check != self.pin:
            print("ACCESS DENIED!!!")
        else:
            withdrawAmount = int(input("How much money do you want to withdraw:$"))
            if withdrawAmount > self.balance:
                print(f"{self.name} you are withdrawing money, greater than your balance. Please select a different amount")
            else:
                self.balance = self.balance - withdrawAmount
                print(f"{self.name} You have withdrawn ${withdrawAmount} from your account, your new balance is {self.balance}")
                self.transaction.append(f"  Withdrawed amount:s{withdrawAmount},new balance {self.balance}")
    
    def deposit(self):
        depostAmount = int(input("How much many do you want to deposit:$"))
        self.balance = self.balance + depostAmount
        print(f"{self.name} You have deposited ${depostAmount} to your account, your new balance is {self.balance}")




account1 = BankAccount("Walter",10000)

# Withdraw, deposit, transfer money