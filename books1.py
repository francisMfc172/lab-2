from csv import reader

bold = '\u001b[1m'
underline = '\u001b[4m'
reversed = '\u001b[7m'
reset = '\u001b[0m'

count = 0
with open('books-en.csv', 'r', encoding='windows-1251', newline='') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        if len(row[1])>30:
            count+=1

print(f'{bold}The number of entries with characters of the Name field greater than 30 are{reset}: {bold}{underline}{reversed}{count}{reset}')
