from package import account_factory

if __name__ == "__main__":
  account = account_factory(
      'savings',
      'Rolf',
      balance=100000.0,
      interest_rate=0.05)
  print(account)
