# Election_Analysis
## UofT Data Analytics Boot Camp - module 3

# Overview of Election Audit: 
## Explain the purpose of this election audit analysis.
* We have been given a dataset that holds voting data, such as the ballot IDs, counties and candidate names. The purpose is to obtain the election results. In order to do this, we will use the Python programming language to extract information with regards to the votes. We will extract, the winning candidate and largest county turnout based on their vote count and vote percentage of the total votes. By using the Python programming language, we will be able to re-use this code in other precincts and scenarios. 

# Election-Audit Results: 
## Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
### How many votes were cast in this congressional election?
* Total Votes: 369,711

![Total Vote Code] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/Total_Votes.PNG
* In order to obtain this information, we used Python to first read data from our dataset then loop through each row in the dataset (skipping the header) to count the total number of votes in this election. I will refer to this loop as "loop_all" below. 

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)

![Counter Vote Counter Code] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/County_Vote_Counter.PNG
*  In order to obtain this information, we used Python to first create a list (county_list) that stores our counties (county_name). Within the loop_all (mentioned above), the if statement looks through each row in the dataset and checks if the county_name is already in the county_list, and if it is not to add it to the list, allowing us to extract each unique county. The loop will then increment (by 1) the vote count (the value) for that county (the key) each time it finds that county in the dataset, and place this within the county_votes dictionary. 

![County Breakdown Code] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/County_Vote_Breakdown.PNG
* Now that we have the county and number of votes in a dictionary, we can create a separate loop (I will refer to this as "loop_list") to loop through each county (county_name) in our list of counties (county_list), and extract the votes (county_vote_count or the value) for each county (county_name or the key) from our county_votes dictionary, and calculate their votes as a percentage of the total votes. 

### Which county had the largest number of votes?
* Largest County Turnout: Denver

! [County Winner Code] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/County_Winner.PNG
* Now that we have the total number of votes and the number of votes for each county, we can use Python to determine which county is the "winner" or "leader". We will use the loop_list loop to loop through the list of counties and their votes (extracted above) and if it is the leading vote getter, we will assign it/list it as the "winner" or "leader".

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)

![Loop_all Structure] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/First%20Loop.PNG

![Loop_List Structure] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/Candidate%20Code.PNG
* The same concept is applied to the candidate breakdowns, except the code is modified to store and extract the candidate information instead of the county information. In these images, it is easier to see more of the code and the loop strcutures, regardless, the idea/structure to extract the information for the candidate is the same used for the county. Generally speaking, if you replace the word "county" with "candidate" in any of the code above (and vice versa), that is how the code for obtaining the candidate (and vice versa) information looks like.

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
* Winner: Diana DeGette
* Winning Vote Count: 272,892
* Winning Percentage: 73.8%

# Election-Audit Summary: 
### In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. 
### Give at least two examples of how this script can be modified to be used for other elections.
![File Path] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/File%20Path.PNG
* One of the first changes that can easily be made is to change the file which we pull the data from by changing the path specified here. Assuming other elections have their voting data organized the same (or even similar) way, we can easily modify the Python code to extract the information from that data source file. As long as the source file contains the same data (i.e. vote/ballot ID for county and candidate), we can modify the code slightly even if the layout were to differ, or other information was in that file. The changes in this scenario will most likely just be the index # in the code "= row[#]" shown in the 'loop_all structure' image. 
* Additionally, we can modify/use this code to count votes for more than just counties. The code is designed in a manner where it extracts the count of a "value" from a "key". In this case, we are extracting the "votes" (value) from the "county" (key). Because the code is structured in this manner, we can use it to extract any other value from any other key. For example, assume our source data file had other information such as the gender, age, race, state, region, etc. for the ballot. We can assign any of this information to be the "key" or the "value" to obtain other information such as # of votes by gender (value) by state (key), or # of votes by age range (value) in each race (key). For scenarios where there would be multiple groups for the value (i.e. male and female, or a range of ages, for the # of votes), we'd likely have to make modifications to the code to extract those counts into their own variables, rather than the current code which only is created for one group (i.e. all votes).

# Appendix:
* [Python Code] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/PyPoll_Challenge.py
* [Results] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Analysis/election_results.txt
* [Data Source File] https://github.com/BBBrian1124/Election_Analysis/blob/Challenge/Resources/election_results.csv
* [Repository Link] https://github.com/BBBrian1124/Election_Analysis/tree/Challenge
