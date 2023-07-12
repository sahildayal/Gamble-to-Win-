def deposit():
    while True:
        amount = input("What would you liek to deposit? $")
        if amount.isdigit(): #we use isdigit because if they put negative it wont regit it so it takes care of that as well
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("AMount must be greater than 0.")
        else:
            print("Please enter a number!")

    return amount

