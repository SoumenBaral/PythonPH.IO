class School:
    def __init__(self,name ,address) -> None:
        self.name = name 
        self.address = address
        self.teachers = []
        # Composition
        self.classrooms = {}
    
    def add_classRoom(self,classroom):
        self.classrooms[classroom.name] = classroom
    
    def add_Teacher(self,subject,teacher):
        self.teachers[subject] = teacher


    def Student_Admission(self,student):
        className = student.classroom.name
        if className in self.classrooms:
            self.classrooms[className].addStudent(student)
        else:
            print(f'No classroom as a {className}')

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00, 
            'A': 4.00, 
            'A-': 3.50, 
            'B': 3.00, 
            'C': 2.00, 
            'D': 1.00, 
            'F': 0.00
            }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value < 4.5:
            return 'A'
        elif 3.0 <= value < 3.5:
            return 'A-'
        elif 2.5 <= value < 3.0:
            return 'B'
        elif 2.0 <= value < 2.5:
            return 'C'
        elif 1.0 <= value < 2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self) -> str:
        print("---------------All Classrooms----------")

        for key,value in self.classrooms.items():
            print(key)
        
        print("----------------Students---------------")

        eight = self.classrooms['eight']
        for student in eight.students:
            print(student.name)

        print("-------Subject && course Teacher-------")
        for subject in eight.subjects:
            print(f'{subject.name} ---------> {subject.teacher.name}')

        
        print("------Student's Exam Marks-------")
        for student in eight.students:
            for key , value in student.marks.items():
                print(student.name,key , value)
            print('\n-------------- END------------------\n')

        
            
        
        return  ''


class ClassRoom:
    def __init__(self,name) -> None:
        self.name  = name 
        self.students = []
        self.subjects = []
    
    def addStudent(self,student):
        serialId =  f'{self.name} - {len(self.students)+1}'
        student.id = serialId
        self.students.append(student)
    
    def addSubject(self,subject):
        self.subjects.append(subject)
        
    def takeSemesterFinal(self):
        for subject in self.subjects:
            subject.exam(self.students)
    def __str__(self) -> str:
        
        return f'{self.name}: {len(self.students)}'
        
    # sort Students by the grade 

    def get_top_Student(self):
        pass

class Subject:
    def __init__(self,name,teacher) -> None:
        self.name = name 
        self.maxMarks = 100
        self.passMark = 33
        self.teacher = teacher

    def exam(self,students):
        for student in students:
            mark = self.teacher.EvaluateExam()
            student.marks[self.name] = mark
