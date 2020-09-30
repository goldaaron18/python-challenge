
import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

outputfile = os.path.join('..',"analysis", "election_analysis.txt")

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    electiondata = csv.reader(csvfile, delimiter=',')

    csv_header = next(electiondata)

    
    polldict = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
    "O'Tooley": 0,
    }

    votes = 0
    count = 0
    for row in electiondata:
        votes += 1
        name = row[2]
        for key, value in polldict.items():
            if key == name:
                polldict[name] += 1
   
    
    output = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes: {votes}\n"
    f"----------------------------\n")

    winner = "Khan"
    winnervotes = polldict["Khan"]
    for key, value in polldict.items():
        if value > winnervotes:
            winner = key
            winnervotes = value
        output += (
        f"{key}: {round(value/votes*100,2)}% ({value})\n")


    output += (
    f"----------------------------\n"
    f"Winner: {winner}\n"
    f"----------------------------\n")

# Print the output to terminal
print(output)

with open(outputfile, "w") as txt_file:
    txt_file.write(output)