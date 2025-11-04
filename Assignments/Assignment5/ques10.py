name=input("Enter your name: ")
roll_num=input("Enter your roll number : ")
sap=input("Enter your sapid : ")
sem=input("Enter your Semester : ")
course=input("Enter your course : ")
sub1=int(input("Enter marks of PDS: "))
sub2=int(input("Enter marks of Python: "))
sub3=int(input("Enter marks of Chemistry: "))
sub4=int(input("Enter marks of English: "))
sub5=int(input("Enter marks of Physics: "))

percent=((sub1+sub2+sub3+sub4+sub5)/500)*100
cgpa=percent/10

print(' SAMPLE GRADE SHEET ')
print('Name:{}'.format(name))
print('Roll Number:{}'.format(roll_num))
print('SAP ID:{}'.format(sap))
print('Semester:{}'.format(sem))
print('Course:{}'.format(course))
print('Subject name :Mark')
print('PDS:{}'.format(sub1))
print('Python:{}'.format(sub2))
print('Chemistry:{}'.format(sub3))
print('English:{}'.format(sub4))
print('Physics:{}'.format(sub5))
print('Percentage:{}'.format(percent))
print("CGPA:{}".format(cgpa))

if cgpa>=0 and cgpa<=3.4:
    print('Grade:F')
elif cgpa>=3.5 and cgpa<=5.0:
    print('Grade:C+')
elif cgpa>=5.1 and cgpa<=6.0:
    print('Grade:B')
elif cgpa>=6.1 and cgpa<=7.0:
    print('Grade:B+')
elif cgpa>=7.1 and cgpa<=8.0:
    print('Grade:A')
elif cgpa>=8.1 and cgpa<=9.0:
    print('Grade:A+')
else:
    print('Grade:O')
