import datetime

class Person():
    def __init__(self,name,cpf) -> None:
        self.__name = name
        self.__cpf = cpf
 

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

    __cod = 1

    @staticmethod
    def get_next_cod():
        return Account.__cod

    def __init__(self,num,person,limit):
        self.__cod = Account.__cod
        Account.__cod += 1
        self.__num = num
        self.person = person
        self.historic = Historic()
        self.__limit = limit
        self.__fund = 0

    @property
    def fund(self,):
        return self.__fund
        
    @fund.setter
    def fund(self,value):
        if valua < 0:
            print("Fund doesn't admit negative value")
        else:
            self.__fund = value


    def deposit(self,value: float) -> bool:
        self.__fund +=value
        self.historic.transactions.append("Deposit: {}".format(value))
        return True

    def to_withdraw(self,value: float) -> bool:
        if self.__fund > value:
            self.__fund -= value
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
            self.historic.transactions.append("Transfer: {} to {}".format(value,account_to.__num))
            return True
        else:
            print("Insufficient funds to tranfer.")
            return False

    def statement(self,):
        print("Fund: {}".format(self.__fund))
        print("Statement: {}".format(self.historic.transactions))


