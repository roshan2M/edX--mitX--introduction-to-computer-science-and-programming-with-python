# Lecture 12.1, slide 2
# This is a package containing the class hierarchy Person -> MITPerson -> Student -> UnderGraduate / Graduate / TransferStudent.

import datetime

class Person(object):
    def __init__(self, name):
        """
        Create a person called name
        """
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    
    def getLastName(self):
        """
        Returns self's last name
        """
        return self.lastName
    
    def __str__(self):
        """
        Returns self's full name
        """
        return self.name
    
    def setBirthday(self, month, day, year):
        """
        Sets self's birthday to birthDate
        """
        if self.birthday == None:
            raise ValueError
        return datetime.date(year, month, day)
    
    def getAge(self):
        """
        Returns self's current age in days
        """
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """
        Return True if self's name is lexicographically
        less than other's name, and False otherwise
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

me = Person('Roshan Munjal')
# print me
foo = 'Roshan Munjal'
# foo.split(' ')
# foo.split(' ')[-1]
# me.getLastName()
# me.setBirthday(1999, 2, 3)
# me.birthday()
# me.getAge()
# me.getAge() / 365.0
her = Person('Cher')
# her.getLastName()
pList = [me, her]
# for p in pList: print p
pList.sort() # very efficient Timsort method
# for p in pList: print p

class MITPerson(Person):
    nextIDNumber = 0 # Next ID number to assign.
    
    def __init__(self, name):
        Person.__init__(self, name) # Initializes Person attributes.
        # New MITPerson attribute: a unique ID number.
        self.IDNumber = MITPerson.nextIDNumber
        MITPerson.nextIDNumber += 1
    
    def getIDNumber(self):
        return self.IDNumber
    
    # Sorting MIT people uses their ID number, not name!        
    def __lt__(self, other):
        return self.IDNumber < other.IDNumber

p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John')

# print p1
# p1.getIDNumber()
# p2.getIDNumber()
# p1 < p2
# p3 < p2
# p4 < p1
# p1 < p4 - AttributeError raised

class Student(MITPerson):
    pass

class UnderGraduate(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    
    def getClass(self):
        return self.year

class Graduate(Student):
    pass

def isStudent(obj):
    return isinstance(obj, Student)

class TransferStudent(Student):
    pass

# s1 = UnderGraduate('Fred', 2016)
# s2 = Graduate('Angels')
# isStudent(s1)
# isStudent(s2)
# me = MITPerson('Eric')
# isStudent(me)
# s1
# s2

# Lecture 12.4, slide 2

class Grades(object):
    """
    A mapping from students to a list of grades.
    """
    
    def __init__(self):
        """
        Creates an empty grade book.
        """
        self.students = [] # List of Student objects.
        self.grades = {} # Dictionary to map IDNumber -> list of grades.
        self.isSorted = True # True if self.students is sorted.
    
    def addStudent(self, student):
        """
        Assumes student is of type Student.
        Add student to the grade book.
        """
        if student in self.students:
            raise ValueError("Duplicate Student")
        self.students.append(student)
        self.grades[student.getIDNumber()] = []
        self.isSorted = False
    
    def addGrade(self, student, grade):
        """
        Assumes grade is a float.
        Adds grade to the list of grades for the student.
        """
        try:
            self.grades[student.getIDNumber()].append(grade)
        except KeyError:
            raise ValueError("Student not in Gradebook")
    
    def getGrades(self, student):
        """
        Returns a list of grades for student.
        """
        try:
            return self.grades[student.getIDNumber()][:]
        except KeyError:
            raise ValueError("Student not in Gradebook")
    
    def allStudents(self):
        """
        Returns a list of all students in the gradebook.
        """
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        # Returns each element or each student in order, as needed.
        for student in self.students:
            yield student

def gradeReport(course):
    """
    Assumes course is of type Grades.
    """
    report = []
    for student in course.allStudents():
        total = 0.0
        numberOfGrades = 0
        for grade in course.getGrades(student):
            total += grade
            numberOfGrades += 1
    
        try:
            average = total / numberOfGrades
            report.append(str(student) + "'s mean grade is " + str(average))
        except ZeroDivisionError:
            report.append(str(student) + " has no grades")
    
    return '\n'.join(report)

# ug1 = UnderGraduate('Jane Doe', 2014)
# ug2 = UnderGraduate('John Doe', 2015)
# ug3 = UnderGraduate('David Henry', 2003)
# g1 = Graduate('John Henry')
# g2 = Graduate('George Steinbrenner')

# sixHundred = Grades()
# sixHundred.addStudent(ug1)
# sixHundred.addStudent(ug2)
# sixHundred.addStudent(g1)
# sixHundred.addStudent(g2)
# 
# for student in sixHundred.allStudents():
#     sixHundred.addGrade(student, 75)

# sixHundred.addGrade(g1, 100)
# sixHundred.addGrade(g2, 25)

# sixHundred.addStudent(ug3)

# print gradeReport(sixHundred)