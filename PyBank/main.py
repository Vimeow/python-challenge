# Assigment: Python-challenge
# Person: Vy Nguyen
# Date: 23/10/2023


# Import modules:
import os
import csv

# Read csv file:

csv_path = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)

# Create lists to hold months and profit/loss:
    months = []
    profits_losses = []

    for row in csv_reader:
        month = row[0]
        profit_loss = row[1]

        months.append(month)
        profits_losses.append(profit_loss)

# The total number of months included in the dataset
total_month = len(months)

# The net total amount of "Profit/Losses" over the entire period
net_total = 0
for i in range(total_month):
    net_total = net_total + int(profits_losses[i])

# The changes in "Profit/Losses" over the entire period
changes = []

for i in range(total_month-1):
    change = int(profits_losses[i+1]) - int(profits_losses[i])
    changes.append(change)

# The average of those changes
total_change = 0

for i in changes:
    total_change = total_change + i
avg_change = round(total_change/(total_month-1), 2)

# The greatest increase in profits (date and amount) over the entire period
max_increase = changes[0]
for i in changes:
    if i > max_increase:
        max_increase = i
    else:
        max_increase = max_increase

# Associating month with the max_increase in profit
# print(months[(changes.index(max_increase)) + 1])

# The greatest decrease in profits (date and amount) over the entire period
max_decrease = changes[0]
for i in changes:
    if i < max_decrease:
        max_decrease = i
    else:
        max_decrease = max_decrease

# Associating month with the max_decrease in profit
# print(months[(changes.index(max_decrease)) + 1])

# Print the analysis to the terminal:
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(
    f"Greatest Increase in Profits: {months[(changes.index(max_increase)) + 1]} (${max_increase})")
print(
    f"Greatest Decrease in Profits: {months[(changes.index(max_decrease)) + 1]} (${max_decrease})")

# Export the results to a text file:
output_path = os.path.join(".", "analysis", "analysis.txt")

with open(output_path, 'w') as textfile:
    textfile.write(
        f"Financial Analysis\n\
----------------------------\n\
Total Months: {total_month}\n\
Total: ${net_total}\n\
Average Change: ${avg_change}\n\
Greatest Increase in Profits: {months[(changes.index(max_increase)) + 1]} (${max_increase})\n\
Greatest Decrease in Profits: {months[(changes.index(max_decrease)) + 1]} (${max_decrease})")
