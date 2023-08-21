#!/usr/bin/env python
# coding: utf-8
# Create a Python script that analyzes the votes and calculates each of the following values:
# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote


#INPUT
import os
import csv
import collections as cnt 

csvpath = os.path.join('.','Resources','election_data.csv')

#variables
vote_total = 0
votes =cnt.Counter()
voter_count = []
nl ='\n'

with open (csvpath) as election_file:
    reader = csv.reader(election_file, delimiter = ',')
    csv_header=next(reader)

    #Calculate
    for row in reader: 
        vote_total +=1
        
        #using collections module to count the canidates
        canidate = row[2]
        votes[canidate] += 1

    for i in votes:
        percent = round((votes[i]/vote_total) *100,3)
        voter_count.append (f"{i}: {percent}% ({votes[i]})")

#output  
output = (
f"Election Results\n"
f"--------------------\n"
f" \n"
f"Total Votes: {vote_total}\n"
f" \n"
f"--------------------\n"
f"{nl.join(voter_count)}"
f" \n"
f"--------------------\n"
f" \n"
f"Winner: {votes.most_common()[0][0]}\n"
)
print(output)

#write txt file 
output_path = os.path.join(".","Analysis","PollAnalysis.txt")
with open (output_path, 'w') as txtfile:
    txtfile.writelines({output})

