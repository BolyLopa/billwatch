# === Stage 41: Add plain text import for a simple line-based format ===
# Project: BillWatch
def read_bills_from_file(filename):
    """Read bills from a plain text file in a simple line-based format.
    
    Each line represents a bill in the format:
    due_date,payment_status,amount,categories
    
    Example:
    2024-01-15,paid,150.00,electricity,water
    2024-02-01,pending,75.50,internet,phone
    
    Returns a list of bill dictionaries.
    """
    bills = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            
            parts = line.split(',')
            if len(parts) >= 4:
                bill = {
                    'due_date': parts[0].strip(),
                    'payment_status': parts[1].strip(),
                    'amount': float(parts[2].strip()),
                    'categories': [cat.strip() for cat in parts[3:]]
                }
                bills.append(bill)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid amount format in file.")
    
    return bills
