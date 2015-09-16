import csv
import argparse
from account import Account

parser = argparse.ArgumentParser(description='Process a CSV of account info, gather status info and \
    output a second file with account and status info.')
parser.add_argument("filepath")
args = parser.parse_args()
input_file = args.filepath
output_file = input_file[0:len(input_file)-4] + "-status" + input_file[len(input_file)-4:len(input_file)]

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

