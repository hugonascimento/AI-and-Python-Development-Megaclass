# Create a program that stores student grades in a dictionary and calculate the average grade.
# The program should ask the user to enter the student name (only letters allowed) and their grade.
# The user should be able to enter multiple students and their grades.
# The program should then calculate and display the average grade of all students.
# The program should also display the student with the highest grade and the student with the lowest grade.
# The program should also display the total number of students.

student_grades = {}

while True:
    name = input("Enter student name (or 'done' to finish): ")
    if name.lower() == 'done':
       break
    # Check if the input contains only letters
    if not name.replace(" ", "").isalpha():
        print("Invalid input. Please enter a valid name.")
        continue
    
    # Check if the name already exists in the dictionary
    if name in student_grades:
        print(f"Student {name} already exists. Please enter a different name.")
        continue
    
    try:
        # Ask for grades for 4 semesters
        grades = []
        
        # Loop to get grades for 4 semesters
        for i in range(1, 5):
            grade = float(input(f"Enter your semester {i} grade for {name}: "))
            grades.append(grade)
        student_grades[name] = grades
        
    except ValueError:
        print("Invalid input. Please enter a numeric grade.")
       
if not student_grades:
    print("No students entered, exiting...")
    
else:
    # Count the total number of students
    total_students = len(student_grades)
    
    # Calculate the average grade for each student
    average_grades = {student: sum(grades) / len(grades) for student, grades in student_grades.items()}
    
    # Find the student with the highest grades
    highest_student = max(student_grades, key=lambda x: max(student_grades[x]))
    
    # Find the student with the lowest grades
    lowest_student = min(student_grades, key=lambda x: min(student_grades[x]))
    
    # Get the highest grades
    highest_grade = max(student_grades[highest_student])
    
    # Get the lowest grades
    lowest_grade = min(student_grades[lowest_student])

    print(f"Total number of students: {total_students}")
    print("Average grade of each student:")
    
    # Display the average grades for each student
    for student, avg in average_grades.items():
        print(f"{student}: {avg:.2f}")

    print(f"Student with the highest grade: {highest_student} with a grade of {highest_grade:.2f}")
    print(f"Student with the lowest grade: {lowest_student} with a grade of {lowest_grade:.2f}")
