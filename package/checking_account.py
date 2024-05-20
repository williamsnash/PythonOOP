from .bank_account import BankAccount


class CheckingAccount(BankAccount):
  def __init__(self, owner, balance=0.0, overdraft_limit=100.0):
    super().__init__(owner, balance)
    self.overdraft_limit = overdraft_limit

  def withdraw(self, amount):
    if 0 < amount <= self.balance + self.overdraft_limit:
      self.balance -= amount
      return f"Withdrew {amount}. New balance: {self.balance}"
    return "Overdraft limit exceeded or invalid amount"

  def __str__(self):
    return f"CheckingAccount(owner: {self.owner}, balance: {self.balance}, overdraft_limit: {self.overdraft_limit})"
