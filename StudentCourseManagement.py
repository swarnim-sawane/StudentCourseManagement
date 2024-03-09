class Student:
    def __init__(self, Name, ID, Gender):
        self.Name = Name
        self.ID = ID
        self.Gender = Gender
        self.marks = {}
    
    def addMarks(self, course, course_marks):
        self.marks[course] = course_marks
    
    def calcGPA(self):
        total_sub = len(self.marks)
        total_marks = 0;
        for i in self.marks.values():
            total_marks += i
        GPA = total_marks / total_sub
        return GPA

class Course:
    def __init__(self, course, students):
        self.course = course
        self.students = []
    
    def addStudent(self, student):
        self.students.append(student)
    
    def removeStudent(self, student):
        if student in self.students:
            self.students.remove(student)
    
    def calcAvgGPA(self):
        total_GPA = 0
        for student in self.students:
            total_GPA += student.calcGPA()
        avgGPA = total_GPA / len(self.students)
        return avgGPA


student1 = Student("A", 123, "F")

student1.addMarks("CS", 85)
student1.addMarks("Math", 90)

student_gpa = student1.calcGPA()
print("Student GPA:", student_gpa)
