class BankAccount:
  def __init__(self, owner, balance=0.0):
    self.owner = owner
    self.balance = balance

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      return f"Deposited {amount}. New balance: {self.balance}"
    return "Deposit amount must be positive"

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      return f"Withdrew {amount}. New balance: {self.balance}"
    return "Insufficient balance or invalid amount"

  def get_balance(self):
    return f"Account balance: {self.balance}"

  def __str__(self):
    return f"BankAccount(owner: {self.owner}, balance: {self.balance})"
