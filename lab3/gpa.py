GPA = int(input("Enter GPA:"))
Lecture = int(input("Enter Number of Lecture:"))

if GPA >= 2 and Lecture >= 47:
    print("GRADUATED!")

elif GPA < 2 and Lecture >= 47:
    print("Not enough GPA!")

elif GPA >= 2 and Lecture < 47:
    print("Not enaugh number of Lectures!")

elif GPA < 2 and Lecture < 47:
    print("Not enaugh number of Lectures and GPA!")