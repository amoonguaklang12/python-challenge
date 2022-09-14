import csv

# define the file path
path = r"C:\Users\ander\databootcamp\HW 3\python-challenge\PyBank\Resources\budget_data.csv"

# Variables for calculations
total_months = 0
total_budget = 0
summary_array = []

# Reads and opens the csv file
# Calculates the total number of months and total profit/loss
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Stores header row
    csv_header = next(csv_file)

    # Inserts rows into a new array without the header
    for row in csv_reader:
        total_months += 1
        total_budget += int(row[1])
        summary_array.append(row)

# Variables for calculations
max_index = 0
min_index = 0
max_profit = 0
min_profit = 0 
counter = 0  
total_profit_change = 0

# Calculating profit changes from month to month
for row in range(len(summary_array) - 1):
    profit_change = int(summary_array[counter+1][1]) - int(summary_array[counter][1])
    total_profit_change += profit_change
    if profit_change > max_profit:
        max_profit = profit_change
        max_index = summary_array[counter+1][0]
    if profit_change < min_profit:
        min_profit = profit_change
        min_index = summary_array[counter+1][0]
    counter += 1

# Financial Analysis
print("Financial Analysis")
print("--" * 14)
print("Total Months:", total_months)
print("Total: $", total_budget)
print("Average Change: $", round(total_profit_change/counter, 2))
print(f"Greatest Increase in Profits: {max_index} (${max_profit})")
print(f"Greatest Decrease in Profits: {min_index} (${min_profit})")
    
output_path = r"C:\Users\ander\databootcamp\HW 3\python-challenge\PyBank\Analysis\analysis.txt"
with open(output_path, 'w') as analysis:
    analysis.write("Financial Analysis")
    analysis.write("\n" + "--" * 14)
    analysis.write(f"\nTotal Months: {total_months}")
    analysis.write(f"\nTotal: ${total_budget}")
    analysis.write(f"\nAverage Change: ${round(total_profit_change/counter, 2)}")
    analysis.write(f"\nGreatest Increase in Profits: {max_index} (${max_profit})")
    analysis.write(f"\nGreatest Decrease in Profits: {min_index} (${min_profit})")
    