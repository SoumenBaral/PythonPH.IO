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
