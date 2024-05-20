from abc import ABC, abstractmethod

class BankAccount(ABC):

  @abstractmethod
  def get_balance(self):
    pass

  @abstractmethod
  def deposit(self, amount):
    pass

  @abstractmethod
  def withdraw(self, amount):
    pass


class SavingsAccount(BankAccount):
  def __init__(self, owner, balance=0.0, interest_rate=0.05):
    self.owner = owner
    self.balance = balance
    self.interest_rate = interest_rate

  def get_balance(self):
    return f"Account balance: {self.balance}"

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

  def add_interest(self):
    interest = self.balance * self.interest_rate
    self.balance += interest
    return f"Added interest: {interest}. New balance: {self.balance}"

  def __str__(self):
    return f"SavingsAccount(owner: {self.owner}, balance: {self.balance}, interest_rate: {self.interest_rate}"
  

class Bad(BankAccount):
  def get_balance(self):
    return super().get_balance()

r = SavingsAccount("Rolf")
print(r)

b = Bad()
print(b)