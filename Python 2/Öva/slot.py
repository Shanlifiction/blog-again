import random #need to generate the slot machine values randomly 

MAX_LINES = 3 #global constant (good if number of lines will be changed later on, the program will update correctly)
MAX_BET = 100
MIN_BET = 1

ROWS = 3 #number of rows for the slot machine
COLM = 3 #number of column for the slot machine

symbol_count = { #{} make a dictionary
    "A": 2, #A highest value so only 2 A's in each reel and so on...
    "B": 4,
    "C": 6,
    "D": 8
}
#how many symbols in (every singel) reel/each column?
#need values for the different symbols

#how many symbols in total?
#and what should the symbols be?

symbol_value = { #{} make another dictionary (for def "check winnings" below)
    "A": 5, #the more rare the symbol is, the higher the bet get multiplied
    "B": 4,
    "C": 3,
    "D": 2
}

#check_winnings is fairly advanced logic (in terms of looking  through rows and columns AND nested lists) 
def check_winnings(columns, lines, bet, values): #to determine how much player won
    winnings = 0
    winning_lines = []
    for line in range(lines): #looping through every row, cheching how many lines player bets on ex. 1 (would be 0), if 2 (would be 0 and 1) etc
        symbol = columns[0][line] #symbols equal to (first) column [0] at the current line, bec need to look at the first column where the first symbol is (for each row) bec to win all the symbols need to be the same
        for column in columns: #(knowing the symbol to check) need to loop through every singel column and check for that symbol
            symbol_to_check = column[line] #the symbol to check (look for) is equal to the column in (looking at [line 0, 1, 2 etc]) current row
            if symbol != symbol_to_check: #check if symbol is NOT equal to the symbol "to check", then break
                break #go loop again to check the next line (bec symbols where not the same)
            else: #if player did not break out of the for loop else statement will be executed (yes possible to put an else statement following a for loop)
                winnings += values[symbol] * bet #if symbol is same as the symbol to check for then its a WIN!
                                                #won whatever is multiplied for that symbol * players bet (on each line, not the total bet)
                                                #meaning its possible to win on one line and loose on another line
                winning_lines.append(line + 1) #add one to it bec this is an index, need to present from 1, not 0

        return winnings, winning_lines #returning two values, the total amount player won and which line player won on

def get_slot_machine_spin(rows, cols, symbols): #three parameters that pass info to this funtion
#inside the function generate what symbols are gonna be in each column (based on the frekvency above (symbols_count)) 
#randomly picking number of rows inside each column
#create a list
    all_symbols = [] #all symbols list
    for symbol, symbol_count in symbols.items(): #item() give both the key (symbol ex. A) and the value (symbols_count ex. 2) associated with the dictionary
        for _ in range(symbol_count):           #rather than only getting the keys and having to manually referencing the values
            all_symbols.append(symbol)          #_ is an anonumos variable in Python used when dont care of the count or the iteration value (so there is no unused variable)

#list check, now need to select the values for every singel column with a for loop that that does this for every column
    #start by defining a columns list:
    columns = []  #nested list tipically [0, 0], [0, 1], [0, 2] etc. but in this case we are storing the columns, and not the rows ([], [], [] (leaving them empty))
    for _ in range(cols): #each column need to generate a value (how many rows there is (ex. 3), thats how many) inside of every singel column
        #col
        column = [] #empty list (to generate randomized values for each column/row)
        current_symbols = all_symbols[:] #[:] (aka the slice operator) copy the all_symbols list, so that the values do not repeat
        for _ in range(rows): #loop through the nr of values that need to be generated (equal to the nr of rows in the slot machine)
            #row
            value = random.choice(current_symbols) #select a certain (random) number of values choosen from the all_symbols list (random possible thx to import)
                                                                                        #(thx to slice [:]) "all" changed to: current_symbols list
            current_symbols.remove(value) #removes the used value (to not pick it agian) 
            column.append(value) #add the value to the column 
                                #and when all values are given, all rows should have symbols inside the column
        
        columns.append(column) #lastly, adding the column to the columns list
        #above will be looped as many columns that need to be generated and the nestled loop inside picks random value for each row 
    return columns #finally return the columns
#this list check and for loops are how the items in the slot machine will be generated 

#to print the above in a nice way:
def print_slot_machine(columns): #instead of printing the items horisontally, need to print them vertically 
                                #but how do we loop through every row and only print the first value to make this change?
    #loop through every single row:
    for row in range(len(columns[0])): #the number of rows is the nr of elements in the columns (number of vertical spaces befintliga). Look at a column and get the lenght of that
                    #assums there is at least a column
                    #looping through all items inside the columns, giving every individual column
                    #continuing with looping through every single column in the row
                    #for every colum, loop through but only printing the "current row":
        for i, column in enumerate(columns): #only print the (first?) value in whatever index of the current row is
            if i != len(columns) - 1: #if i is not equal to the maximum index (to access an element in the columns list), if this is correct then pipe will be printed
                print(column[row], end=" | ") #pipe to separate values, but to not have one in the end changes made in the
            else:                       #for loop from: "for column in columns:" to i and enumerate to give the index 0, 1 ,2 when looping through, as well as the item
                print(column[row], end="") #pipe wont printed
                                    #end tells teh print statement what to end the line with, similar to "\n" (the new line character)
                                    #not possible to use in this case bec backslash will tell to move to next line after every singel column
                                    #not suited here bec need new line after every row, and not column
        print() #to print a inbetween nada (new line character)

