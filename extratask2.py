import csv

def topbooks(file):

    publishers = set()  
    books = []       

    try:
        # Open and read the CSV file
        with open(file, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';') 

            # Process each row in the CSV
            for row in reader:
                # Skip rows that don't have enough columns (at least 7)
                if len(row) < 7:
                    continue 

                #  Unpack row into meaningful variables
                isbn, title, author, year, publisher, downloads, price = row
                
                # Add publisher to set (automatically handles duplicates)
                publishers.add(publisher)

                #  Convert downloads to integer and add book to list
                try:
                    downloads_count = int(downloads)
                    books.append((title, author, publisher, downloads_count))
                except ValueError:
                    print(f"invalid downloads value: {downloads}")

        # Sort books by downloads (descending) and take top 20
        book_list = sorted(books, key=lambda x: x[3], reverse=True)[:20]

        #  Print all unique publishers in alphabetical order
        print("Publishers:")
        for publisher in sorted(publishers):
            print(publisher)

        #  Print top 20 most downloaded books
        print("\nTop 20 Most Popular Books (by Downloads):")
        for book in book_list:
            print(f"Title: {book[0]}, Author: {book[1]}, Publisher: {book[2]}, Downloads: {book[3]}")

    except FileNotFoundError:
        print("CSV file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


topbooks('books-en.csv')


