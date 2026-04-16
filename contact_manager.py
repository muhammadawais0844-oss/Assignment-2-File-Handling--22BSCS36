import csv
import os

# Path configuration
DATA_FILE = "../data/contacts.csv"

def initialize_file():
    """Ensure the data directory and file exist."""
    os.makedirs("../data", exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Phone", "Email"]) # Header

def add_contact():
    """CREATE: Append a new contact."""
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    try:
        with open(DATA_FILE, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([name, phone, email])
        print("Contact saved successfully!")
    except IOError as e:
        print(f"File Error: Could not write to file. {e}")

def view_contacts():
    """READ: Display all contacts."""
    try:
        with open(DATA_FILE, 'r') as f:
            reader = csv.reader(f)
            next(reader) # Skip header
            print("\n--- Contact List ---")
            for row in reader:
                print(f"Name: {row[0]} | Phone: {row[1]} | Email: {row[2]}")
    except FileNotFoundError:
        print("Error: No data file found. Add a contact first.")

def update_contact():
    """UPDATE: Modify existing data."""
    target = input("Enter the Name of the contact to update: ")
    updated_rows = []
    found = False
    try:
        with open(DATA_FILE, 'r') as f:
            rows = list(csv.reader(f))
            updated_rows.append(rows[0]) # Keep header
            for row in rows[1:]:
                if row[0].lower() == target.lower():
                    row[1] = input(f"New Phone (current {row[1]}): ")
                    row[2] = input(f"New Email (current {row[2]}): ")
                    found = True
                updated_rows.append(row)
        
        if found:
            with open(DATA_FILE, 'w', newline='') as f:
                csv.writer(f).writerows(updated_rows)
            print("Update complete!")
        else:
            print("Contact not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_contact():
    """DELETE: Remove a contact."""
    target = input("Enter Name to delete: ")
    try:
        with open(DATA_FILE, 'r') as f:
            rows = list(csv.reader(f))
        
        new_rows = [rows[0]] + [r for r in rows[1:] if r[0].lower() != target.lower()]
        
        if len(new_rows) < len(rows):
            with open(DATA_FILE, 'w', newline='') as f:
                csv.writer(f).writerows(new_rows)
            print("Contact deleted.")
        else:
            print("Contact not found.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    initialize_file()
    while True:
        print("\n=== CONTACT MANAGER ===")
        print("1. Add | 2. View | 3. Update | 4. Delete | 5. Exit")
        choice = input("Select: ")
        if choice == '1': add_contact()
        elif choice == '2': view_contacts()
        elif choice == '3': update_contact()
        elif choice == '4': delete_contact()
        elif choice == '5': break
        else: print("Invalid choice!")

if __name__ == "__main__":
    main()