import csv

# Open the CSV file and create a CSV reader
with open('fraud-data.csv', 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=';')

    # Extract the first column
    urls = [row[0] for row in reader]

# Write the first column to a new text file
with open('urls.txt', 'w') as txt_file:
    for url in urls:
        txt_file.write(url + '\n')