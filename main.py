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
    fifth_column_values = []
    sixth_column_values = []

    # Iterate through rows
    for i, row in enumerate(csv_reader):
        # Store the value from the 5th column into the array
        fifth_column_values.append(row[4])  # Index 4 corresponds to the 5th column

        # Store the value from the 6th column into the array
        sixth_column_values.append(row[5])  # Index 5 corresponds to the 6th column

# Initialize a counter for equal values
equal_count = 0

# Iterate through the arrays to count equal values
for i in range(len(fifth_column_values)):
    if fifth_column_values[i] == sixth_column_values[i]:
        equal_count += 1

# Calculate the percentage of equal values
percentage_equal = (equal_count / len(fifth_column_values)) * 100

print(f"The percentage of values in the 5th and 6th columns that are equal is: {percentage_equal:.2f}%")
