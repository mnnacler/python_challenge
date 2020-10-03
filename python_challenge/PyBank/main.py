import os
import csv

csvpath = os.path.join('Resources','budget_data.csv')

def avgChange(numbers):
    total = 0
    for num in numbers:
        total += num
    return total/len(numbers)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader,None)
    print(csvreader)

    months = int(0)
    totalRev = int(0)
    changes = []
    prevNum = 0
    newNum = 0
    change = 0
    greatestInc = 0
    greatestDec = 0
    decMonth = ""
    incMonth = ""

    for row in csvreader:
        totalRev += int(row[1])
        months += 1
        newNum = int(row[1])
        if months >1:
            if (newNum - prevNum) > greatestInc:
                greatestInc = newNum - prevNum
                incMonth = row[0]
            elif (newNum - prevNum) < greatestDec:
                greatestDec = newNum - prevNum
                decMonth = row[0]

            change = newNum - prevNum
            changes.append(change)
            prevNum = newNum
        else:
            prevNum = int(row[1])


    title = "Financial Analysis"
    dashes = "-----------------------------"
    totalMonths = "Total Months: " + str(months)
    profit = "Total: $" + str(totalRev)
    avgChange = "Average Change: $" + str(avgChange(changes))
    profitInc = "Greatest Increase in Profits: " + str(incMonth) + " $" + str(greatestInc)
    profitDec = "Greatest Decrease in Profits: " + str(decMonth) + " $" + str(greatestDec)

textlist = [title,dashes,totalMonths,profit,avgChange,profitInc,profitDec]
#print(textlist)
resultsPyBank = open("Analysis/resultsPyBank.txt","w")
for line in textlist:
    print(line)
    resultsPyBank.write(line)
    resultsPyBank.write("\n")
resultsPyBank.close()
