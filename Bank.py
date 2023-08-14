class BankC:
    _Current_balance = None
    _Account_num = None

    # initialing the current balance
    def __init__(self, current_balance, account_num):
        self._Current_balance = current_balance
        # self._Account_num=account_num

    # depositing the money
    def deposit_cash(self, d_amount):
        self._Current_balance += d_amount
        print("you have successfully deposited ", d_amount)

    def check_current_balance(self):
        # calling testing file to show current balance
        return self._Current_balance

    def transfer_funds(self,amount, bank_customer2):
        # transfer fund from account 1 to account 2
        # self.withdraw_cash(self, bank_customer2)
        self.withdraw_cash(self,amount)
        self.deposit_cash(bank_customer2, amount)
        print("you have successfully transferred funds ")

    def withdraw_cash(self, cash):
        if cash > self.check_current_balance():
            # throw exception
            pass
        self._Current_balance -= cash
        print("you have withdrawn ", cash, " your current balance is ", self._Current_balance)

        # calling testing if less than the account request throw exception
        # else
