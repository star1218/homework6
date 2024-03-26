class Person:
    def __init__(self,name,sername,age):
        self.name=name
        self.sername=sername
        self.age=age

class Teacther(Person):
    def __init__(self,name,sername,age,subject_taught):
        super().__init__(name,sername,age)
        self.subject_taught=subject_taught

class Student(Person):
    def __init__(self,name,sername,age,subject_specialty):
        super().__init__(name,sername,age)
        self.subject_specialty=subject_specialty

class Subject:
    def __init__(self,name):
        self.name=name

class  Academy:
    def __init__(self,name,location):
        self.name=name
        self.location=location

liter_teacther=Teacther("Tamara","Shaykina","67","Foreign Literature")
physics_teacther=Teacther("Lilia","Byzova","38","Physics")

student1=Student("Igor","Tkachenko","19","")







