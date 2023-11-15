from School import School,ClassRoom
from Person import Student
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

    print(school)





if __name__  == "__main__":
    main()
