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
# ... $ python3 budget.py new <category> <label>        (Adds a new label to current budget)
# ... $ python3 budget.py del <category> <label>        (Removes label from current budget)
# ... $ python3 budget.py show                          (Shows budget as a pandas dataframe)
# ... $ python3 budget.py labels                        (Shos labels, ie Food, Snacks, Cinema, Taxis, Clothing)
# ... $ python3 budget.py add <amount> <label>          (Adds <amount> into <label> for current month/date/year)
# ... $ python3 budget.py sub <amount> <label>          (Subtracts <amount> from <label> for current month/date/year)
# ... $ python3 budget.py undo                          (Undos the last used command)
# TODO: Add a way to 'activate' your budget for data manipulation
# TODO: Add "manage" argument to change name of labels (ie $ python3 budget.py manage Hone Home)


# ***** FUTURE DEVELOPMENTS *****
# TODO Store in database rather than local 
# TODO Function: refactor current amount on x label for y date
# TODO Add an Exception Handler for custom exceptions (see Exception hook below)
# TODO Extract json to csv (view budget as table)
# TODO Configure threshold of each label (what to spend each month)
# TODO Get profits/losses, summaries, etc.
# TODO Show graphs and plots (numpy, matplotlib)
# TODO Add support for different currencies
# TODO Add "$ python3 budget.py download" to download a pdf with your budget statistics

# IMPORTS
import sys
import os
import commands                                         # Includes commands for above stated CLI commands
import argparse
import calendar
import itertools
from datetime import datetime

class Budget():
    id_iter = itertools.count()
    def __init__(self, name, income_s, expense_s, month, year):
        self.id = next(self.id_iter)
        self.name = name
        self.stable_incomes = income_s
        self.stable_expenses = expense_s
        self.current_month = month
        self.year = year
        self.months = [month.lower() for month in calendar.month_name if month]

# Exception hook
# https://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
def exception_handler(exception_type, exception, traceback):

    if exception_type == Exception:
        # TODO: Get error message from Exception Handler 
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
        # TODO: Make several budgets for each year (make it possible)

        year = datetime.now().year
        month = datetime.now().month

        PATH = f"budgets/budget_{year}.json"

        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            # checks if file exists
            answer = input(f"'/budget_{year}.json' already exists. Override? [y]/[n]: ")
            if answer.lower() == "y":
                print(f"'/budget_{year}.json' is about to be overriden. Press ctrl+C to cancel.")
                budget_name = input(" >>> Name your new Budget: ")

                _income_label = set([x.replace(',', '').lower() for x in input(" >>> Set INCOME labels ('salary, loan' etc): ").split()])
                _expenses_label = set([x.replace(',', '').lower() for x in input(" >>> Set EXPENSE labels ('rent, phone, spotify' etc): ").split()])

                incomes = { label : int(input(f" >>> Fixed income of {label}: ")) for label in _income_label }
                expenses = { label : int(input(f" >>> Fixed expense of {label}: ")) for label in _expenses_label }


                budget = Budget(budget_name, incomes, expenses, month, year)
                commands.init(budget)
            elif answer.lower() == "n":
                print(f"'/budget_{year}.json' kept default values. Application terminated.")
            else:
                print("No matching input: Application terminated.")
        else:
            print("No file with that name exists.")
    elif args.new:  
        if len(args.new) != 2:
            #raise Exception('Please use correct syntax: --new <category> <label>') 
            print('ERROR: Please use correct syntax: --new <category> <label>')
        else:
            cat = args.new[0].lower()
            lbl = args.new[1].lower()


            commands.new(lbl, cat)


    elif args.delete:
        commands.delete(args.delete)
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

    # TODO: add more arguments + fix arguments
    parser = argparse.ArgumentParser(description="Create a CLI Budget Scheme")
    parser.add_argument("--helpme", help="Shows all the argument options", action="store_true")   # Adds argument for "help" command
    parser.add_argument("--init", help="Initiates a new budget", action="store_true")
    parser.add_argument("--new", nargs="*", help="Adds a new label to current budget")
    parser.add_argument("--delete", nargs="*", help="Removes a label from current budget")
    parser.add_argument("--show", help="Shows budget as a pandas dataframe") 
    parser.add_argument("--labels", help="Shows all labels in current budget", action="store_true") 
    parser.add_argument("--add", nargs="*", help="Adds <amount> into <label> for current month/date/year") 
    parser.add_argument("--sub", nargs="*", help="Subtracts <amount> from <label> for current month/date/year")
    parser.add_argument("--undo", help="Undos the latest command made", action="store_true") 

    # Check if arg has 'action="store true"' or not >>> *args/**kwargs

    args = parser.parse_args() 

    # TODO BUG: check if min 1 arg for nargs="*" arguments (argparse has no built in func)

    main(args)
