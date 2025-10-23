from csv import reader
import sys

def search_books(file, author, min_price=200):
    """Search for books by author with price above minimum threshold."""
    results = []
    
    try:
        with open(file, 'r', encoding='utf-8') as csvfile:
            table = reader(csvfile, delimiter=';')
            
            # Skip header if exists
            header = next(table, None)
            
            for row in table:
                # Check if row has enough columns and author matches
                if len(row) > 6 and author.lower() in row[2].lower():
                    try:
                        price = float(row[6].replace(',', '.'))
                        if price >= min_price:
                            results.append(row)
                    except (ValueError, IndexError):
                        print(f'Invalid price in row: {row}')
                        
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []
    
    return results

def main():
    file = 'books-en.csv'
    author = input('Enter author\'s name to search: ').strip()
    
    if not author:
        print("Please enter a valid author name.")
        return
    
    results = search_books(file, author)
    
    if results:
        print(f'\033[44mBooks by {author} priced 200 or higher:\033[0m')
        
        for row in results:
            print(f'Title: {row[1]}, Author: {row[2]}, Price: {row[6]}')
        
        print(f'Total books found: {len(results)}')
    else:
        print(f'No books found by "{author}" priced 200 or higher.')

if __name__ == "__main__":
    main()
