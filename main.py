class Person:
    def __init__(self,name,sername,age):
        self.name=name
        self.sername=sername
        self.age=age
    def get_stats(self):
        return f"{self.name} {self.sername}"
    def get_age(self):
        return self.age

class Teacther(Person):
    def __init__(self,name,sername,age,subject_taught):
        super().__init__(name,sername,age)
        self.subject_taught=subject_taught
    def fet_subject_taught(self):
        return self.subject_taught


class Student(Person):
    def __init__(self,name,sername,age,subject_specialty):
        super().__init__(name,sername,age)
        self.subject_specialty=subject_specialty
    def get_subject_specialty(self):
        return self.subject_specialty

class Subject:
    def __init__(self,name):
        self.name=name

class  University:
    def __init__(self,name,location):
        self.name=name
        self.location=location

    def get_name(self):
        return self.name
    def get_location(self):
        return self.location

liter_teacther=Teacther("Tamara","Shaykina","67","Foreign Literature")
physics_teacther=Teacther("Lilia","Byzova","38","Physics")

student1=Student("Igor","Tkachenko","19","cybersecurity")
student2=Student("Alyona","Byzova","19","Food Technologist")

liter_subject=Subject("Foreign Literature")
physics_subject=Subject("Physics")

university=University("Polytech","Shevchenko Avenue")

print("Literature teacher:", liter_teacther.name, liter_teacther.sername)
print("Age:", liter_teacther.age)
print("Teaching subject:", liter_teacther.subject_taught)
print("\nPhysics teacher:", physics_teacther.name, physics_teacther.sername)
print("Age:", physics_teacther.age)
print("Teaching subject:",physics_teacther.subject_taught)

print("\nStudent Igor:", student1.name, student1.sername)
print("Age:", student1.age)

print("\nAlena student:", student2.name, student2.sername)
print("Age:", student2.age)

print("\nUniversity:", university.name)
print("Location:", university.location)










