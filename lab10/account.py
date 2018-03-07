class Account: 
    ID=0
    
    def __init__(self,balance=100.0,annualInterestRate=0.0):
        self.__balance=balance
        self.__annualInterestRate=annualInterestRate
    
    def get_ID(self):
        return self.__ID 
    
    def set_ID(self,newID):
        self.__ID=newID 
    
    def get_balance(self):
        return self.__balance

    def set_balance(self,newbalance):
        self.__balance=newbalance
    
    def get_annualInterestRate(self):
        return self.__annualInterestRate
    
    def set_annualInterestRate(self,newann):
        self.__annualInterestRate=newann
    
    def getMonthlyInterestRate(self):
        return (self.__annualInterestRate)/12
    
    def getMonthlyInterest(self):
        return (self.__balance)*((self.__annualInterestRate)/12)
    
    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance=self.__balance-amount
            
    def deposit(self,amount1):
        self.__balance=self.__balance+amount1
        
    def __str__(self):
        display_string = ""
        display_string += str(self.__ID) + " has " + str(self.__balance) + " dollars "
        display_string += "and annual interest rate is " + str(self.__annualInterestRate)
        return display_string
