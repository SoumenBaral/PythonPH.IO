class School:
    def __init__(self,name ,address) -> None:
        self.name = name 
        self.address = address
        # Composition
        self.classrooms = {}
    
    def add_classRoom(self,classroom):
        self.classrooms[classroom.name] =classroom

    def Student_Admission(self,student,classroomName):
        if classroomName in self.classrooms:
            self.classrooms[classroomName].addStudent(student)
        else:
            print(f'No classroom as a {classroomName}')

class ClassRoom:
    def __init__(self,name) -> None:
        self.name  = name 
        self.students = []
    
    def addStudent(self,student):
        serialId =  f'{self.name} - {len(self.students)+1}'
        self.students.append(student)
    
    def __str__(self) -> str:
        
        return f'{self.name}: {len(self.students)}'
        
    # sort Students by the grade 

    def get_top_Student(self):
        pass