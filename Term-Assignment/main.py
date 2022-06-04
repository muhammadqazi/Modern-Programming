def console():
    print("""


 █████╗ ███████╗███████╗██╗ ██████╗ ███╗   ██╗███╗   ███╗███████╗███╗   ██╗████████╗
██╔══██╗██╔════╝██╔════╝██║██╔════╝ ████╗  ██║████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
███████║███████╗███████╗██║██║  ███╗██╔██╗ ██║██╔████╔██║█████╗  ██╔██╗ ██║   ██║
██╔══██║╚════██║╚════██║██║██║   ██║██║╚██╗██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║
██║  ██║███████║███████║██║╚██████╔╝██║ ╚████║██║ ╚═╝ ██║███████╗██║ ╚████║   ██║
╚═╝  ╚═╝╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝
                                                          github.com/muhammadqazi
                    """)

    print("Supervisor \t\t\t\t\t\t Dr. Tamer Tulgar")
    print("By Muhammad Qazi \t\t\t\t\t 21906778\n")


def _file_reader():
    students = []
    with open('students.txt', 'r') as f:
        for line in f:
            students.append(line.split(','))
            students[-1][-1] = students[-1][-1].rstrip()
    return students


def insert(stdid, name, cgpa, date, gender):

    students = _file_reader()

    for i in range(len(students)):
        if students[i][0] == stdid:
            print("\nStudent with the same id already exists !")
            break
    else:
        with open("students.txt", "a") as x:
            x.write(f"\n"+",".join([stdid, name, cgpa, date, gender]))
        print("Record is sucessfully inserted !")


def modify(stdid, field, new_value):

    students = _file_reader()

    for i in range(len(students)):
        if students[i][0] == stdid:

            if field == "1":

                students[i][1] = new_value

                with open('students.txt', 'w') as x:
                    for student in students:
                        # if its the last student in the list then we dont need to add a new line
                        if student == students[-1]:
                            x.write(','.join(student))
                        else:
                            x.write(','.join(student) + '\n')

                print("\nModified successfully!")
                print("Name of the student with id " + stdid +
                      " is changed to " + new_value, end="\n\n")
                break

            elif field == "2":
                students[i][2] = new_value

                with open('students.txt', 'w') as x:
                    for student in students:
                        if student == students[-1]:
                            x.write(','.join(student))
                        else:
                            x.write(','.join(student) + '\n')

                print("\nModified successfully!")
                print("CGPA of the student with id " + stdid +
                      " is changed to " + new_value, end="\n\n")
                break

            elif field == "3":
                students[i][3] = new_value

                with open('students.txt', 'w') as x:
                    for student in students:
                        if student == students[-1]:
                            x.write(','.join(student))
                        else:
                            x.write(','.join(student) + '\n')

                print("\nModified successfully!")
                print("DOB of the student with id " + stdid +
                      " is changed to " + new_value, end="\n\n")
                break

            elif field == "4":

                students[i][4] = new_value

                with open('students.txt', 'w') as x:
                    for student in students:
                        if student == students[-1]:
                            x.write(','.join(student))
                        else:
                            x.write(','.join(student) + '\n')

                print("\nModified successfully!")
                print("Gender of the student with id " + stdid +
                      " is changed to " + new_value, end="\n\n")
                break
            else:
                print("No suchh field found")
                break
    else:
        print("Student not found!")


def delete(stdid):

    students = _file_reader()
    for i in range(len(students)):
        if students[i][0] == stdid:

            students.pop(i)

            prompt = input(
                "Are you sure you want to delete this record? (y/n)")

            if prompt == "y" or prompt == "Y":
                with open('students.txt', 'w') as x:
                    for student in students:
                        # if its the last student in the list then we dont need to add a new line
                        if student == students[-1]:
                            x.write(','.join(student))
                        else:
                            x.write(','.join(student) + '\n')

                print("\nDeleted successfully!")
                print("Student with id " + stdid + " is deleted", end="\n\n")
                break
            else:
                print("\nDeletion cancelled")
                break
    else:
        print("Student not found!")


def display():

    students = _file_reader()
    print("\n")
    for i in range(len(students)):

        print("{:<10}{:<25}{:<10}{:<20}{:<10}".format(
            students[i][0], students[i][1], float(students[i][2]), students[i][3], students[i][4]))
    print("\n")


def stats():

    students = _file_reader()
    _total_females = 0
    _total_males = 0
    _sum_cgpa = 0
    for i in range(len(students)):
        _sum_cgpa += float(students[i][2])
        if students[i][4] == 'F':
            _total_females += 1
        elif students[i][4] == 'M':
            _total_males += 1

    with open('stats.txt', 'w') as x:
        x.write("\n\t{:20}{:10}\n".format("Total Students :", len(students)))
        x.write("\t{:20}{:10}\n".format("Total Males    :", _total_males))
        x.write("\t{:20}{:10}\n".format("Total Females  :", _total_females))
        x.write("\t{:20}{:10.2f}\n".format(
            "Average CGPA   :", _sum_cgpa/len(students)))

    print("\n\t{:20}{:10}\n".format("Total Students :", len(students)))
    print("\t{:20}{:10}\n".format("Total Males    :", _total_males))
    print("\t{:20}{:10}\n".format("Total Females  :", _total_females))
    print("\t{:20}{:10.2f}\n".format(
        "Average CGPA   :", _sum_cgpa/len(students)))


def main():

    console()

    print("Enter the number from the given options:")

    while True:
        print("""
        1. Insert a new record
        2. Modify a record
        3. Delete a record
        4. Display all records
        5. Stats of the records
        6. Exit
        """)

        choice = input("\n\n┌─[ " + "CIU" + "~" +
                       "@HOME" + " ]" + "\n└──╼ " + "$ ")

        if choice == "1":

            stdid = input("Please enter the student id: ")
            name = input("Please enter the name: ")
            cgpa = input("Please enter the cgpa: ")
            dob = input("Please enter the date of birth: ")
            prompt = input(
                "Please enter the gender : \n1. Male \t2.Female\n=> ")

            if prompt == "1":
                gender = 'M'
                insert(stdid, name, cgpa, dob, gender)
                break
            elif prompt == "2":
                gender = 'F'
                insert(stdid, name, cgpa, dob, gender)
                break
            else:
                print("Invalid Choice !")
                break

        elif choice == "2":

            stdid = input("Please enter the student id: ")
            field = input(
                "Please enter the field you want to modify: \n1. Name \t2. CGPA \t3. DOB \t4. Gender\n=> ")

            if field.isnumeric():
                if int(field) <= 4 and int(field) != 0:

                    new_value = input("Please enter the new value: ")
                    modify(stdid, field, new_value)
                    break
                else:
                    print("Invalid Choice !")
                    break
            else:
                print("Invalid Choice ! Error: Wrong input type")
                break

        elif choice == "3":
            stdid = input("Please enter the student id: ")
            delete(stdid)
            break

        elif choice == "4":

            display()
            break

        elif choice == "5":

            stats()
            break

        elif choice == "6":

            print("Bye !")
            break

        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()
