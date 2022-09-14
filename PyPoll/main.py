import csv

# define the file path
path = "PyPoll/Resources/election_data.csv"

# Variables for calculations
total_votes = 0
c_votes = 0
d_votes = 0
r_votes = 0
candidates_array = []

# Reads and opens the csv file
# Calculates the total number of votes
with open(path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    # Stores header row
    csv_header = next(csv_file)

    # Makes a list of unique candidates and calculates their share of votes
    for row in csv_reader:
        total_votes += 1
        if row[2] not in candidates_array:
            candidates_array.append(row[2])
        if row[2] == candidates_array[0]:
            c_votes += 1
        elif row[2] == candidates_array[1]:
            d_votes += 1
        else:
            r_votes += 1

# determines winner
if c_votes > d_votes and c_votes > r_votes:
    winner = candidates_array[0]

elif d_votes > c_votes and d_votes > r_votes:
    winner = candidates_array[1]

else:
    winner = candidates_array[2]

# Output results to Terminal
print("Election Results")
print("--" * 14)
print(f"Total Votes: {total_votes}")
print("--" * 14)
print(f"{candidates_array[0]}: {round(c_votes * 100/total_votes, 3)}% ({c_votes})")
print(f"{candidates_array[1]}: {round(d_votes * 100/total_votes, 3)}% ({d_votes})")
print(f"{candidates_array[2]}: {round(r_votes * 100/total_votes, 3)}% ({r_votes})")
print("--" * 14)
print(f"Winner: {winner}")
print("--" * 14)

# Writes to an analysis.txt file
output_path = "PyPoll/Analysis/analysis.txt"
with open(output_path, 'w') as analysis:
    analysis.write("Election Results")
    analysis.write("\n" + "--" * 14)
    analysis.write(f"\nTotal Votes: {total_votes}")
    analysis.write("\n" + "--" * 14)
    analysis.write(f"\n{candidates_array[0]}: {round(c_votes * 100/total_votes, 3)}% ({c_votes})")
    analysis.write(f"\n{candidates_array[1]}: {round(d_votes * 100/total_votes, 3)}% ({d_votes})")
    analysis.write(f"\n{candidates_array[2]}: {round(r_votes * 100/total_votes, 3)}% ({r_votes})")
    analysis.write("\n" + "--" * 14)
    analysis.write(f"\nWinner: {winner}")
    analysis.write("\n" + "--" * 14)