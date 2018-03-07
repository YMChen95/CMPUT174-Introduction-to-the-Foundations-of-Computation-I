from account import Account
def main():
    accountA=Account()
    accountA.set_ID("1234")
    accountA.set_balance(20500)
    accountA.set_annualInterestRate(0.375)
    print(accountA)
    accountA.withdraw(500)
    accountA.deposit(1500)
    print(accountA)
    print(accountA.getMonthlyInterest())
        
main()