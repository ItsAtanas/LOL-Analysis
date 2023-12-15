import csv
from percentage_calculator import calculate_percentage_equal

# Specify the path to your CSV file
csv_file_path = 'games.csv'

# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader
    csv_reader = csv.reader(file)

    # Skip the header row
    next(csv_reader)

    # Initialize empty arrays to store values from columns
    winner_column_values = []
    firstBlood_column_values = []
    firstTower_column_values = []
    firstInhibitor_column_values = []
    firstBaron_column_values = []
    firstDragon_column_values = []
    firstRiftHerald_column_values = []

    # Iterate through rows
    for i, row in enumerate(csv_reader):
        # Store the values from the columns into arrays
        winner_column_values.append(row[4])  # Winner column. (1 = First team, 2 = Second team)
        firstBlood_column_values.append(row[5])  # Column contains which team got the first kill of the game. 
        firstTower_column_values.append(row[6])  # Column contains which team got the first tower of the game.
        firstInhibitor_column_values.append(row[7])  # Column contains which team got the first inhibitor of the game.
        firstBaron_column_values.append(row[8])
        firstDragon_column_values.append(row[9])
        firstRiftHerald_column_values.append(row[10])

# Use the function from the percentage_calculator module
firstBlood_equal = calculate_percentage_equal(winner_column_values, firstBlood_column_values)
firstTower_equal = calculate_percentage_equal(winner_column_values, firstTower_column_values)
firstInhibitor_equal = calculate_percentage_equal(winner_column_values, firstInhibitor_column_values)
firstBaron_equal = calculate_percentage_equal(winner_column_values, firstBaron_column_values)


print(f"The team that gets the first kill of the game is: {firstBlood_equal:.2f}% more likely to win the game.")
print(f"The team that gets the first tower of the game is: {firstTower_equal:.2f}% more likely to win the game.")
print(f"The team that gets the first tower of the game is: {firstInhibitor_equal:.2f}% more likely to win the game.")
print(f"The team that gets the first baron of the game is: {firstBaron_equal:.2f}% more likely to win the game.")
