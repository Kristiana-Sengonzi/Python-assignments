# Student Record Management System Report

## Introduction

This project implements a menu-driven Student Record Management System using Python. The purpose of the system is to manage student records while demonstrating the use of file handling, object-oriented programming, exception handling, logging, and input validation. The application stores basic student information in a CSV file and additional student information in a JSON file.

## Program Design

The system is built around a `StudentManager` class which contains all the functions required to manage student records. The class performs the following operations:

* Add a new student
* View all students
* Search for a student by registration number
* Update student details
* Delete a student record

The application uses two different file formats for storage:

* **students.csv** stores the student's registration number and name.
* **students.json** stores additional details such as address, contact number, and program using the registration number as the key.

This design reduces redundancy because the student's additional information is separated from the basic information while still being linked through the registration number.

## Key Functions

### add_student()

This function validates that the registration number does not already exist, saves the student's registration number and name into the CSV file, stores the remaining details inside the JSON file, records the action in the log file, and informs the user whether the operation was successful.

### view_students()

This function reads all student records from the CSV file and loads the JSON file once. It combines information from both files using the registration number before displaying complete student details.

### search_students()

The search function searches the CSV file for the registration number entered by the user. If the student exists, the additional details are retrieved from the JSON file and displayed. If the student does not exist, a custom exception is raised.

### update_student()

This function allows the user to modify the student's information. Existing values may be kept by pressing Enter. After updating, both the CSV and JSON files are saved with the new information.

### delete_student()

This function removes the student's basic information from the CSV file and removes the corresponding entry from the JSON file before saving both files.

## Exception Handling Strategy

The application uses several exception handling techniques.

* **try** blocks are used whenever file operations or searches are performed.
* **except** blocks handle file errors, invalid JSON data, and unexpected runtime errors.
* **finally** is used in the add student operation to ensure a separator is printed after execution regardless of success or failure.
* A custom exception named `StudentNotFoundError` is raised whenever a student record cannot be found. This provides meaningful feedback to the user instead of displaying a generic Python error.

## Logging

Python's logging module is used to record important system events. Examples of logged actions include:

* Student added successfully
* Student searched
* Student updated
* Student deleted
* Search failures
* System errors

The log file (`student_system.log`) helps keep a record of user activity and assists in debugging if problems occur.

## Testing

The program was tested using several scenarios.

| Test Case                   | Expected Result                    | Outcome |
| --------------------------- | ---------------------------------- | ------- |
| Add a new student           | Student saved successfully         | Passed  |
| View all students           | All records displayed              | Passed  |
| Search existing student     | Student information displayed      | Passed  |
| Search missing student      | Custom exception message displayed | Passed  |
| Update student              | Student information updated        | Passed  |
| Delete student              | Student removed from both files    | Passed  |
| Invalid registration number | Validation message displayed       | Passed  |

## Conclusion

The Student Record Management System successfully demonstrates the use of object-oriented programming, CSV and JSON file handling, exception handling, logging, and user input validation. Separating the student information between CSV and JSON files provides an organized structure while allowing efficient retrieval of complete student records through the registration number.

