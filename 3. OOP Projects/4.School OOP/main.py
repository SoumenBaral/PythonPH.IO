from School import School,ClassRoom,Subject
from Person import Student,Teacher
def main():
    school = School("Edam Ji","UTT O RA")

    eight = ClassRoom("eight")
    school.add_classRoom(eight)

    Nine = ClassRoom("Nine")
    school.add_classRoom(Nine)

    Ten = ClassRoom("Ten")
    school.add_classRoom(Ten)

    Abel = Student("Abib",eight)
    school.Student_Admission(Abel)
    Babul = Student("Babul",eight)
    school.Student_Admission(Babul)
    kabul = Student("kabul",eight)
    school.Student_Admission(kabul)

    # Subjects  ::::

    
    Chemistry_Teacher = Teacher("Bagger sen ")
    Chemistry = Subject("Chemistry",Chemistry_Teacher)
    eight.addSubject(Chemistry)

    physics_Teacher = Teacher("sultan Ali khan")
    physics = Subject("Physics",physics_Teacher)
    eight.addSubject(physics)

    Biology_Teacher = Teacher("Gaze Sir")
    Biology = Subject("Biology",Biology_Teacher)
    eight.addSubject(Biology)

    eight.takeSemesterFinal()

    print(school)





if __name__  == "__main__":
    main()
