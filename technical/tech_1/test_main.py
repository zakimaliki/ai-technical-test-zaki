import csv
from main import find_discount_position

# Open data.csv file in read mode
with open('data.csv', newline='') as csvfile:
    # Create DictReader object to read CSV as dictionary
    reader = csv.DictReader(csvfile)
    for row in reader:
        # Get input value from 'input' column
        test_input = row['input']
        expected = int(row['expected_output'])
        result = find_discount_position(test_input)

        # Verify result matches expected output
        assert result == expected, f"Failed for input {test_input}. Expected {expected}, got {result}"
    print("Semua test case berhasil.")