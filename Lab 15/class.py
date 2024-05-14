#Create a class called Student. Create a variable (name,rollno) using constructor

class Student:
    def __init__(self):
        self.name=""
        self.rollno=""
    def display(self):
        print("Name: ",self.name)
        print("Rollno: ",self.rollno)
    
student1=Student()
student1.name="Crank"
student1.rollno="69"
student1.display()
student2=Student()
student2.name="Sathvik"
student2.rollno="72"
student2.display()