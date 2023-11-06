class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class

    def __repr__(self):
        return f'Name: {self.name} Class : {self.current_class} Roll: {self.id}'
        
class Teacher:
    def __init__(self, name, subject, id) -> None:
        self.name = name
        self.subject = subject
        self.id = id
    def __repr__(self) -> str:
        return f'Name: {self.name} Subject : {self.subject} Id: {self.id}'

alia = Student("alia Torkari ", 9,1)
print(alia)
ranbeer = Teacher('Douran beer', 'Algorithm', 101)
print(ranbeer)