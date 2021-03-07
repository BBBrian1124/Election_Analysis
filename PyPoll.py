#Data to retreive
#1. Total number of votes cast
#2. A complete list of candidates who received votes
#3. Total number of votes each candidate received
#4. Percentage of votes each candidate won
#5. The winner of the election based on popular vote

#to import the csv and os module
import csv 
import os

## FILE CREATION ##
#tells the program to load in the csv file under the resources folder and assigns it to the file_to_load variable using the direct method 
file_to_load = 'Resources/election_results.csv'
# Create a filename variable and save the file to an path via the indirect method 
file_to_save = os.path.join("analysis", "election_analysis.txt")

## OPEN FILE ##
# we opened the file_to_load (the csv) and declare it as the variable election_data
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

 

# Using the with statement open the file as a text file rather than having to open and close it
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    txt_file.write("Counties in the election\n")
    txt_file.write("------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson") 
