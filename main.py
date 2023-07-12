import random 


MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count={
    "A":  2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value={
    "A":  5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #.items will give me both the key and its value
        for _ in range(symbol_count):
            all_symbols.append(symbol) 

    columns = []
    for _ in range(cols):  
        column = []
        current_symbols = all_symbols[:]#slicing it because we need a copy
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slots_machine(columns):
    #transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) - 1 : 
                print(column[row], end=" | ")#tells what to end the line with
            else:
                print(column[row])
        print()



def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #we use isdigit because if they put negative it wont regit it so it takes care of that as well
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")

    return amount

def get_numbers_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit: 
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid no of lines! ")
        else:
            print("Please enter a number!")

    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): #we use isdigit because if they put negative it wont regit it so it takes care of that as well
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a number!")

    return amount
    


def main():
    balance = deposit()
    lines = get_numbers_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines

        if total_bet > balance :
            print(f"You dont have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    print()

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slots_machine(slots)

main()
