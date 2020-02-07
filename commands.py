



# BUDGET FUNCTIONS
def show_commands():
    """ Prints all the arguments available and what they do """
    print("Showing all arguments for the Budget application: ")
    print("  --helpme                        Shows all the argument options")
    print("  --init                          Initiates a new budget with following commands")
    print("  --new <labeL>                   Adds a new label to current budget")
    print("  --delete <label>                Removes label from current budget")
    print("  --show                          Shows budget as a pandas dataframe")
    print("  --labels                        Shos labels, ie Food, Snacks, Cinema, Taxis, Clothing")
    print("  --add <amount> <label>          Adds <amount> into <label> for current month/date/year")
    print("  --sub <amount> <label>          Subtracts <amount> from <label> for current month/date/year")
    print("  --undo                          Undos the latest command made")

def init():
    pass

def new(label):
    pass

def delete(label):
    pass

def show(mode):
    # Check if mode is 'FULL', 'DAY', 'MONTH', 'YEAR'
    pass

def add(amount, label):
    """ Adds amount to specific label """
    # if db.find_label(label):
    #       add <amount> to label in json
    print("TBD execution of <def add()>")

def sub(amount, label):
    """ Removes amount from specific label """
    # if db.find_label(label):
    #       subtract <amount> from label in json
    print("TBD execution of <def sub()>") 

def undo():
    # Undo last command
    pass



