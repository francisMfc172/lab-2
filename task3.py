import random
from csv import reader

def refs(file, records=20):
    references = []
    try:
        
        with open(file, 'r') as csvfile:
            
            table = list(reader(csvfile, delimiter=';'))

            # Select random sample of records (up to 20 or file size if smaller)
            data = random.sample(table, min(records, len(table)))
            
            # Process each randomly selected row
            for row in data:
                # Extract author from column 3 (index 2), default if missing
                author = row[2] if len(row) > 2 else "Unknown Author"
                # Extract title from column 2 (index 1), default if missing
                title = row[1] if len(row) > 1 else "Unknown Title"
                # Extract year from column 5 (index 4), default if missing
                year = row[4] if len(row) > 4 else "Unknown Year"
                # Format the bibliographic reference
                reference = f"{author}. {title} - {year}"
                references.append(reference)
        
        # Write all references to output file
        with open('bibliographic_references.txt', 'w') as output_file:
            # Number each reference starting from 1
            for i, ref in enumerate(references, 1):
                output_file.write(f"{i}. {ref}\n")

        print("Bibliographic references saved to bibliographic_references.txt.")
    
    except FileNotFoundError:
        print("the specified CSV file was not found.")
    except Exception:
        print("an error occured")

# Call the function with the CSV file
refs('books-en.csv')
