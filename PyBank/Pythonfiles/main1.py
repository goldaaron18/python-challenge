
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

outputfile = os.path.join('..',"analysis", "budget_analysis.txt")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    budgetdata = csv.reader(csvfile, delimiter=',')

    csv_header = next(budgetdata)
 
    firstrow = next(budgetdata)

    months = 1
    profit = int(firstrow[1])
    change = 0
    prevprofit = int(firstrow[1])
    sumchange = 0
    greatestincrease = 0
    greatestdecrease = 0
    increasedate = 0
    decreasedate = 0
    for row in budgetdata:
        months += 1
        profit += int(row[1])
        change = int(row[1]) - prevprofit
        sumchange += change
        prevprofit = int(row[1])
        if change > greatestincrease:
            greatestincrease = change
            increasedate = str(row[0])
        if change < greatestdecrease:
            greatestdecrease = change
            decreasedate = str(row[0])


    output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${profit}\n"
    f"Average Change: $ {sumchange/(months-1)}\n"
    f"Greatest Increase in Profits: {increasedate} (${greatestincrease})\n"
    f"Greatest Decrease in Profits: {decreasedate} (${greatestdecrease})\n")

# Print the output (to terminal)
print(output)

with open(outputfile, "w") as txt_file:
    txt_file.write(output)
