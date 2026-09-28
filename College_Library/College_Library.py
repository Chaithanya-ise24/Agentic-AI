from datetime import datetime, timedelta
books = {
    "B001": {"title": "Python Programming", "author": "Guido van Rossum", "available": True, "issued_to": "", "due_date": ""},
    "B002": {"title": "Java Programming", "author": "James Gosling", "available": True, "issued_to": "", "due_date": ""},
    "B003": {"title": "Data Structures", "author": "Seymour Lipschutz", "available": True, "issued_to": "", "due_date": ""},
    "B004": {"title": "Database Management System", "author": "Raghu Ramakrishnan", "available": True, "issued_to": "", "due_date": ""},
    "B005": {"title": "Computer Networks", "author": "Andrew Tanenbaum", "available": True, "issued_to": "", "due_date": ""},
    "B006": {"title": "Operating Systems", "author": "Abraham Silberschatz", "available": True, "issued_to": "", "due_date": ""},
    "B007": {"title": "Machine Learning", "author": "Tom Mitchell", "available": True, "issued_to": "", "due_date": ""},
    "B008": {"title": "Artificial Intelligence", "author": "Stuart Russell", "available": True, "issued_to": "", "due_date": ""},
    "B009": {"title": "Web Technology", "author": "Jeffrey C. Jackson", "available": True, "issued_to": "", "due_date": ""},
    "B010": {"title": "Software Engineering", "author": "Ian Sommerville", "available": True, "issued_to": "", "due_date": ""}
}
students = {}
def register_student():
    student_id = input("\nEnter Student ID: ").strip().upper()
    if student_id == "":
        print("Student ID cannot be empty.")
        return
    if student_id in students:
        print("Student already registered.")
        return
    name = input("Enter Student Name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    students[student_id] = {"name": name, "books": []}
    print("\nStudent registered successfully!")
    print("--------------------------------")
    print("Student ID :", student_id)
    print("Name       :", name)
def show_books():
    print("\n" + "=" * 70)
    print("                     ALL BOOKS")
    print("=" * 70)
    for book_id, book in books.items():
        if book["available"]:
            status = "AVAILABLE"
        else:
            status = "ISSUED"
        print("\nBook ID :", book_id)
        print("Title   :", book["title"])
        print("Author  :", book["author"])
        print("Status  :", status)
        print("-" * 50)
def search_book():
    keyword = input("\nEnter book title or author: ").strip().lower()
    if keyword == "":
        print("Please enter a search keyword.")
        return
    found = False
    for book_id, book in books.items():
        if keyword in book["title"].lower() or keyword in book["author"].lower():
            if book["available"]:
                status = "Available"
            else:
                status = "Issued"
            print("\nBook ID :", book_id)
            print("Title   :", book["title"])
            print("Author  :", book["author"])
            print("Status  :", status)
            print("-" * 50)
            found = True
    if not found:
        print("\nNo matching book found.")
def issue_book():
    student_id = input("\nEnter Student ID: ").strip().upper()
    if student_id not in students:
        print("Student not registered.")
        print("Please register first.")
        return
    student = students[student_id]
    if len(student["books"]) >= 3:
        print("You have already borrowed 3 books.")
        print("Return a book before issuing another.")
        return
    book_id = input("Enter Book ID: ").strip().upper()
    if book_id not in books:
        print("Invalid Book ID.")
        return
    book = books[book_id]
    if not book["available"]:
        print("Sorry, this book is already issued.")
        return
    due_date = datetime.now() + timedelta(days=14)
    book["available"] = False
    book["issued_to"] = student_id
    book["due_date"] = due_date.strftime("%Y-%m-%d")
    student["books"].append(book_id)
    print("\nBOOK ISSUED SUCCESSFULLY!")
    print("--------------------------------")
    print("Book      :", book["title"])
    print("Student   :", student["name"])
    print("Student ID:", student_id)
    print("Due Date  :", book["due_date"])
def return_book():
    student_id = input("\nEnter Student ID: ").strip().upper()
    if student_id not in students:
        print("Student not found.")
        return
    book_id = input("Enter Book ID: ").strip().upper()
    if book_id not in books:
        print("Invalid Book ID.")
        return
    book = books[book_id]
    if book["available"]:
        print("This book is already in the library.")
        return
    if book["issued_to"] != student_id:
        print("This book was not issued to this student.")
        return
    today = datetime.now().date()
    due_date = datetime.strptime(book["due_date"], "%Y-%m-%d").date()
    late_days = (today - due_date).days
    if late_days > 0:
        fine = late_days * 2
    else:
        fine = 0
    book["available"] = True
    book["issued_to"] = ""
    book["due_date"] = ""
    students[student_id]["books"].remove(book_id)
    print("\nBOOK RETURNED SUCCESSFULLY!")
    print("--------------------------------")
    if fine > 0:
        print("Late Days :", late_days)
        print("Fine      : Rs.", fine)
    else:
        print("No fine. Book returned on time!")
def student_details():
    student_id = input("\nEnter Student ID: ").strip().upper()
    if student_id not in students:
        print("Student not found.")
        return
    student = students[student_id]
    print("\n========== STUDENT DETAILS ==========")
    print("Student ID :", student_id)
    print("Name       :", student["name"])
    print("\nBorrowed Books:")
    if len(student["books"]) == 0:
        print("No books currently borrowed.")
    else:
        for book_id in student["books"]:
            book = books[book_id]
            print(book_id, "-", book["title"], "(Due:", book["due_date"], ")")
def issued_books():
    print("\n========== ISSUED BOOKS ==========")
    found = False
    for book_id, book in books.items():
        if not book["available"]:
            student_id = book["issued_to"]
            student = students.get(student_id)
            if student:
                print("\nBook       :", book["title"])
                print("Book ID    :", book_id)
                print("Student    :", student["name"])
                print("Student ID :", student_id)
                print("Due Date   :", book["due_date"])
                print("-" * 40)
                found = True
    if not found:
        print("No books are currently issued.")
def statistics():
    total = len(books)
    available = 0
    issued = 0
    for book in books.values():
        if book["available"]:
            available += 1
        else:
            issued += 1
    total_students = len(students)
    print("\n========== LIBRARY STATISTICS ==========")
    print("Total Books          :", total)
    print("Available Books      :", available)
    print("Issued Books         :", issued)
    print("Registered Students  :", total_students)
def library_info():
    print("\n========================================")
    print("          COLLEGE LIBRARY")
    print("========================================")
    print("Library Timings     : 9:00 AM - 6:00 PM")
    print("Working Days        : Monday - Saturday")
    print("Maximum Books       : 3 per student")
    print("Borrowing Period    : 14 days")
    print("Late Fine           : Rs. 2 per day")
    print("========================================")
print("\n==========================================")
print("        COLLEGE LIBRARY MANAGEMENT")
print("==========================================")
while True:
    print("\n========== MAIN MENU ==========")
    print("1. Register Student")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Student Details")
    print("7. Show Issued Books")
    print("8. Library Statistics")
    print("9. Library Information")
    print("0. Exit")
    print("===============================")
    choice = input("Enter your choice: ").strip()
    if choice == "1":
        register_student()
    elif choice == "2":
        show_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        issue_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        student_details()
    elif choice == "7":
        issued_books()
    elif choice == "8":
        statistics()
    elif choice == "9":
        library_info()
    elif choice == "0":
        print("\nThank you for using the College Library Management System!")
        break
    else:
        print("\nInvalid choice. Please enter a number from 0 to 9.")
    