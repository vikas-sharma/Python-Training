class Account1:

    # single underscore naming convention for private variables. For ex _name

    def __init__(self): # constructor
        print('SB Acc#')

    def adduser(self, n): # instance method
        self.name=n # instance variable

    def viewuser(self):
        return self.name

    def viewbank(self):
        return self.bank

    bank = 'ICICI' # class variable

    def bankrules(): # class method
        return 'Bank Rules'

class Account2(Account1):

    def __init__(self):
        super().__init__()
        # Account1.__init__(self)
        print('CA Acct#')

    def addadhar(self, a):
        self.adhar = a

    def viewadhar(self):
        return self.adhar

    def viewuser(self):
        return 'Welcome ' + self.name

class RBI:
    def viewrules(self):
        return 'RBI rules'

class Account3(Account2, RBI):
    def message(self):
        return 'In Account3'

class Govt:
    def viewRules(self):
        return 'Govt rules'

class Account4(Account3):
    def __init__(self):
        self.gov = Govt()

class Account5:
    def __init__(self, n):
        self.name = n

    def __add__(self, other): # + operator over-loading
        return 'Hello ' + self.name + ' and ' + other.name

cust1 = Account1() # cust1 is instance object
cust2 = Account1()

cust1.adduser('c1')
cust2.adduser('c2')

print(cust1.viewuser())
print(cust2.viewuser())

print(Account1.bank) # Account1 is class object

print(Account1.bankrules())

cust3=Account2()
cust3.adduser('c3')
print(cust3.viewuser())
print(Account2.bank)
print(Account2.bankrules())
cust3.addadhar('A1')
print(cust3.viewadhar())

cust4 = Account3()
print(cust4.viewrules())

cust5=Account4()
print(cust5.viewrules())
print(cust5.gov.viewRules())

a=Account5('abc')
b=Account5('xyz')
c = a + b
print('c = ', c)