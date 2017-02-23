#  Created by Bradley Ruck on 2/18/17.
#  Copyright © 2016 Bradley Ruck. All rights reserved.
#  Latest modification date 2/18/17.
#
#  Program that recursively finds all solutions for making change from
#  a user entered amount in US cents.  The user is asked if only the unique
#  solutions are to be printed (in ascending order - based on total coins
#  required to make the change). Otherwise, all recursive solutions are
#  printed in ascending order. Coins available to make change are a
#  penny(1), nickel(5), dime(10) and quarter(25).

# Global Variable
totalways = 0

# Function to return the denomination of each coin available
def coins(denomination) :
    if denomination == 1 :
        return 1
    elif denomination == 2 :
        return 5
    elif denomination == 3 :
        return 10
    elif denomination == 4:
        return 25

# Function to recursively solve for all change solutions, returns total number of unique solutions
def ways(amount, i, solutions, coin, answer) :
    global totalways
    if i != amount :
        if i + coins(4) <= amount :
            coin[0] +=1
            ways(amount, i + coins(4), solutions, coin, answer)
            coin[0] -=1
        if i + coins(3) <= amount :
            coin[1] +=1
            ways(amount, i + coins(3), solutions, coin, answer)
            coin[1] -=1
        if i + coins(2) <= amount :
            coin[2] +=1
            ways(amount, i + coins(2), solutions, coin, answer)
            coin[2] -=1
        if i + coins(1) <= amount :
            coin[3] +=1
            ways(amount, i + coins(1), solutions, coin, answer)
            coin[3] -=1
    else :
         # Total number of coins in solution
        coin[4] = coin[0] + coin[1] + coin[2] + coin[3]
         # Test to see if solution already exists, and if user opts for unique solutions
        if coin in solutions and (answer == 'Y' or answer == 'y') :
            return
        else :
            # Add to solution list if not found and/or all solutions are to be printed option
            solutions.append([coin[0], coin[1], coin[2], coin[3], coin[4]])
        totalways +=1       # Increment total number of solutions
    return

def main() :
    counts = 5          # 1,2,3,4 - number of each coin denomination in solution,
                        # 5 - number of total coins in solution
    coin = [0] * counts # Set of coin solution counts
    solutions = []      # Master set of solutions
    global totalways    # Track the amount of solutions calculated

    amount = int(input("Please enter the amount in US currency (in cents) to change: "))

    answer = input('''
Do you want only unique solutions?
Please enter 'Y' for yes or 'N' for no: ''')

    if amount > 0 :
        # starting number of coins in solution
        startcoins = 0
        # Call method to recursively solve for solutions
        ways(amount, startcoins, solutions, coin, answer)
        # Sort solution list by total # of coins in solution ascending order
        sorted_solutions = sorted(solutions, key=lambda x: x[4])
        # Print all saved solutions to screen
        print()
        print("Optimal Combination:", end=" ")
        for i in range(0, len(sorted_solutions)) :
            print("   { %1d Quarters, %2d Dimes, %2d Nickels, %2d Pennies }    Total: %2d coins" %
                  (sorted_solutions[i][0], sorted_solutions[i][1],  sorted_solutions[i][2], sorted_solutions[i][3],
                   sorted_solutions[i][4],))
        if answer == 'Y' or answer == 'y' :
            print()
            print("Total unique coin combinations: ", totalways)
        else :
            print()
            print("Total recursive coin combinations: ", totalways)
    # No change to be made if no initial amount
    elif amount == 0 :
        print('\n', "You have entered no value, there is no change to be made.")
    # Cannot make change from a negative amount
    else :
        print('\n', "You have entered a negative value, please try again.")

main()