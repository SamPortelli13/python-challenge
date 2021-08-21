import sys, os
import csv

budget_data_csv = os.path.join(os.path.realpath('..'),"PyBank\Resources", "budget_data.csv")

# Lists & variables to store data
monthslist = []
profitlosslist = []

totalprofit = 0
greatestincr =0.0
greatestincrmonth=""
greatestdecr =0.0
greatestdecrmonth=""
currprofitloss=0

# Use encoding for Windows   , newline=''
with open(budget_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    for row in csvreader:
        # Add months
            monthslist.append(row[0])
        # Add profitloss
            profitlosslist.append(row[1])
counter=0
totalchange=0
currentchange=0

for counter in range(len(monthslist)):
    if counter == 0:
        currprofitloss = int(profitlosslist[counter])
        totalprofit += currprofitloss
        lastchange = 0
    else: 
        currprofitloss = int(profitlosslist[counter])
        lastprofitloss = int(profitlosslist[counter-1])
        totalprofit += currprofitloss
        currentchange = currprofitloss - lastprofitloss
        if currentchange > greatestincr:
            greatestincr = currentchange
            greatestincrmonth = monthslist[counter]
        elif currentchange < greatestdecr:
            greatestdecr = currentchange
            greatestdecrmonth = monthslist[counter]
    totalchange += currentchange

# Determine the totals
total_number_months = len(monthslist)
average_change = totalchange/(total_number_months-1)
format_average = "{:.2f}".format(average_change)

# Print the Summary
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_number_months}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatestincrmonth} (${greatestincr})")
print(f"Greatest Decrease in Profits: {greatestdecrmonth} (${greatestdecr})")

# Write the Summary to a text file
analysis_data_csv = os.path.join(os.path.realpath('..'),"PyBank\Analysis", "analysis_data.csv")

with open(analysis_data_csv,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Months: "+str(total_number_months)])
    csvwriter.writerow(["Average Change: $"+str(format_average)])
    csvwriter.writerow(["Greatest Increase in Profits: "+ greatestincrmonth+" ($" + str(greatestincr)+")"])
    csvwriter.writerow(["Greatest Increase in Profits: "+ greatestdecrmonth+ " ($" + str(greatestdecr)+")"])
