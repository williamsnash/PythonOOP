from .bank_account import BankAccount


class SavingsAccount(BankAccount):
  def __init__(self, owner, balance=0.0, interest_rate=0.01):
    super().__init__(owner, balance)
    self.interest_rate = interest_rate

  def add_interest(self):
    interest = self.balance * self.interest_rate
    self.deposit(interest)
    return f"Interest added: {interest}. New balance: {self.balance}"

  def __str__(self):
    return f"SavingsAccount(owner: {self.owner}, balance: {self.balance}, interest_rate: {self.interest_rate})"
