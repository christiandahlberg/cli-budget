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
# ... $ python3 budget.py undo                          (Undos the last used command)


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

def main(args):
    sys.excepthook = exception_handler  # Change?

    # TODO Send args to command module function (acknowledge what command to use)
    # TODO Add more conditions and fix actions/placeholders

    if args.helpme:
        commands.show_commands()
    elif args.init:

        # ------------------------------- CONTINUE ON THIS ------------------------------------

        # Create budget framework (for specific years?)
        # Setup labels for dynamic income and expenses
        # Setup stable incomes dictionary {"CSN": 13000, "Tenant": 9300, "Salary": 4000} etc
        # Setup stable expenses dictionary {"Rent": 3500, "Phone Bill": 500, "Spotify": 49} etc

        _income_label = set([x.replace(',', '').title() for x in input("Set INCOME labels (salary, loan etc): ").split()])
        _expenses_label = set([x.replace(',', '').title() for x in input("Set EXPENSE labels ('rent, phone, spotify' etc): ").split()])

        incomes = { label : input(f"{label}: ") for label in _income_label }
        expenses ={ label : input(f"{label}: ") for label in _expenses_label }

        print("Income --------------------")
        for k, v in incomes.items():
            print(f" >>> {k}: {v}")
        print("Expense -------------------")
        for k, v in expenses.items():
            print(f" >>> {k}: {v}")

    elif args.new:
        print(f"Added label (placeholder): {args.new}")
    elif args.delete:
        print(f"Removed label (placeholder): {args.delete}")
    elif args.show:
        mode = args.show    # Check if mode is 'FULL', 'DAY', 'MONTH', 'YEAR' 
        commands.show(mode)
    elif args.labels:
        pass
    elif args.add:
        if len(args.add) != 2:
            raise Exception('Please use correct syntax: --add <amount> <label>') 
        amount = int(args.add[0])
        label = args.add[1]

        # budget.add(amount, label)       # TODO: Add error handling to know if it's amount or label
        if commands.add(amount, label):
            print(f"Successfully added {amount} to {label}")
            # TODO: Add 'current balance / blabla'       
    elif args.sub:
        if len(args.sub) != 2:
            raise Exception('Please use correct syntax: --sub <amount> <label>')  
        amount = int(args.sub[0])
        label = args.sub[1]

        # budget.sub(amount, label)       # TODO: Add error handling to know if it's amount or label
        if commands.sub(amount, label):
            print(f"Successfully removed {amount} from {label}")
            # TODO: Add 'current balance / blabla'  
    elif args.undo:
        pass
    else:
        pass # Will never reach this stage
            



if __name__ == "__main__":
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
    parser.add_argument("--sub", nargs="*", help="Subtracts <amount> from <label> for current month/date/year")
    parser.add_argument("--undo", help="Undos the latest command made", action="store_true") 

    # Check if arg has 'action="store true"' or not >>> *args/**kwargs

    args = parser.parse_args() 

    # TODO BUG: check if min 1 arg for nargs="*" arguments (argparse has no built in func)

    main(args)
