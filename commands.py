from budget import Budget
from datetime import datetime
import json
import calendar
import os
import pandas as pd
import numpy as np

MODES = ['full', 'year', 'month']
MONTH = calendar.month_name[datetime.now().month].lower()
ALL_MONTHS = [month.lower() for month in calendar.month_name if month]
YEAR = datetime.now().year
INCOME = "income"
EXPENSE = "expense"

# BUDGET FUNCTIONS
def show_commands():
    """ Prints all the arguments available and what they do """
    print("Showing all arguments for the Budget application: ")
    print("  --helpme                        Shows all the argument options")
    print("  --init                          Initiates a new budget with following commands")
    print("  --new <category> <label>        Adds a new label to current budget in mentioned category")
    print("  --delete <category> <label>     Removes label from current budget in mentioned category")
    print("  --show                          Shows budget as a pandas dataframe")
    print("  --labels                        Shos labels, ie Food, Snacks, Cinema, Taxis, Clothing")
    print("  --add <amount> <label>          Adds <amount> into <label> for current month/date/year")
    print("  --sub <amount> <label>          Subtracts <amount> from <label> for current month/date/year")
    print("  --undo                          Undos the latest command made")

def init(Budget):
    current_budget = Budget

    # Add name/year to budget?
    data = {
        month: {
            INCOME: {
                label: value
                for label, value in current_budget.stable_incomes.items()
            },
            EXPENSE: {
                label: value
                for label, value in current_budget.stable_expenses.items()
            }
        }
        for month in current_budget.months
    }

    with open(f'budgets/budget_{current_budget.year}.json', 'w', encoding='utf-8') as fp:
        json.dump(data, fp, ensure_ascii=False, indent=4) 

    print(f"Successfully created budget '{current_budget.name}'. (PATH '/budgets/budget_{current_budget.year}.json')")
        

def new(label, category):
    with open(f"budgets/budget_2020.json", "r") as file:
        data = json.load(file)
    
    if find_label(label, data, category):
        print(f"A label with that name ({label}) already exists. ")
        print(f"Use: '$ python3 budget.py manage <old_label> <new_label>' to change its name.")
    else:
        for m in ALL_MONTHS:
            data[m][category][label] = 0

        # TODO: Dynamic budget "budget_{current_budget.year}.json"
        with open(f'budgets/budget_2020.json', 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4) 

def delete(label):
    with open(f"budgets/budget_2020.json", "r") as file:
        data = json.load(file)

    category = find_category(label, data)

    if find_label(label, data, category):
        del data[MONTH][category][label]
        print(f"Successfully deleted {label} from your Budget.")
    else:
        print(f"Sorry! Couldn't find a label named {label} in your budget.")


def show(mode):
    # Check if mode is 'FULL', 'DAY', 'MONTH', 'YEAR'
    if mode not in MODES:
        print("Can only show data from _ by year, month or full.")
    else:

        ############ CONTINUE HERE ##############

        # Fetch data
        with open(f"budgets/budget_2020.json", "r") as file:
            data = json.load(file)


        # Convert data
        df_all = pd.DataFrame.from_dict({(i,j): data[i][j] 
                           for i in data.keys() 
                           for j in data[i].keys()},
                       orient='index')

        # Clean data
        df_all[np.isnan(df_all)] = 0
        df_all = df_all.rename(index={EXPENSE:INCOME}, level=1).fillna(0).groupby(level=[0,1]).sum()
        df_all = df_all.reset_index()
        df_all = df_all.reindex([4, 3, 7, 0, 8, 6, 5, 1, 11, 10, 9, 2])
        del df_all["level_1"]
        df_all = df_all.reset_index(drop=True)
        df_all.columns.values[0] = "month"
        df_all.set_index('month')

        # Add column with summary
        pos = [data[k][INCOME] for k, v in data.items()]
        neg = [data[k][EXPENSE] for k, v in data.items()]

        # Prepare current sum 
        pos_list = [sum([dictio[key] for key in dictio]) for dictio in pos]
        neg_list = [sum([dictio[key] for key in dictio]) for dictio in neg]

        _sum = [a_i - b_i for a_i, b_i in zip(pos_list, neg_list)]

        # Add sum column to table
        df_all['Summary'] = _sum

        # Show data
        print(df_all)

def add(amount, label):             
    """ Adds amount to specific label """
    with open(f"budgets/budget_2020.json", "r") as file:
        data = json.load(file)

    # TODO BUG: What if same Label in both categories?
    category = find_category(label, data)

    if find_label(label, data, category):
        # FOUND LABEL
        data[MONTH][category][label] += amount
        print(f"Added {amount} SEK to {label} ({category}).")
        print(f"Current {category} for {MONTH.title()}: {data[MONTH][category][label]}")

        # TODO: Dynamic budget "budget_{current_budget.year}.json"
        with open(f'budgets/budget_2020.json', 'w', encoding='utf-8') as fp:
            json.dump(data, fp, ensure_ascii=False, indent=4)
    else:
        # DIDNT FIND LABEL
        print(f"Couldn't find a label with name '{label}''. Did you spell right?")
        print(f"Use: '$ python3 budget.py --new <label> <category (Income/Expense)>' to add a new label.")

def sub(amount, label):
    """ Removes amount from specific label """
    # if db.find_label(label):
    #       subtract <amount> from label in json
    print("TBD execution of <def sub()>") 

def undo():
    # Undo last command
    pass

# OTHER FUNCTIONS

def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield dictionary
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if isinstance(d, dict):
                    for result in find(key, d):
                        yield result

def find_label(label, data, category):
    for key in data.keys():        
        if key == MONTH:
            return find_label(label, data[key], category)
        elif key == category:
            return find_label(label, data[key], category)
        elif key == label:
            return True

def find_category(label, data):
    for key in data.keys():        
        if key == MONTH:
            return find_category(label, data[key])
        elif label in data[key]:
            return key