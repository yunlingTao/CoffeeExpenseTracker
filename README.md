# Coffee Expense Tracker

The `CoffeeExpenseTracker` is a command-line Python application designed to help coworkers track and manage their coffee expenses. It ensures fair rotation among coworkers when paying for coffee by keeping track of who has paid and suggesting who should pay next, based on the least amount paid so far. It supports tracking expenses for multiple groups, with each group's data stored in its own CSV file.

## Features
- Tracks coffee expenses for multiple groups of coworkers.
- Suggests the next payer based on previous payments.
- Resets all payments to zero once everyone within the group has paid the same amount.
- Stores payment history and group-to-csv mapping using CSV and JSON files. 

## Setup 
1. Clone this repository or download the `CoffeeExpenseTracker.py` and `NameToCSVMapping.json` files to your preferred directory. 
2. Ensure you have Python 3.x installed on your system.

# Usage
Follow the steps below:
1. Open your terminal or command prompt and navigate to the directory containing the downloaded script and JSON file. 
3. Run the script using:
    ```
    python CoffeeExpenseTracker.py
    ```
4. When prompted, enter the names of the coworkers in your group, separated by commas. For example
    ![alt text](image.png)
    - If the group is new, you'll be prompted to provide a CSV filename for tracking expenses. If the group already exists, the script will automatically use the associated CSV file.
    - If only one name is provided, you will be prompted to provide more names.
5. Enter the total coffee price for today when prompted. 
    - If the total coffee price is less than or equal to 0, then you will be prompted to provide a positive number. 
6. The script will then suggest which coworker should pay next based on the previous payments.
    - If it is the first time running the script, it will create a CSV file named 'CoffeePayments.csv' with all coworkers' names and initialize their payments to zero. 
    - `CoffeeExpense.csv` is an example. 
6. The script will update the CSV file based on the suggested coworker. 

## Customization

1. Different groups: To manage a different group of coworkers, simply run the script again and enter the new group's names when prompted. 

2. Data Modification: Directly edit the NameToCSVMapping.json or CSV files if manual adjustments are needed. 

## Assumptions
1. Checkout Total Only: The script is designed for use during the checkout process. It accepts the total coffee expense for the day and does not account for the individual prices of each coffee purchase.
1. Case Sensitivity: All names are converted to lowercase. The script assumes that case variations are irrelevant. For example, 'Alice' is considered the same as 'ALIce'. 
2. No Duplication in Names Within a Group: The script removes duplicates and assumes that users follow the instructions. 
3. Unique Groups: Unique groups are identified based on a sorted, comma-separated string of names. It assumes that users input names with commas and have no spelling mistakes.
4. Concurrent Access: The script is not intended for simultaneous access by multiple users in a shared environment.
5. Manual Editing: The script assumes that the JSON and CSV files it reads from and writes to are accessible, correctly formatted, and not corrupted. 