def deposit(): #function deposit
    while True: #while loop until break and lead to "return amount" below this codeblock
        amount = input("How much would you like to deposit? €")
        if amount.isdigit(): #if input is digit
            amount = int(amount) #then the amount will be turned into an integer
            if amount > 0: #check is input is greater than zero
                break #if it is a valid amount the program will break out of the loop
            else:
                print("Amount must be greater than 0.") #otherwise this will be printed out to try again
        else:
            print("Please type a number.") #or this will be printed until the program gets a number and then break out of the loop

    return amount

def get_nrlines():
    while True: #while loop until break and lead to "return amount" 
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit(): #if input is digit
            lines = int(lines) #then the lines will be turned into an integer
            if 1 <= lines <= MAX_LINES: #check if input is greater than 1 and less than maximun amount of lines
                break #if so the program will break out of the loop
            else:
                print("Enter a valid number of lines.") #otherwise this will be printed out to try again
        else:
            print("Please type a number.") #or this will be printed until the program gets valid number and then break out of the loop

    return lines

def get_bet():
    while True: #while loop until break and lead to "return amount" (line14)
        amount = input("How much would you like to bet on each line? €")
        if amount.isdigit(): #if input is digit
            amount = int(amount) #then the amount will be turned into an integer
            if MIN_BET <= amount <= MAX_BET: #check is input is greater than zero
                break #if it is a valid amount the program will break out of the loop
            else:
                print("Amount must be between " + str(MIN_BET) + " and " + str(MAX_BET) + ".") #otherwise this will be printed out to try again
                #print(f"Amount must be between €{MIN_BET} - €{MAX_BET}.") #possile to write it this way too
        else:
            print("Please type a number.") #or this will be printed until the program gets a number and then break out of the loop

    return amount

#deposit() #calling the function

def gamespin(balance): #making it possible to run the game more than once after the deposit is declaired #added (balance) to pass balance into gamespin function
    #the (copied) codeblock below will executes one game:
    lines  = get_nrlines()
    while True: #loop to check if the bet amount is within the range of their deposit
        bet = get_bet()
        #if 
        total_bet = lines * bet
        if total_bet > balance: #thx to the pass (balance add to the function)
            print(f"You do not have enough to bet that amount, your current balance is €{balance}.")
        else:
            break

    print(f"You are betting €{bet} on {lines} lines. Total bet is equal to: €{total_bet}") #printing a summary of action above
    #print(balance, lines) #was printed half-way through the basic structure

    slots = get_slot_machine_spin(ROWS, COLM, symbol_count) #should have all columns (called slots here) in the slots spin
    print_slot_machine(slots) 
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) #determine and print the winnings for the player
    print (f"You won! €{winnings}.")
    print (f"You won on lines:", *winning_lines) #using * is the splat or unpack operator, which passes every singel line from the wininng_lines list to this print function
    return winnings - total_bet #will tell how much the player won or lost from this gamespin (ex. if win: the win - the bet amount)
                                                                                                #(ex. if lost: no win - "negative" bet amount)
                                                                                                #(subratcted from the balance deposit amount)

def main(): #so if program is ended possible to call the function again and rerun the program
    balance = deposit()
    while True:
        print(f"Current balance is €{balance}")
        #input("Press eneter to spin") #if no value nedded bec does not matter what the player press/"enters"
        answer = input("Press enter to play (q to Quit).") 
        if answer == "q": #end game and break
            break
        balance += gamespin(balance) #spin returns info about how much the player won/lost AND tell the player AND update the balance 
                        #based on the result of the spin and then run the whileTrue loop above again
    print(f"You left with €{balance}")

    #since the deposit (above) will stay the same but the rest of the program will most likely run several times lets copy the below part into a function
    # lines  = get_nrlines()
    # while True: #loop to check if the bet amount is within the range of their deposit
    #     bet = get_bet()
    #     #if 
    #     total_bet = lines * bet
    #     if total_bet > balance:
    #         print(f"You do not have enough to bet that amount, your current balance is €{balance}.")
    #     else:
    #         break

    # print(f"You are betting €{bet} on {lines} lines. Total bet is equal to: €{total_bet}") #printing a summary of action above
    # #print(balance, lines) #was printed half-way through the basic structure

    # slots = get_slot_machine_spin(ROWS, COLM, symbol_count) #should have all columns (called slots here) in the slots spin
    # print_slot_machine(slots) 
    # winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value) #determine and print the winnings for the player
    # print (f"You won! €{winnings}.")
    # print (f"You won on lines:", *winning_lines) #using * is the splat or unpack operator, which passes every singel line from the wininng_lines list to this print function

main() #calling main so that program will start running on main