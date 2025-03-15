class BalanceException(Exception):
    pass

class bankaccount:
    def __init__(self, initialamount, accname):
        self.balance = initialamount
        self.name = accname
        print(f"\n Account {self.name} created.\nBalance ${self.balance:.2f}")

    def getbalance(self):
        print(f"\n Account '{self.name}' balanced = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit completed.")
        self.getbalance()

    def transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\n Sorry account {self.name} has balance of ${self.balance:.2f}")
    
    def withdraw(self,amount):
        try:
            self.transaction(amount)
            self.balance=self.balance-amount
            print("\nWithraw completed")
            self.getbalance()
        except BalanceException as error:
            print(f"\n Withdraw interupted:{error}")
    
    def transfer(self,amount,account):
        try:
            print("\n*************\ntransfer begining....")
            self.transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("Transfer completed\n**************")
        except BalanceException as error:
            print(f"\n transfer interupted.{error}")
            
class intrestrewardacc(bankaccount):
    def deposit(self, amount):
        self.balance=self.balance+(amount*1.05)
        print("\n Deposit completed")
        self.getbalance()
            
            
class savingaccount(intrestrewardacc):
    def __init__(self, initialamount, accname):
        super().__init__(initialamount, accname)
        self.fee=5
        
    def withdraw(self, amount):
        try:
            self.transaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\nwithdraw completed")
            self.getbalance()
        except BalanceException as error:
            print("\n withdraw interupted: {error}")
            
