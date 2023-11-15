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

    def __repr__(self) -> str:
        print("---------------All Classrooms----------")

        for key,value in self.classrooms.items():
            print(key)
        
        print("----------------Students---------------")

        eight = self.classrooms['eight']
        for student in eight.students:
            print(student.name)
        
        return  ''


class ClassRoom:
    def __init__(self,name) -> None:
        self.name  = name 
        self.students = []
    
    def addStudent(self,student):
        serialId =  f'{self.name} - {len(self.students)+1}'
        student.id = serialId
        self.students.append(student)
    
    def __str__(self) -> str:
        
        return f'{self.name}: {len(self.students)}'
        
    # sort Students by the grade 

    def get_top_Student(self):
        pass