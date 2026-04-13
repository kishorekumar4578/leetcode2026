balance=50000;
withdraw_amount = int(input("Enter the amount to withdraw: "));
if withdraw_amount > balance:
    print("Transaction Failed: Insufficient balance.");
elif withdraw_amount % 100 != 0:
    print("Transaction Failed: Amount must be a multiple of 100.");
else:
    balance -= withdraw_amount
    print("Transaction Successful!")
    print(f"Please collect your cash. Remaining balance: {balance}")
