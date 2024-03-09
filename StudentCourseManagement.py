class Student:
    def __init__(self, Name, ID, Gender):
        self.Name = Name
        self.ID = ID
        self.Gender = Gender
        self.marks = []
    
    def addMarks(self, course, course_marks):
        self.marks.append(course_marks)
    
    def calcGPA(self):
        total_sub = len(self.marks)
        for i in self.marks:
            total_marks += i
        GPA = total_marks / total_sub
        return GPA

class Course:
    def __init__(self, course, students):
        self.course = course
        self.students = []
    
    def addStudent(self, name):
        self.students.append(name)
    
    def removeStudent(self, name):
        if name in self.students:
            self.students.remove(name)
    
    def calcAvgGPA(self):
        total_GPA = 0
        for student in self.students:
            total_GPA += student.calcGPA()
        AvgGPA = total_GPA / len(self.students)
        return AvgGPA
