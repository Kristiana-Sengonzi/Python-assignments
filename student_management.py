import csv
import json
import logging
import os

# Configure Logging
logging.basicConfig(
    filename="student_system.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception
class StudentNotFoundError(Exception):
    """Exception raised when a student record cannot be found in the system."""
    def __init__(self, reg_no):
        self.reg_no = reg_no
        super().__init__(f"Student with Registration Number {reg_no} not found.")


def get_input(prompt):
    """Validates and collects menu options."""
    options = ["1", "2", "3", "4", "5", "6"]
    while True:
        selection = input(prompt).strip()
        if selection in options:
            return selection
        print("Please enter a valid option (1-6).")


def get_no(prompt):
    """Validates registration numbers ensuring they are exactly 10 digits."""
    while True:
        reg_no = input(prompt).strip()
        if len(reg_no) != 10 or not reg_no.isdigit():
            print("Invalid input. Enter a valid 10-digit numeric registration number.")
        else:
            return reg_no


class StudentManager:
    def __init__(self):
        self.csv_file = "System/students.csv"
        self.json_file = "System/students.json"
       
    def _initialize_files(self):
        """Ensures storage files exist with baseline layouts."""
        try:
            if not os.path.exists(self.csv_file):
                with open(self.csv_file, "w", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow(["Registration Number", "Name"])
            if not os.path.exists(self.json_file):
                with open(self.json_file, "w") as file:
                    json.dump({}, file)
        except Exception as e:
            logging.error(f"Failed to initialize storage files: {str(e)}")
            print("System Error: Could not initialize storage systems.")

    def _load_json(self):
        """Helper to read JSON file securely."""
        try:
            with open(self.json_file, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_json(self, data):
        """Helper to write to JSON file securely."""
        with open(self.json_file, "w") as file:
            json.dump(data, file, indent=4)

    def _read_csv(self):
        """Helper to read all rows from CSV file."""
        records = []
        if os.path.exists(self.csv_file):
            with open(self.csv_file, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)  # Skip header row
                for row in reader:
                    if row:
                        records.append(row)
        return records

    def _write_csv(self, records):
        """Helper to write all rows back to CSV file."""
        with open(self.csv_file, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Registration Number", "Name"])
            writer.writerows(records)

    def add_student(self, name, reg_no, address, contact, program):
        try:
            records = self._read_csv()
            # Check for duplicate Registration Number
            if any(row[0] == reg_no for row in records):
                print(f"Error: A student with Registration Number {reg_no} already exists.")
                return False

            # Write to CSV
            with open(self.csv_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([reg_no, name])

            # Write to JSON
            details = self._load_json()
            details[reg_no] = {
                "address": address,
                "contact": contact,
                "program": program
            }
            self._save_json(details)

            logging.info(f"Successfully added student: {reg_no} - {name}")
            print("Student added successfully!")
            return True
        except Exception as e:
            logging.error(f"Error adding student {reg_no}: {str(e)}")
            print("An unexpected error occurred while adding the student.")
        finally:
            print("-" * 30)

    def view_students(self):
        try:
            records = self._read_csv()
            details = self._load_json()

            if not records:
                print("No student records found.")
                return

            print("\n--- All Student Records ---")
            for row in records:
                reg_no, name = row[0], row[1]
                print(f"Registration Number : {reg_no}")
                print(f"Name                : {name}")
                if reg_no in details:
                    print(f"Address             : {details[reg_no].get('address', 'N/A')}")
                    print(f"Contact             : {details[reg_no].get('contact', 'N/A')}")
                    print(f"Program             : {details[reg_no].get('program', 'N/A')}")
                print("-" * 30)
            logging.info("Viewed all student records.")
        except Exception as e:
            logging.error(f"Error viewing students: {str(e)}")
            print("An error occurred while loading student records.")

    def search_students(self, reg_no):
        try:
            records = self._read_csv()
            details = self._load_json()

            for row in records:
                if row[0] == reg_no:
                    print(f"\nStudent Found:")
                    print(f"Registration Number : {row[0]}")
                    print(f"Name                : {row[1]}")
                    if reg_no in details:
                        print(f"Address             : {details[reg_no].get('address', 'N/A')}")
                        print(f"Contact             : {details[reg_no].get('contact', 'N/A')}")
                        print(f"Program             : {details[reg_no].get('program', 'N/A')}")
                    logging.info(f"Searched and found student: {reg_no}")
                    return True
            
            raise StudentNotFoundError(reg_no)
        except StudentNotFoundError as snfe:
            logging.warning(str(snfe))
            print(snfe)
            return False
        except Exception as e:
            logging.error(f"Error searching for student {reg_no}: {str(e)}")
            print("An error occurred during search.")
            return False

    def update_student(self, reg_no):
        try:
            records = self._read_csv()
            details = self._load_json()

            student_index = -1
            for i, row in enumerate(records):
                if row[0] == reg_no:
                    student_index = i
                    break

            if student_index == -1:
                raise StudentNotFoundError(reg_no)

            print("\nLeave blank and press enter to keep existing details.")
            new_name = input(f"Enter new name (Current: {records[student_index][1]}): ").strip()
            if new_name:
                records[student_index][1] = new_name

            current_details = details.get(reg_no, {})
            new_address = input(f"Enter new address (Current: {current_details.get('address', '')}): ").strip()
            new_contact = input(f"Enter new contact (Current: {current_details.get('contact', '')}): ").strip()
            new_program = input(f"Enter new program (Current: {current_details.get('program', '')}): ").strip()

            if reg_no not in details:
                details[reg_no] = {}
            if new_address: details[reg_no]['address'] = new_address
            if new_contact: details[reg_no]['contact'] = new_contact
            if new_program: details[reg_no]['program'] = new_program

            self._write_csv(records)
            self._save_json(details)
            logging.info(f"Updated details for student: {reg_no}")
            print("Student records updated successfully!")
            return True
        except StudentNotFoundError as snfe:
            logging.warning(str(snfe))
            print(snfe)
            return False
        except Exception as e:
            logging.error(f"Error updating student {reg_no}: {str(e)}")
            print("An error occurred while updating the student record.")
            return False

    def delete_student(self, reg_no):
        try:
            records = self._read_csv()
            details = self._load_json()

            updated_records = [row for row in records if row[0] != reg_no]

            if len(records) == len(updated_records):
                raise StudentNotFoundError(reg_no)

            if reg_no in details:
                del details[reg_no]

            self._write_csv(updated_records)
            self._save_json(details)
            logging.info(f"Deleted student record for: {reg_no}")
            print("Student record deleted successfully.")
            return True
        except StudentNotFoundError as snfe:
            logging.warning(str(snfe))
            print(snfe)
            return False
        except Exception as e:
            logging.error(f"Error deleting student {reg_no}: {str(e)}")
            print("An error occurred while deleting the student record.")
            return False


def main():
    s1 = StudentManager()
    
    while True:
        print("\n=== Student Management System ===")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student by registration number")
        print("4. Update student details")
        print("5. Delete a student record")
        print("6. Exit")

        selection = get_input("Select one of the options (1-6): ")

        if selection == "1":
            name = input("Enter name: ").strip()
            reg_no = get_no("Enter 10-digit registration number: ")
            address = input("Enter address: ").strip()
            contact = input("Enter contact number: ").strip()
            program = input("Enter program: ").strip()
            s1.add_student(name, reg_no, address, contact, program)

        elif selection == "2":
            s1.view_students()

        elif selection == "3":
            reg_no = get_no("Enter registration number to search: ")
            s1.search_students(reg_no)

        elif selection == "4":
            reg_no = get_no("Enter registration number to update: ")
            s1.update_student(reg_no)

        elif selection == "5":
            reg_no = get_no("Enter registration number to delete: ")
            s1.delete_student(reg_no)

        elif selection == "6":
            print("Exiting system. Goodbye!")
            logging.info("System closed normally by user choice.")
            break


if __name__ == "__main__":
    main()