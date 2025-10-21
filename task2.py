from csv import reader
from datetime import datetime

matching_books = []
target_year = [2014, 2016, 2017]
extracted_years = []
search = input('Author name: ')
with open('books.csv', 'r', encoding='windows-1251', newline='') as csvfile:
    table = reader(csvfile, delimiter=';')

    for row in table:

        date_string = row[6]
        try:
            date = datetime.strptime(date_string, "%d.%m.%Y %H:%M")  
            year = date.year
            if year in target_year:
                extracted_years.append(year)
        except ValueError:
            print(f"Invalid date format: {date_string}")

        if row[3] == search and year in extracted_years:
            matching_books.append(row)

if matching_books:
    print(f'Books by {search} published in 2014, 2016, or 2017 are:')
    for row in matching_books:
        print(f'{row[1]} \t ({row[6]})')
else:
    print(f'No books by {search}  are found in 2014, 2016, or 2017.')
