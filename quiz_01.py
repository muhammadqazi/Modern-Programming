def display():
    for staff in employees:
        fields = staff.split(',')
        for field in fields:
            print(field, end="\t")
        print()


def display_old():
    for staff in employees:
        fields = staff.split(',')
        date = fields[2]
        parts = date.split('/')
        if parts[2] <= "2020":
            for field in fields:
                print(field, end="\t")
            print()


def change_salary(id, newsalary):
    for staff in employees:
        fields = staff.split(',')
        if staff[0:8] == id:
            fields[3] = newsalary
            new_rec = ",".join(fields)
            employees.remove(staff)
            employees.append(new_rec)
            break


def change_salary2(id, newsalary):
    idx = 0
    for staff in employees:
        if staff[0:8] == id:
            oldsalary = staff.split(',')[3]
            employees[idx] = employees[idx].replace(oldsalary, newsalary)
            break
        idx += 1


employees = ["22334455,Jane White               ,22/04/2021,1300.50",
             "11223344,Joe Black                ,11/02/2022,1500.25",
             "66778899,Alice Purple             ,03/06/2020,1200.75",
             "55779900,Tom Green                ,29/02/2022,1100.00",
             "12345678,Robert Claymore          ,14/01/2019,2300.25"]

print("\nAll employees")
display()

print("\nOld employees")
display_old()

change_salary("66778899", "2500.00")
print("\nAll employees after salary change")
display()


change_salary2("11223344", "3500.00")
print("\nAll employees after salary change")
display()
