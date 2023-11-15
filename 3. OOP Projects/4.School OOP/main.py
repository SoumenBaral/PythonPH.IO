from School import School,ClassRoom
from Person import Student
def main():
    school = School("Edam Ji","UTT O RA")

    eight = ClassRoom("Eight")
    school.add_classRoom(eight)

    Nine = ClassRoom("Nine")
    school.add_classRoom(Nine)

    Ten = ClassRoom("Ten")
    school.add_classRoom(Ten)

    Abel = Student("Abib",Ten)
    school.Student_Admission(Abel)

    print(school)





if __name__  == "__main__":
    main()
