import csv

def add_student():
    with open("students.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        name = input("Enter student's name: ")
        roll = input("Enter roll number: ")
        grade = input("Enter grade: ")
        writer.writerow([name, roll, grade])
        print("Student added successfully!")

def view_students():
    try:
        with open("students.csv", mode='r') as file:
            reader = csv.reader(file)
            print("Name\tRoll No\tGrade")
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("No student records found.")

def main():
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
