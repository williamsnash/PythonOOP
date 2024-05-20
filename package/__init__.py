from .bank_account import BankAccount
from .savings_account import SavingsAccount
from .checking_account import CheckingAccount


def account_factory(account_type, owner, balance=0.0, **kwargs):
  account_classes = {
      'basic': BankAccount,
      'savings': SavingsAccount,
      'checking': CheckingAccount
  }
  if account_type in account_classes:
    return account_classes[account_type](owner, balance, **kwargs)
  else:
    raise ValueError(f"Unknown account type: {account_type}")
