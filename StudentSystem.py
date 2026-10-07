print ("======== STUDENT MANAGEMENT SYSTEM ========")
student_name = input("Name: ")
student_program = input("Program: ")
student_section = input("Section: ")

print ("======== GRADES OF STUDENTS ========")
csElec = float(input("CSElec:"))
softEng = float(input("CS303:"))
automata = float(input("CS302:"))
geElec = float(input("GE Elec:"))
progLang = float(input("CS301:"))

ave = (csElec + softEng + automata + geElec + progLang) / 5

if ave >= 90:
    remark = "EXELLENT"
elif ave >= 75:
    remark = "PASSED"
else:
    remark = "FAILED"

print ("======== RESULTS ========")
print("Student Name:", student_name )
print("Program: ", student_program)
print("Section: ", student_section)
print("CSElec:", csElec)
print("CS303: ", softEng)
print("CS302: ", automata)
print("GE Elec:", geElec)
print("CS301: ", progLang)
print("Average: ", format(ave,".2f"))
print("Remark:", remark)

