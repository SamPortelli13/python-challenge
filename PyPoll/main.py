import sys, os
import csv

election_data_csv = os.path.join(os.path.realpath('..'),"Pypoll\Resources", "election_data.csv")

# Lists & variables to store data
candidatelist = []
candidatevotes = []

totalvotes = 0

# Use encoding for Windows   , newline=''
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Read the header row first
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    for row in csvreader:
        # Add votes
        totalvotes += 1
        # Add Candidate to List and Count their votes
        found=False
        for i in range(len(candidatelist)):
            if row[2] == candidatelist[i]:
                found = True
                candidatevotes[i] +=1
        if found == False:
            candidatelist.append(row[2])
            candidatevotes.append(1)
#            print(f"{candidatelist} VoterId: {row[0]}")
#            print(f"Votes: {candidatevotes}")
counter=0

# Print Summary Results
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {totalvotes}")
print(f"----------------------------")

winningcandidate =""
winningvotes=0

for i in range(len(candidatelist)):
    percentage=candidatevotes[i] / totalvotes
    format_percentage = "{:.3%}".format(percentage)
    print(f"{candidatelist[i]}: {format_percentage} ({candidatevotes[i]})")
    if candidatevotes[i] > winningvotes:
        winningvotes = candidatevotes[i]
        winningcandidate = candidatelist[i]
print(f"----------------------------")
print(f"Winner: {winningcandidate}")
print(f"----------------------------")

# Write the Summary to a text file
analysis_data_csv = os.path.join(os.path.realpath('..'),"PyPoll\Analysis", "analysis_data.csv")

with open(analysis_data_csv,'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Total Votes: "+str(totalvotes)])
    csvwriter.writerow(["----------------------------"])
    for i in range(len(candidatelist)):
        percentage=candidatevotes[i] / totalvotes
        format_percentage = "{:.3%}".format(percentage)
        csvwriter.writerow([candidatelist[i]+": " + str(format_percentage) + " (" + str(candidatevotes[i]) + ")"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow(["Winner: "+ winningcandidate])
    csvwriter.writerow(["----------------------------"])