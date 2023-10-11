import re

class Validator:
    @staticmethod
    def validate_name(name):
        return bool(re.match("^[a-zA-Z]+$", name))

    @staticmethod
    def validate_age(age):
        return 0 < age < 150

    @staticmethod
    def validate_passport(passport):
        return bool(re.match("^[A-Z]{2}\d{6}$", passport))

class COVID_CERTIFICATE:
    def __init__(self, ID, username, international_passport, start_date, end_date, date_of_birth, vaccine):
        self.ID = ID
        self.username = username
        self.international_passport = international_passport
        self.start_date = start_date
        self.end_date = end_date
        self.date_of_birth = date_of_birth
        self.vaccine = vaccine

    def __str__(self):
        return f"ID: {self.ID}, Username: {self.username}, Passport: {self.international_passport}, " \
               f"Start Date: {self.start_date}, End Date: {self.end_date}, DOB: {self.date_of_birth}, Vaccine: {self.vaccine}"

class Collection:
    def __init__(self):
        self.certificates = []

    def load_certificates_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    if len(data) == 7:
                        ID, username, passport, start_date, end_date, dob, vaccine = data
                        certificate = COVID_CERTIFICATE(ID, username, passport, start_date, end_date, dob, vaccine)
                        self.certificates.append(certificate)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def add_certificate(self, certificate):
        self.certificates.append(certificate)
        self.save_to_file('certificates.txt')  

    def remove_certificate_by_id(self, ID):
        self.certificates = [cert for cert in self.certificates if cert.ID != ID]
        self.save_to_file('certificates.txt')  

    def edit_certificate_by_id(self, ID, new_data):
        for certificate in self.certificates:
            if certificate.ID == ID:
                for field, value in new_data.items():
                    setattr(certificate, field, value)
        self.save_to_file('certificates.txt') 

    def search_certificates(self, keyword):
        return [cert for cert in self.certificates if keyword.lower() in cert.__dict__.values()]

    def sort_certificates(self, field):
        self.certificates.sort(key=lambda certificate: getattr(certificate, field))

    def display_certificates(self):
        for certificate in self.certificates:
            print(certificate)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for certificate in self.certificates:
                file.write(f"{certificate.ID},{certificate.username},{certificate.international_passport},"
                           f"{certificate.start_date},{certificate.end_date},{certificate.date_of_birth},{certificate.vaccine}\n")

def main():
    collection = Collection()
    collection.load_certificates_from_file('certificates.txt')

    while True:
        print("\nCOVID Certificate Management System")
        print("1. Add Certificate")
        print("2. Remove Certificate by ID")
        print("3. Edit Certificate by ID")
        print("4. Search Certificates")
        print("5. Sort Certificates")
        print("6. Display Certificates")
        print("7. Save to File")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ID = input("Enter ID: ")
            username = input("Enter Username: ")
            international_passport = input("Enter Passport Number: ")
            start_date = input("Enter Start Date: ")
            end_date = input("Enter End Date: ")
            date_of_birth = input("Enter Date of Birth: ")
            vaccine = input("Enter Vaccine: ")
            certificate = COVID_CERTIFICATE(ID, username, international_passport, start_date, end_date, date_of_birth, vaccine)
            collection.add_certificate(certificate)
            print("Certificate added successfully.")

        elif choice == "2":
            ID = input("Enter ID to remove: ")
            collection.remove_certificate_by_id(ID)
            print("Certificate removed successfully.")

        elif choice == "3":
            ID = input("Enter ID to edit: ")
            new_data = {}
            new_data['username'] = input("Enter new Username: ")
            new_data['international_passport'] = input("Enter new Passport Number: ")
            new_data['start_date'] = input("Enter new Start Date: ")
            new_data['end_date'] = input("Enter new End Date: ")
            new_data['date_of_birth'] = input("Enter new Date of Birth: ")
            new_data['vaccine'] = input("Enter new Vaccine: ")
            collection.edit_certificate_by_id(ID, new_data)
            print("Certificate edited successfully.")

        elif choice == "4":
            keyword = input("Enter search keyword: ")
            results = collection.search_certificates(keyword.lower())
            print("\nSearch Results:")
            if results:
                for result in results:
                    print(result)
            else:
                print("No matching certificates found.")

        elif choice == "5":
            field = input("Enter field to sort by: ")
            collection.sort_certificates(field)
            print("Certificates sorted successfully.")

        elif choice == "6":
            collection.display_certificates()

        elif choice == "7":
            filename = input("Enter filename to save: ")
            collection.save_to_file(filename)
            print("Certificates saved to file successfully.")

        elif choice == "8":
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()
