print("*** welcome To My First Basic Project In Python ***")
print("")
class bank:
    no_of_coustme=0
    coustmer_account_no=8128
    def __init__(self,name,phone_no,initial_deposit,pin):
        self.name=name
        self.phone_no=phone_no
        self.initial_deposit=initial_deposit
        self.pin=pin
        self.coustmer_account_no=bank.coustmer_account_no
        bank.coustmer_account_no=bank.coustmer_account_no+1
        bank.no_of_coustme=bank.no_of_coustme+1
    def basic_informatio(self):
         print(f"user:{self.name}\t Account_no:{self.coustmer_account_no}\t Balance:Rs{self.initial_deposit}")
        # print(self.name)
        # print(self.coustmer_account_no)
        # print(self.balance)
    def deposit(self):
        amount=int(input("Enter amount for deposit:"))
        if amount > 0:
            self.initial_deposit=self.initial_deposit+amount
            print("Transaction completed successfull your current ballance is:Rs",self.initial_deposit)
        else:
            print("Invalid amount transaction")
    def with_draw(self):
        amount=int(input("Enter amount for withdraw:"))
        if amount <=self.initial_deposit and amount > 0:
            self.initial_deposit=self.initial_deposit-amount
            print(f"Transaction completed successfull your current ballance is:Rs{self.initial_deposit}")
        else:
            print("Invalid amount transaction")

    def payment(self,other):
        amount = int(input("Enter amount for payment:"))
        if amount <= self.initial_deposit and amount > 0:
            self.initial_deposit = self.initial_deposit - amount
            other.initial_deposit=other.initial_deposit+amount
            print(f"Transaction completed successfull your current ballance is:Rs {self.initial_deposit}")
        else:
            print("Invalid amount transaction")

obj1=bank(name='hassan',phone_no=6627646,initial_deposit=200000,pin=8128)
obj2=bank(name='abdulrehman',phone_no=4805022,initial_deposit=300000,pin=3773)
obj3=bank(name='samiullah',phone_no=46577,initial_deposit=500000,pin=73)
print("NO Of Coustmer:",bank.no_of_coustme)
print(obj1.basic_informatio())
# print(obj2.basic_informatio())
# print(obj3.basic_informatio())
obj1.deposit()
# obj1.with_draw()
# obj1.payment(obj2)
# print(obj2.basic_informatio())


