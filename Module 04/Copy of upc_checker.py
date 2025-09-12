# UPC-A Checksum Validation Program
# Author: Brett Day
# Course: SDEV 140 (Intro to Software Development)
# Fall 2025 - Project Due 9/21

# Description
# This program is an interactive console style program that validates 12-digit UPC codes.
# This program validates UPC-A codes by calculating the "check" digit and comparing it to the supplied "check"

# This program demonstrates: 
# Basic I/O
# Variables
# Lists
# Basic Looping
# Conditionals
# Functionals
# Basic Error Handling

# Usage: Run the "upc_checker.py" program, and follow the prompt. Find a valid 12-digit UPC-A barcode. 
# The program will report whether the UPC is valid, and if it's invalid, why it's invalid. 

# Use this line for debugging purposes only. Comment out when not in use. 
# I made this because I was fixing some formatting stuff and I couldn't tell 
# If the program was the current version. 
'''
print("Running the Latest Version\n")
'''
# Step 1: Sum Odd-Position Digits (1,3,5,7,9,11)
def calculate_check_digit(upc):
    odd_sum = 0
    even_sum = 0

# Only looks at the first 11 digits.
    for i in range(11): 
        digit = int(upc[i])
        if (i + 1) % 2 == 1:
            # Odd Positions
            odd_sum += digit
        else:
            # Even Positions
            even_sum += digit
            
# Step 2: Multiple the Odd Sum by 3 and Add the Even Sum. 
    total = (odd_sum * 3) + even_sum
    remainder = total % 10

# Step 3: Calculate the Remainder and Check the Digit
   
    if remainder == 0:
        return 0
    else: 
        return 10 - remainder

# Step 4: Body of Main Program. The above logic allows this program to run. 
def main():
    
    print("|*~==================================~*|")
    print("| Brett Day's UPC-A Checksum Validator |")
    print("|*~==================================~*|\n")

    print("Please Enter a 12-Digit UPC (Press Q to quit!)\n")
    #"\n" Is a linebreak, which moves the users cursor to the beginning of the next line. 
    #"\n" Will be used for this section, since the user will be inputting information. 4
    
    while True: 
        upc = input("UPC> ").strip()

        if upc.lower() in ["q", "quit", "exit"]:
            # This line allows for the user to exit the program. 
            print("Seeya Later, Alligator!")
            break
        # Makes sure the provided input is valid. 
        if len(upc) != 12:
            print("Error: The provided UPC must be exactly 12 digits.\n")
            continue
        if not upc.isdigit():
            print("Error: The UPC may only contain numbers.")
            continue
        # Here is where the check digit (checksum) is calculated. 
        supplied = int(upc[-1]) # "[-1]" is the last digit of the UPC, known as the "checksum"
        computed = calculate_check_digit(upc)

        if upc == "666908016460" and supplied == computed: 
            print("Ah, a classic. Analord 2 by Aphex Twin, an Acid Techno staple.")
            print("Track 1, 'Phontacid', is a nearly 9-minute long masterpiece, a modern electronic masterpiece.")
            print("Not to mention track 4, 'Bwoon Dub', which has blown out subwoofers since 2005.")
            print("I'm also pleased to inform you that this UPC is valid.")
        elif supplied == computed:
            print("Valid UPC!\n")
        else: 
            print("Sorry! Your UPC is invalid! Bad check digit:", supplied)
            print("Sorry! Your UPC is invalid! Expected to see check digit: ", computed, "\n")

if __name__ == "__main__":
    main()
## Begin more fun here 