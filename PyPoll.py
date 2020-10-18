<<<<<<< HEAD
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)
=======
# The data we need to retrieve.
# 1. The total number of votes  cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Assign a variable for the file to load and the path.
import csv
import os

#Create a filename to a direct or indirect path to the file.
file_to_load = os.path.join("Resources", "election_results.csv")

#Open the election results and read the file.
with open(file_to_load) as election_data:

#To do: perform analysis
    print(election_data)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

 # Write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")
>>>>>>> ba02c3819d761d4482841c94696f498b5daf51ef
