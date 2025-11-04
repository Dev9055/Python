class UPES:
    def __init__(self, schoolname, students, faculty):
        self.schoolname = schoolname
        self.students = students
        self.faculty = faculty
    
    def display(self):
        """Display the details of the school."""
        return "|{}\t\t|{}\t\t\t|{}\t\t\t|\n".format(str(self.schoolname), str(self.students), str(self.faculty))

soc = UPES('SoCS', 1000, 150)
media = UPES('Media', 500, 50)
law = UPES('Law', 450, 25)


with open("upes_details.txt", "w") as file:
    file.write("| School Name     | Number of Students | Number of Faculties |\n")
    file.write("+----------------+--------------------+------------------------+\n")
    file.write(soc.display())
    file.write(media.display())
    file.write(law.display())
    file.write("+----------------+--------------------+------------------------+\n")


print("Details written to 'upes_details.txt' file.")

with open("upes_details.txt", "r") as file:
    content = file.read()
    print(content)
