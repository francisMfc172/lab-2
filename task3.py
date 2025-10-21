from csv import reader

output = open('bibliographic_references.txt', 'w')


def generate_bibliographic_references():
    with open('books.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')

        for i, row in enumerate(table):
            if i >= 20:
                break   
            author = row[row[3]]
            name = row[row[1]]
            year = row[row[6]]
            reference = f"{author}. {name} - {year}"
            yield reference
            output.write(f'{reference}\n')

print(f'{output}')
output.close()