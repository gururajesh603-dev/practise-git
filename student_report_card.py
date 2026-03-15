# Student Report Card Generator
def get_marks(subject):
    while True:
        mark = int(input(f"Enter {subject} Marks: "))

        if mark < 0:
            print("Marks should be 0 to 100 only")
        elif mark > 100:
            print("Marks should not exceed 100")
        else:
            return mark

def get_name():
    while True:
        name = input("Enter Student Name: ")

        if any(char.isdigit() for char in name):
            print("Numbers are not allowed in the name")
        else:
            return name

def get_student_id():
    while True:
        student_id = input("Enter Student Identity: ")

        if " " in student_id:
            print("Spaces are not allowed in the register number")
        else:
            return student_id

def calculate_grade(avg, marks):

    # If any subject < 50 → Fail
    if any(mark < 50 for mark in marks.values()):
        return "Fail"

    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


def print_report(student_id, name, marks, average, grade):

    print("\n========== STUDENT REPORT CARD ==========")
    print(f"Student ID : {student_id}")
    print(f"Name       : {name}")

    print("\nMarks:")
    for subject, mark in marks.items():
        print(f"{subject:<10}: {mark}")

    print("\nAverage Marks :", round(average, 2))
    print("Grade         :", grade)
    print("=========================================")


def main():

    while True:

        student_id = get_student_id()
        name = get_name()

        # Get marks with validation
        math = get_marks("Math")
        science = get_marks("Science")
        english = get_marks("English")
        history = get_marks("History")

        # Store in dictionary
        marks = {
            "Math": math,
            "Science": science,
            "English": english,
            "History": history
        }

        # Calculate average
        average = sum(marks.values()) / len(marks)

        # Calculate grade
        grade = calculate_grade(average, marks)

        # Print report
        print_report(student_id, name, marks, average, grade)

        again = input("\nDo you want to enter another student? (yes/no): ")

        if again.lower() != "yes":
            print("Program Ended.")
            break


main()