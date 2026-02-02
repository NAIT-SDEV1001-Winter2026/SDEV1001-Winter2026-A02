student_grades = [88, 65, 91, 72, 98]

print("Our student grades are: ")
print(student_grades)

print("Our student grades sorted are: ")
student_grades.sort(reverse=True)
print(student_grades)

# Let's add 100 to the student grades.
student_grades.append(100)
student_grades.insert(2,50)
print("After we've added grades, the new list is: ")
print(student_grades)

# Let's remove a few items from the list.
student_grades.pop(3) # remove at index 2
student_grades.remove(98) # remove the value 98 from the list.
print("After we've removed grades, the new list is: ")
print(student_grades)

# Show students the value error on the next line.
# student_grades.remove(9001)

# other code removed for brevity
print("Has a student got a perfect grade?")
print(100 in student_grades)
print("Has a student gotten a 0 in the course?")
print(0 in student_grades)