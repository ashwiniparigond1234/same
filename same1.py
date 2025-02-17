current_Bal=100000
withdrawal=int(input("enter the amout for withdrawal: "))
if withdrawal<=current_Bal:
    balance=current_Bal-withdrawal
    print("allow the transaction ")
    print(balance)
else:
    print("insufficient balance")    