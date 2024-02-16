import os
import csv
import json
import random

class CoffeeExpenseTracker:
    def __init__(self, coworkers, totalCoffeePrice, filename):
        self.coworkers = coworkers
        self.totalCoffeePrice = totalCoffeePrice
        self.filename = filename
        
    def initialize_csv(self):
        # if tracking csv file is not created, create with coworker names and total payments for each is 0
        with open(self.filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.coworkers)
            writer.writerow([0]*len(self.coworkers))
        return [0]*len(self.coworkers)
        
    def read_expense(self):
        # read from tracking csv file and get the total payments for each coworker
        with open(self.filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        payments = rows[-1]
        return payments
        
    def suggest_payer(self, payments):
        # randomly select one person who has paid the least
        min_value = min(payments)
        min_idx = [idx for idx, val in enumerate(payments) if val == min_value]
        rand_min = random.choice(min_idx)
        print("It is " + self.coworkers[rand_min] + "'s turn to pay for coffee.")
        return rand_min
    
    def reset_payments(self, rows):
        # if every coworker has paid the same amount, reset all payments to 0
        if len(set(rows[-1])) == 1:
            rows[-1] = ['0' for _ in rows[-1]]
        
        return rows
    def update_payment(self, idx, payments):
        # after suggestion, update paid amount to the paying individual
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
        rows[-1][idx] = str(float(payments[idx]) + self.totalCoffeePrice)

        rows = self.reset_payments(rows)
        
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
    def run(self):
        if os.path.exists(self.filename):
            payments = self.read_expense()
        else:
            payments = self.initialize_csv()
            
        idx = self.suggest_payer(payments)
        self.update_payment(idx, payments)
        
def get_sorted_names():
    # from the command line prompt to get a sorted list of more than one distinct names
    while True:
        names_str = input("Enter names separated by comma (,). Ensure each name is unique, ignoring case differences. Duplicate names will be ignored: ")
        name_list = [name.strip().lower() for name in names_str.split(',')]
        filtered_list = [item for item in name_list if item]
        if len(set(filtered_list)) == 1:
            print("Please provide more names")
        else:
            break
        
    filtered_list.sort()
    return filtered_list
    
def search_group_CSV_mapping(mapping_file):
    # open the json mapping file to find string of names map to their expense tracking csv file
    with open(mapping_file, 'r') as file:
        return json.load(file)
    
def update_group_CSV_mapping(mapping_file, mapping_data):
    # update the json file to update new string of names to their expense tracking csv file
    with open(mapping_file, 'w') as file:
        json.dump(mapping_data, file)
    
def main():
    mapping_file = "NameToCSVMapping.json"
    mapping_data = search_group_CSV_mapping(mapping_file)
    
    name_list = get_sorted_names()
    coworkers = name_list
    
    name_key = ','.join(name_list)
    
    # if string of name already in json file, get the csv filename, if not create a new csv file
    if name_key in mapping_data:
        filename = mapping_data[name_key]
    else:
        filename = input("Your expense tracker has not yet created. Please provide a CSV filename to set up your expenses: ")
        if not filename.lower().endswith('.csv'):
            filename = filename + '.csv'
        mapping_data[name_key] = filename
        
    # let user enter the total coffee price for today
    while True:    
        user_input = input("Please enter total coffee price for today: ")
        try: 
            totalCoffeePrice = round(float(user_input), 2)
            if totalCoffeePrice <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("This is not a number. Please try again.")
          
    # update mapping file with new string of names and the corresponding csv filename
    update_group_CSV_mapping(mapping_file, mapping_data)
    
    tracker = CoffeeExpenseTracker(coworkers, totalCoffeePrice, filename)
    tracker.run()
    

if __name__ == "__main__":
    main()