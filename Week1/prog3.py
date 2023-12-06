# Create the grading system of PDEU

OSmarks = int(input("Enter OS your marks: ")) # Take marks as input
DAAmarks = int(input("Enter DAA your marks: "))
DBMSmarks = int(input("Enter DBMS your marks: "))

total = (OSmarks + DAAmarks + DBMSmarks) / 3 


print("              ***************************             ")
print("           Pandit Deendayal Energy University         ")
print("                       GRADE SHEET                    ")
print("              ***************************        ")

if OSmarks >= 80:
    print("OS : O Grade")
    cgpa1 = 10
elif OSmarks >=70:
    print("OS : A+ Grade")
    cgpa1 = 9
elif OSmarks >=60:
    print("OS : A Grade")
    cgpa1 = 8
elif OSmarks >=50:
    print("OS : B Grade")
    cgpa1 = 7
elif OSmarks >=40:
    print("OS : P Grade")
    cgpa1 = 6
elif OSmarks < 40:
    print("OS : F Grade")
    cgpa1 = 0

if DAAmarks >= 80:
    print("DAA : O Grade")
    cgpa2 = 10
elif DAAmarks >=70:
    print("DAA : A+ Grade")
    cgpa2 = 9
elif DAAmarks >=60:
    print("DAA : A Grade")
    cgpa2 = 8
elif DAAmarks >=50:
    print("DAA : B Grade")
    cgpa2 = 7
elif DAAmarks >=40:
    print("DAA : P Grade")
    cgpa2 = 6
elif DAAmarks < 40:
    print("DAA : F Grade")
    cgpa2 = 0

if DBMSmarks >= 80:
    print("DBMS : O Grade")
    cgpa3 = 10
elif DBMSmarks >=70:
    print("DBMS : A+ Grade")
    cgpa3 = 9
elif DBMSmarks >=60:
    print("DBMS : A Grade")
    cgpa3 = 8
elif DBMSmarks >=50:
    print("DBMS : B Grade")
    cgpa3 = 7
elif DBMSmarks >=40:
    print("DBMS : P Grade")
    cgpa3 = 6
elif DBMSmarks < 40:
    print("DBMS : F Grade")
    cgpa3 = 0

if cgpa1 != 0 and cgpa2 != 0 and cgpa3 != 0:
    cgpa = (cgpa1 + cgpa2 + cgpa3) / 3
else:
    cgpa = (cgpa1 + cgpa2 + cgpa3) / 3
    print("You have a backlog in one or more subject")

if total >= 80:
    print("total : O Grade")
    print("CGPA: " + str(cgpa))
elif total >=70:
    print("total : A+ Grade")
    print("CGPA: " +str(cgpa))
elif total >=60:
    print("total : A Grade")
    print("CGPA: " +str(cgpa))
elif total >=50:
    print("total : B Grade")
    print("CGPA: " + str(cgpa))
elif total >=40:
    print("total : P Grade")
    print("CGPA: " +str(cgpa))
elif total < 40:
    print("total : F Grade")
    print("Fail")




