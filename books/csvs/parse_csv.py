import csv

html_output = ''
book_title = [],
author = [],
publication_date = [],
plot_summary = []

with open ('patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next (csv_data)

        for line in csv_data:
            print(line)
