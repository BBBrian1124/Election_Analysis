### PROJECT OVERVEIW ####
# Data to retreive
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#to import the csv and os modules needed to perform functions
import csv 
import os

## FILE CREATION ##
#tells the program to load in the csv file under the resources folder and assigns it to the file_to_load variable using the direct method 
file_to_load = 'Resources/election_results.csv'
# Create a filename variable and save the file to an path via the indirect method 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a vote counter variable which we will increment to count the number of votes
total_votes = 0

#2. Create a list to store the list of candidates, we will first create a blank list and feed values into this list 
candidate_options = []

#3. Declare an empty dictionary, which we will fill with the candidate name as the key and their number of votes as the value 
candidate_votes = {}

#5. Winning Candidate and Winning Count Tracker, we will first initialize these values as nothing, then replace them as we loop through the data 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

## OPEN FILE ##
# Ppen the file_to_load (the source csv) and declare it as the variable election_data
with open(file_to_load) as election_data:

    # Read the data in the file object (election data aka the csv file) with the reader function.
    file_reader = csv.reader(election_data)

    # Skip the first row in the file_reader object 
        # the souce data is Ballot ID, County, Canditate, followed by the values below those headers
        # by using the next function on the file reader object, we skip the first row in that object
    headers = next(file_reader)
    
    # Loop through each row in the CSV file, the header is skipped since we have use the next() function on the file_reader object
    for row in file_reader:
        #1. add 1 to the total vote count each time we go through the rows
        total_votes += 1 # this is the python format to increment, it is the same as saying total_votes = total votes + 1
        
        # 2. Extracts the values in each row in the 2nd index and declares is as the variable candidate name 
        candidate_name = row[2]
        #2. We are checking if the candidate name is not in the list candiate_options, and if not then add it to the list  
        if candidate_name not in candidate_options:
            #2. Add the candidate name to the candidate list if it is not already there, it is being assinged as a key to the candidate_options list 
            candidate_options.append(candidate_name)
            #3. As we are looping through the rows we are using this function dictionary_name[key] to assign the candidate_name as the key and assigning it with a value of 0
                # we are assigning these values into the "candidate_voters" dictonary  
            candidate_votes[candidate_name] = 0 

        #3. We are adding the count of the votes to the candidates name 
        #3. We need to do this outside of the if statement but within the loop
        #3. As it loops, it adds 1 each time it finds the key (candidate name)
        candidate_votes[candidate_name] += 1

# Save the results to our text file by opening the file and indicating that we will be writing into it
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal by assigning values to the variable election_results 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # write the election_results to the txt file
    txt_file.write(election_results)

    # 4. Iterate through the candidate_votes list
    for candidate_name in candidate_votes:
        # retreive the # of votes by getting the values for the key [candidate name] in the candidate_votes dictionary
        # using the function dictionary_name[key] we are assinging the values for the key candidate_name to the variable votes 
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # assign each candidate name, their vote % and their # of votes to a variable
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  write the candidate results to our text file.
        txt_file.write(candidate_results)

    # 5. Determine winning vote count and candidate
        # Place a if statement within the loop to check these conditions 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # as it loops through the values, if the values is > than the prior value then it is declared/assigned to be the winner 
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    ## PRINT ##
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)