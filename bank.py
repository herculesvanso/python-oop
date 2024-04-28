import datetime

class Person():
    def __init__(self,name,cpf) -> None:
        self.name = name
        self.cpf = cpf


class Historic():
    def __init__(self) -> None:
        self.opening_date = datetime.datetime.today()
        self.transactions = []

    def print(self,):
        print(f"Opening date {self.opening_date}")
        print("Transactions")
        for transaction in self.transactions:
            print("-",transaction)


class Account():
    def __init__(self,num,person,limit):
        self.num = num
        self.person = person
        self.historic = Historic()
        self.limit = limit
        self.fund = 0

    def deposit(self,value: float) -> bool:
        self.fund +=value
        self.historic.transactions.append("Deposit: {}".format(value))
        return True

    def to_withdraw(self,value: float) -> bool:
        if self.fund > value:
            self.fund -= value
            self.historic.transactions.append("Withdraw: {}".format(value))
            return True
        else:
            print("Insufficient funds to withdraw.")
            return False

    def transfer_to(self, account_to, value: float):
        withdraw = self.to_withdraw(value)
        if withdraw:
            account_to.deposit(value)
            self.historic.transactions.pop(-1)
            self.historic.transactions.append("Transfer: {} to {}".format(value,account_to.num))
            return True
        else:
            print("Insufficient funds to tranfer.")
            return False

    def statement(self,):
        print("Fund: {}".format(self.fund))
        print("Statement: {}".format(self.historic.transactions))


