
# Case Bulk loader
This project contains scripts for creating test data to load case data directly into the Postgres Database.

The code is in two parts to allow the creation of the data and the load of the data to be run independently.

## Create CSVs

The createcsv.py program will create data for loading into the case and action service.

Case schema

case.csv

casegroup.csv

caseevents.csv

Action schema

actionplan.csv

actionrule.csv

actiontype.csv


The number of cases to be generated can be configured by changing the value of the total_records variable within the code.

One action plan is created with one rule to create initial contact letters with a handler of printer. The rule is set to run one hour from file creation time. This can be configured by changing the future_time variable within the code.

# Load Data
The loadcases.py program will load the CSVs created into the relevant Postgres tables. The data in the tables is cleared before the new data is loaded.

NOTE: No IACs will be created as the case delivery queue is bypassed.

## Setting up the python environment
```
brew install pyenv
pyenv install
pip install --upgrade pip setuptools pipenv
pipenv install --dev
pip3 install psycopg2
```

## Running the procedures

To test the script locally you must have the relevant RM services running
```
pipenv shell
python createcsvs.py
python loadcases.py
```