import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

votes = 0
candidates = []
canVotes = []
canIndex = 0
percentage = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader,None)
    print(csvreader)

    for row in csvreader:
        votes += 1
        if votes == 1:
            candidates.append(row[2])
            canVotes.append(int(0))
        elif row[2] not in candidates:
            candidates.append(row[2])
            canVotes.append(int(0))
        
        canIndex = candidates.index(row[2])

        canVotes[canIndex] += 1

percentage = [x/votes*100 for x in canVotes]      
winner = candidates[percentage.index(max(percentage))]

results = []

title= "Election Results"
dashes = "-----------------------"
totalVotes = "Total Votes: " + str(votes)
#print("-----------------------")

for (a,b,c) in zip(candidates, percentage, canVotes):
    results.append(a + ": " + str(b) + "% (" + str(c) + ")")

#print("-----------------------")
winnerTitle = "Winner: " + winner
#print("-----------------------")
resultsPyPoll = open("Analysis/resultsPyPoll.txt","w")
textlist = [title,dashes,totalVotes,results,dashes,winnerTitle,dashes]
for elem in textlist:
    if elem == results:
        for x in results:
            print(x)
            resultsPyPoll.write(x)
            resultsPyPoll.write("\n")
    else:
        print(elem)
        resultsPyPoll.write(elem)
        resultsPyPoll.write("\n")
resultsPyPoll.close()