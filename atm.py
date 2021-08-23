class Atm(object):
    def __init__(self,cardnumber,pinnumber):
        self.cardnumber=cardnumber
        self.pinnumber=pinnumber

    def cashwithdrawl(self):
        print("withdrawl")

    def balanceenquiry(self):
        print("balanceenquiry")

Atm1=Atm("10","500")
print(Atm1.cardnumber)
Atm1.cashwithdrawl()