# Expense Sharing App

## Project Description
A Python-based expense-sharing application that helps multiple users record shared expenses, split bills equally or using custom amounts, calculate balances, and view transaction history.

## Features
- Add and view users
- Record expenses with descriptions and amounts
- Split expenses equally or with custom shares
- Calculate amounts owed and amounts receivable
- View transaction history
- Save and reload records using Pandas and CSV files

## Technologies Used
- Python
- Python lists and dictionaries
- Functions and modules
- Pandas
- CSV file storage

## Requirements
- Python 3
- pip
- Pandas

## Installation
1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Create a virtual environment:

   `python3 -m venv .venv`

4. Activate it on macOS:

   `source .venv/bin/activate`

5. Install dependencies:

   `python -m pip install -r requirements.txt`

## Run the Application
Run:

`python main.py`

Follow the menu to add users, record expenses, view balances, and check transaction history.

## Data Storage
The application creates `data/users.csv` and `data/expenses.csv` when records are saved.

## Limitations
This is a console-based application. It currently stores data locally in CSV files and does not provide login accounts or multi-device synchronization.