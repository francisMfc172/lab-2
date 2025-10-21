import csv

csv_file_path = 'books-en.csv'

books = []
with open(csv_file_path, 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        books.append(row)

books.sort(key=lambda x: float(x.get('downloads', 0)), reverse=True)

print("The 20 most popular books:")
for book in books[:20]:
    print(f"Title: {book.get('Book-Title')}, Rating: {book.get('Downloads')}")

