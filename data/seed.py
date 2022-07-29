import csv
import os
    
def populate_users():
    delete_users_file()
    with open('users.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        header = ("id", "first_name", "last_name", "user_name")
        writer.writerows([
            header,
            (1, "Jacob", "Goldfarb", "jacobjr23"),
            (2, "Alex", "Lars", "abenlars"),
            (3, "Christina", "Lim", "clim")
        ])
        
def populate_addresses():
    delete_addresses_file()
    with open('addresses.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        header = ("id", "user_id", "address_1", "city", "country")
        writer.writerows([
            header,
            (1, 2, "56 Ridley Blvd.", "Toronto", "Canada"),
            (2, 3, "36 Maplewood Cr.", "North Bay", "Canada"),
            (3, 1, "31 Oakdale Rd.", "London", "England")
        ])
        
def delete_file(file_name):
    if os.path.isfile(file_name):
        os.remove(file_name)

def delete_users_file():
    delete_file("./users.csv")

def delete_addresses_file():
    delete_file("./addresses.csv")
        
def main():
    populate_users()
    populate_addresses()
    
if __name__ == "__main__": main()