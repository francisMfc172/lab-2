

from csv import reader

bold = '\u001b[1m'
underline = '\u001b[4m'
reversed = '\u001b[7m'
reset = '\u001b[0m'

count = 0
with open('books-en.csv', 'r', encoding='windows-1251', newline='') as csvfile:
    table = reader(csvfile, delimiter=';')
    # Skip the header row to avoid counting it
    next(table, None)
    for row in table:
        if len(row[1]) > 30:  # row[1] should be the book name field
            count += 1

print(f'{bold}The number of entries with book titles longer than 30 characters{reset}: {bold}{underline}{reversed}{count}{reset}')