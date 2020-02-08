# CLI Budget

A command line Budget application that stores your data in .json files. 

NOTE: Application is still heavily under construction and won't work as of yet.

## Installation

Clone repository. TBD

```bash
TBD
```

## Usage

In this first version, the application will only allow one budget template per year that will include each month and their respective labels.

```python
# Commands that will be available to use to manipulate the budget:
$ python3 budget.py --helpme                       #Shows all commands
$ python3 budget.py --init                           #Initiates a new budget with following commands
$ python3 budget.py --new <category> <label>         #Adds a new label to current budget globally
$ python3 budget.py --delete <category> <label>      #Removes label from current budget
$ python3 budget.py --show                           #Shows budget as a pandas dataframe
$ python3 budget.py --labels                         #Shows labels, ie Food, Snacks, Cinema, Taxis, Clothing
$ python3 budget.py --add <amount> <label>           #Adds <amount> into <label> for current month/date/year
$ python3 budget.py --sub <amount> <label>           #Subtracts <amount> from <label> for current month/date/year
$ python3 budget.py --undo                           #Undos the last used command
$ python3 budget.py --manage <old label> <new label> #Changes the name of one label to something else
```
In later versions, it'll be possible to visualize (and download) the budget statistics by year or month to make comparisons or for personal archive.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
