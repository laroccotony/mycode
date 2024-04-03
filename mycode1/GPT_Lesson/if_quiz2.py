account_balance = 29

if account_balance > 0:
    print("Your account is in good standing.")
elif account_balance == 0:
    print("Your account is empty.")
elif account_balance < 0 and account_balance >= -100:
    print("Your account is overdrawn, but you can still use overdraft protection.")
else:
    print("Your account is significantly overdrawn! Immediate action required.")
