# Budget Application
# .
# .
# Version: v1.01
# Author: Christian Dahlberg


# ***** LAST STEP *****
# TODO: 1) pip3 freeze > requirements.txt
# TODO: 2) Pin depencies
# TODO: 3) Add requirements.txt to root 

# ***** COMMANDS *****
# ... $ python3 budget.py --helpme                      (Shows all commands)
# ... $ python3 budget.py init                          (Initiates a new budget with following commands)
# ... $ python3 budget.py new <labeL>                   (Adds a new label to current budget)
# ... $ python3 budget.py del <label>                   (Removes label from current budget)
# ... $ python3 budget.py show                          (Shows budget as a pandas dataframe)
# ... $ python3 budget.py labels                        (Shos labels, ie Food, Snacks, Cinema, Taxis, Clothing)
# ... $ python3 budget.py add <amount> <label>          (Adds <amount> into <label> for current month/date/year)
# ... $ python3 budget.py sub <amount> <label>          (Subtracts <amount> from <label> for current month/date/year)


# ***** FUTURE DEVELOPMENTS *****
# TODO Store in database rather than local 
# TODO Function: refactor current amount on x label for y date
# TODO Add an Exception Handler for custom exceptions (see Exception hook below)
# TODO Extract json to csv (view budget as table)

# IMPORTS
import sys
import commands                                         # Includes commands for above stated CLI commands
import argparse

# Exception hook
def exception_handler(exception_type, exception, traceback):
    if exception_type == Exception:
        print('ERROR: Please use correct syntax: --add <amount> <label>')
    else:
        sys.__excepthook__(exception_type, exception, traceback)

# BUDGET FUNCTIONS

# Adds amount to specific label
def add(amount, label):
    # if db.find_label(label):
    #       add <amount> to label in json
    print("TBD execution of <def add()>")




def main(args):
    sys.excepthook = exception_handler  # Change?

    # TODO Send args to command module function (acknowledge what command to use)

    # TODO Add more conditions and fix actions/placeholders
    if args.helpme:
        print("Showing all arguments for the Budget application: ")
        print(" >>> --helpme                        (Shows all the argument options)")
        print(" >>> --init                          (Initiates a new budget with following commands)")
        print(" >>> --new <labeL>                   (Adds a new label to current budget)")
        print(" >>> --delete <label>                (Removes label from current budget)")
        print(" >>> --show                          (Shows budget as a pandas dataframe)")
        print(" >>> --labels                        (Shos labels, ie Food, Snacks, Cinema, Taxis, Clothing)")
        print(" >>> --add <amount> <label>          (Adds <amount> into <label> for current month/date/year)")
        print(" >>> --sub <amount> <label>          (Subtracts <amount> from <label> for current month/date/year)")
    elif args.init:
        print("placeholder")
    elif args.new:
        print(f"Added label (placeholder): {args.new}")
    elif args.delete:
        print(f"Removed label (placeholder): {args.delete}")
    elif args.labels:
        print("placeholder")
    elif args.add:
        if len(args.add) != 2:
            raise Exception('Please use correct syntax: --add <amount> <label>')
        else:
            amount = int(args.add[0])
            label = args.add[1]
            
            # budget.add_amount(amount, label)       # TODO: Add error handling to know if it's amount or label
            if add(amount, label):
                print(f"Successfully added {amount} to {label}")
                # TODO: Add 'current balance / blabla'

            

    # Add dates (year, month)
    # Add labels
    # Add stable incomes
    # Add stable expenses

if __name__ == "__main__":
    # TODO Argparse
    # TODO Commands

    # TODO: add more arguments + fix arguments
    parser = argparse.ArgumentParser(description="Create a CLI Budget Scheme")
    parser.add_argument("--helpme", help="Shows all the argument options", action="store_true")   # Adds argument for "help" command
    parser.add_argument("--init", help="Initiates a new budget", action="store_true")
    parser.add_argument("--new", help="Adds a new label to current budget")
    parser.add_argument("--delete", help="Removes a label from current budget")
    parser.add_argument("--show", help="Shows budget as a pandas dataframe", action="store_true") 
    parser.add_argument("--labels", help="Shows all labels in current budget", action="store_true") 
    parser.add_argument("--add", nargs="*", help="Adds <amount> into <label> for current month/date/year") 

    # Check if arg has 'action="store true"' or not >>> *args/**kwargs

    args = parser.parse_args() 

    # TODO BUG: check if min 1 arg for nargs arguments (argparse has no built in func)

    # Init
    main(args)
