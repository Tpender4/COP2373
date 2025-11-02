class BankAcct:
    def __init__(self, name, account_number, amount=0.0, interest_rate=0.0):
        self.name = name
        self.account_number = str(account_number)
        self.amount = float(amount)
        self.interest_rate = float(interest_rate)
        self._last_interest = None  # (days, interest)

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = float(new_rate)

    def deposit(self, amt):
        if amt <= 0: raise ValueError("deposit must be > 0")
        self.amount += amt
        return self.amount

    def withdraw(self, amt):
        if amt <= 0 or amt > self.amount: raise ValueError("invalid withdrawal")
        self.amount -= amt
        return self.amount

    def balance(self):
        return self.amount

    def calculate_interest(self, days):
        if days < 0: raise ValueError("days must be >= 0")
        i = round(self.amount * (self.interest_rate / 365) * days, 2)  # simple daily interest
        self._last_interest = (days, i)
        return i

    def __str__(self):
        s = f"Account: {self.name} • ****{self.account_number[-4:]}\nBalance: ${self.amount:.2f}\nAPR: {self.interest_rate*100:.2f}%"
        if self._last_interest:
            d, i = self._last_interest
            s += f"\nLast interest: ${i:.2f} for {d} days"
        return s


def test_bankacct():
    acct = BankAcct("Marquese", "123456789", amount=1000, interest_rate=0.05)
    print(acct)
    acct.deposit(200)
    acct.withdraw(50)
    print("30-day interest:", acct.calculate_interest(30))
    print(acct)


if __name__ == "__main__":
    test_bankacct()