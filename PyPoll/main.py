# Assigment: Python-challenge
# Person: Vy Nguyen
# Date: 23/10/2023


# Import modules:
import os
import csv

# Read csv file:

csv_path = os.path.join('.', 'Resources', 'election_data.csv')

with open(csv_path) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_header = next(csv_reader)

# Create lists to hold "Voter ID", "County", and "Candidate"
    voter_IDs = []
    counties = []
    candidates = []

    for row in csv_reader:
        voter_ID = row[0]
        county = row[1]
        candidate = row[2]

        voter_IDs.append(voter_ID)
        counties.append(county)
        candidates.append(candidate)

# The total number of votes cast
total_votes = len(voter_IDs)

# A complete list of candidates who received votes
candidate_list = []
candidate_list.append(candidates[0])

for i in range(total_votes-1):
    if candidates[i] != candidates[i+1] and candidates[i+1] not in candidate_list:
        candidate_list.append(candidates[i+1])

# The percentage of votes each candidate won (percentage_vote) and the total number of votes each candidate won (vote_count)
total_candidates = len(candidate_list)
percentage_vote = []
vote_count = []

for j in range(total_candidates):
    count = 0
    for i in range(total_votes):
        if candidates[i] == candidate_list[j]:
            count = count + 1
    percentage = (count / total_votes) * 100
    percentage_vote.append(percentage)
    vote_count.append(count)

# The winner of the election based on popular vote
for i in range(total_candidates-1):
    if vote_count[i+1] > vote_count[i]:
        winner_count = vote_count[i+1]
winner = candidate_list[vote_count.index(winner_count)]

# Print the analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

candidate_summary = []
for i in range(total_candidates):
    candidate_summary.append(
        f"{candidate_list[i]}: {round(percentage_vote[i], 3)}% ({vote_count[i]})")
candidate_summary_lines = "\n".join(candidate_summary)

print(candidate_summary_lines)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Export the results to a text file:
output_path = os.path.join(".", "analysis", "analysis.txt")

with open(output_path, 'w') as textfile:
    textfile.write(f"Election Results\n\
-------------------------\n\
Total Votes: {total_votes}\n\
-------------------------\n\
{candidate_summary_lines}\n\
-------------------------\n\
Winner: {winner}\n\
-------------------------")
