import csv
from account import Account

input_file = "/Users/danielfrank/Documents/accountExercise/testData/input.csv"         
output_file = "/Users/danielfrank/Documents/accountExercise/testData/input-status.csv"

accounts = []

with open(input_file, newline='') as in_csvfile:
    reader = csv.DictReader(in_csvfile)
    for row in reader:
        account = Account(row)
        account.getStatus()
        accounts.append(account)

with open(output_file,'w') as out_csvfile:
    fieldnames = ['Account ID','First Name','Created On','Status','Status Set On']
    writer = csv.DictWriter(out_csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for account in accounts:
        temp_dict = account.makeDictionary()
        """DictWriter doesn't like when keys not defined in fieldnames are in the dictionary"""
        del temp_dict["Account Name"]
        writer.writerow(temp_dict)

