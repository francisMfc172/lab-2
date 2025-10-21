import csv

csv_file_path = 'books-en.csv'

unique_publishers = set()

with open(csv_file_path, 'r', encoding='windows-1251', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        publisher = row.get('publisher', None)
        if publisher:
            unique_publishers.add(publisher)

unique_publishers_list = list(unique_publishers)

for publisher in unique_publishers_list:
    print(publisher)