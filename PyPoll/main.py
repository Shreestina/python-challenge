#Import modules os and csv
import os
import csv

#Create a path for the election_data.csv file in csv_path
csv_path = os.path.join("Resources", "election_data.csv")

#Create the lists to store data
votes = []
candidates_list = []
unique_candidate_name = []
vote_count = []
vote_percent = []

#Open the csv file using the the set path
with open (csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    #Read the header row first
    header = next(csv_reader)

    #looping through all the rows
    for row in csv_reader:
        #calculate the total votes
        votes.append(row[0])
        total_votes=len(votes)

        #Add the candidate names in candidates_list
        candidates_list.append(row[2])
    
    #Using set() property of Python, we can check for the unique name of candidates
    for x in set(candidates_list):
        unique_candidate_name.append(x)
        
        #Count the votes for each candidate
        y = candidates_list.count(x)
        vote_count.append(y)

        #calculate the percentage of the votes for each candidate
        z = (y/total_votes)*100
        vote_percent.append(z)
    
    #Calculate the winner    
    wining_vote_count = max(vote_count)
    winner = unique_candidate_name[vote_count.index(wining_vote_count)]

#Print the output
print(f'---------------------------')
print(f'Election Results')
print(f'--------------------------- ')
print(f'Total Votes: {total_votes} ')
print(f'--------------------------- ')
for i in range(len(unique_candidate_name)):
    print(f'{unique_candidate_name[i]} : {vote_percent[i]:.3f} % ({vote_count[i]})')    
print(f'--------------------------- ')
print(f'The winner is : {winner}')
print(f'--------------------------- ')  

#Specify a path for output file named pybank_output
output_path = os.path.join("Analysis","pypoll_output.txt") 

#Open the file using "write" mode in a text file
with open(output_path, 'w') as text:
    text.write(f'---------------------------\n')
    text.write(f'Election Results\n')
    text.write(f'--------------------------- \n ')
    text.write(f'Total Votes: {total_votes}\n')
    text.write(f'---------------------------\n ')
    for i in range(len(unique_candidate_name)):
        text.write(f'{unique_candidate_name[i]} : {vote_percent[i]:.3f} % ({vote_count[i]})\n')    
    text.write(f'---------------------------\n')
    text.write(f'The winner is : {winner}\n')
    text.write(f'---------------------------\n')  