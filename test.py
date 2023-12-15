import csv

# Specify the path to your CSV file
csv_file_path = 'games.csv'

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Skip the header row
    next(csv_reader)

    # Initialize empty arrays to store values from the 5th and 6th columns
    test = []

    # Iterate through rows
    for i, row in enumerate(csv_reader):
        # Store the value from the 5th column into the array
        test.append(row[7])  # Index 4 corresponds to the 5th column

sum_of_zero = 0

for x in test:
    if x == '0':
        sum_of_zero += 1

print (sum_of_zero)
