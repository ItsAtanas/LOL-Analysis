import csv
import json

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

# Normalized Values
firstBlood_equal_normalized = calculate_percentage_equal(winner_column_values, firstBlood_column_values, True)
firstTower_equal_normalized = calculate_percentage_equal(winner_column_values, firstTower_column_values, True)
firstInhibitor_equal_normalized = calculate_percentage_equal(winner_column_values, firstInhibitor_column_values, True)
firstBaron_equal_normalized = calculate_percentage_equal(winner_column_values, firstBaron_column_values, True)


print(json.dumps({
    "firstKill": f"{firstBlood_equal:.2f}%",
    "firstTower": f"{firstTower_equal:.2f}%",
    "firstInhibitor": f"{firstInhibitor_equal:.2f}%",
    "firstBaron": f"{firstBaron_equal:.2f}%",
    "firstBloodNormalized": f"{firstBlood_equal_normalized:.2f}%",
    "firstTowerNormalized": f"{firstTower_equal_normalized:.2f}%",
    "firstInhibitorNormalized": f"{firstInhibitor_equal_normalized:.2f}%",
    "firstBaronNormalized": f"{firstBaron_equal_normalized:.2f}%"
}, indent=4))

