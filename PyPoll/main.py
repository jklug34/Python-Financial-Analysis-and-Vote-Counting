# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```

# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.


#import modules 
#create file paths across operating systems
import os
#module for reading a CSV file
import csv


#import a counter module
from collections import Counter

#find the path of the resource folder containing the csv file "election_data"
election_data_path = os.path.join('Resources', 'election_data.csv')
#print(election_data_path)

voter_ID = []
county = []
canidate = []

with open (election_data_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    #print(csv_reader)
    
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    for row in csv_reader:
        voter_ID.append(row[0])
        county.append(row[1])
        canidate.append(row[2])

    #Determine the total number of votes cast
    total_votes = len(voter_ID)
    #print(total_votes)

    #find all of the unique canidates names using set
    myset_unique_canidates = set(canidate)
    #print(myset_unique_canidates)
    #print(len(myset_unique_canidates))

    #count of votes each canidate recieved
    number_of_unique_canidates = Counter(canidate).keys()
    vote_count_each_canidate = Counter(canidate).values()
    #print(number_of_unique_canidates)
    #print(vote_count_each_canidate)
    

    # turn the dictionary output into a list
    list_of_vote_count_candiate = list(vote_count_each_canidate)
    #print(list_of_vote_count_candiate)

    # determine the percentage of votes each canidate won
    percentage_of_votes_each_canidate_won = []
    for x in list_of_vote_count_candiate:
        percentage_of_votes_each_canidate_won.append(x/(total_votes) * 100)
    #print(percentage_of_votes_each_canidate_won)
       
    #round the list to three decimals
    import numpy as np
    percentage_of_votes_each_canidate_won = list(np.around(np.array(percentage_of_votes_each_canidate_won), decimals=3))
    #print(percentage_of_votes_each_canidate_won)

    
    #find the winner (zero index)
    winner = list(number_of_unique_canidates)[0]
    #print(winner)
    
    #find second place (first index)
    runnerup = list(number_of_unique_canidates)[1]
    #print(runnerup)
    
    #find third place (second index)
    third_place = list(number_of_unique_canidates)[2]
    #print(third_place)
   
    #find fourth place (third index)
    fourth_place = list(number_of_unique_canidates)[3]
    #print(fourth_place)


#print out all values as requested
print('Election Results')
print('-------------------------------')
print(f"Total Votes: {str(total_votes)}")
print('-------------------------------')
print(f"{winner}: {str((percentage_of_votes_each_canidate_won)[0])}% ({str((list_of_vote_count_candiate)[0])})")
print(f"{runnerup}: {str((percentage_of_votes_each_canidate_won)[1])}% ({str((list_of_vote_count_candiate)[1])})")
print(f"{third_place}: {str((percentage_of_votes_each_canidate_won)[2])}% ({str((list_of_vote_count_candiate)[2])})")
print(f"{fourth_place}: {str((percentage_of_votes_each_canidate_won)[3])}% ({str((list_of_vote_count_candiate)[3])})")
print('-------------------------------')
print(f"Winner: {winner}")
print('-------------------------------')



print 
import sys
sys.stdout = open('main.txt', 'w')
print('Election Results')
print('-------------------------------')
print(f"Total Votes: {str(total_votes)}")
print('-------------------------------')
print(f"{winner}: {str((percentage_of_votes_each_canidate_won)[0])}% ({str((list_of_vote_count_candiate)[0])})")
print(f"{runnerup}: {str((percentage_of_votes_each_canidate_won)[1])}% ({str((list_of_vote_count_candiate)[1])})")
print(f"{third_place}: {str((percentage_of_votes_each_canidate_won)[2])}% ({str((list_of_vote_count_candiate)[2])})")
print(f"{fourth_place}: {str((percentage_of_votes_each_canidate_won)[3])}% ({str((list_of_vote_count_candiate)[3])})")
print('-------------------------------')
print(f"Winner: {winner}")
print('-------------------------------')
sys.stdout.close()
