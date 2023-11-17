from abc import ABC,abstractmethod
class bank(ABC):
    @abstractmethod
    def loan(self): pass
    @abstractmethod
    def credit(self): pass
    @abstractmethod
    def debit(self): pass
class HDFC(bank):
    def loan(self):
        print("loan got")
    def credit(self):
        print("credit got")
    def debit(self):
        print("debit got")    
    def card(self):
        print("card got")
o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()

    
