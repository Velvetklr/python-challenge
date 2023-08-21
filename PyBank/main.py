#!/usr/bin/env python
# coding: utf-8

# Analyze Finance Records
# Calculate Total Number of Months
# Calculate Total Profit/Loss over entire time
# Calculate Changes in Profit over time
# Greatest Increase (date & amount)
# Greatest Decrease (Date & amount)


#INPUT
import os
import csv
from statistics import mean 

#os.chdir(os.path.dirname(os.path.realpath(__file__)))
csvpath = os.path.join('.','Resources','budget_data.csv')

all_months = 0
total_profit = 0
total_change = 0
change_list = []
change_month = []
previous_row = 0
greatest_increase = 0
with open (csvpath) as budget_file:
    csvreader = csv.reader(budget_file, delimiter = ',')
    csv_header=next(csvreader)
       
    for row in csvreader: 
        #CALCULATE
        all_months +=1
        total_profit += int(row[1])
        
        profit = int(row[1])
        
        #Getting Change over time
        change_list.append(profit - previous_row)
        change_month.append([row[0],profit - previous_row])
        previous_row = profit
        change = change_list[1:]

            
change_avg = round(mean(change),2)
greatest_increase = max(change)
greatest_decrease = min(change)  
great = [greatest for greatest in change_month if greatest_increase in greatest]
least = [decrease for decrease in change_month if greatest_decrease in decrease]

#OUTPUT
print("Financial Analysis")
print("----------------------------")
print(f"Total_Months: {all_months}")
print()
print(f"Total: ${total_profit}")
print()
print(f"Average Change ${change_avg}")
print()
print(f"The Greatest Increase in Profits {great}")
print()
print(f"The Greatest Decrease in Profits {least}")


output_path = os.path.join(".","Analysis","BudgetAnalysis.txt")
#print(output_path)
with open(output_path,'w')as txtfile:
    txtfile.writelines ("Financial Analysis\n")
    txtfile.writelines ("----------------------------\n")
    txtfile.writelines (f"Total_Months: {all_months}\n")
    txtfile.writelines (" \n")
    txtfile.writelines (f"Total: ${total_profit}\n")
    txtfile.writelines ("\n")
    txtfile.writelines (f"Average Change ${change_avg}\n")
    txtfile.writelines (" \n")
    txtfile.writelines (f"The Greatest Increase in Profits {great}\n")
    txtfile.writelines (" \n")
    txtfile.writelines (f"The Greatest Decrease in Profits {least}\n")

