class Person:
    def __init__(self,name,surname,age):
        self.__name=name
        self.__surname=surname
        self.__age=age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 2:
            self.__name = name

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if len(surname) > 2:
            self.__surname = surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age > 18:
            self.__age = age

    def show_info(self):
        print(f"Имя: {self.__name}, Фамилия: {self.__surname}, Лет: {self.__age} ")


class Teacher(Person):
    def __init__(self,name,surname,age,subject_taught):
        super().__init__(name,surname,age)
        self.subject_taught=subject_taught
    def show_info(self):
        super().show_info()
        print(f"Предмет:",self.subject_taught)


class Student(Person):
    def __init__(self,name,surname,age,course,group,subject_specialty):
        super().__init__(name,surname,age)
        self.course=course
        self.group=group
        self.subject_specialty=subject_specialty
    def show_info(self):
        super().show_info()
        print(f"Курс: {self.course},Группа: {self.group},Специальность: {self.subject_specialty}")

class Subject:
    def __init__(self,name):
        self.name=name

    def show_info(self):
        print(f"Предмет: {self.name}")


class University:
    def __init__(self,name,location,subject):
        self.name=name
        self.location=location
        self.subject=subject

    def show_info(self):
        print(f"Название Университета: {self.name},Местоположение: {self.location}")
        print(f"Предметы: {', '.join(self.subject)}")

class Courpus(University):
    def __init__(self,name,speciality):
        self.name=name
        self.speciality=speciality

    def show_info(self):
        print(f"Название корпуса: {self.name}, Специальность: {self.speciality}")


university = University("Политех\t","Проспект Шевченко",["Математика,Укр,Англ"])
university.show_info()

corpys1=Courpus("ИИБРТ","125,126,127")
corpys1.show_info()

corpys2=Courpus("ИГН","144,148,149")
corpys2.show_info()

virology_teacher=Teacher("Генадий\t","Шаповалов","38","Вирусология")
print("Учитель Вирусологии:",virology_teacher )
virology_teacher.show_info()

its_teacher=Teacher("Норман\t","Бобок","42","ИТС")
print("Учитель ИТС и их защита:",its_teacher)
its_teacher.show_info()

student1=Student("Игорь\t","Ткаченко","19","2","ИИБРТ РЗ-223","125")
student1.show_info()

student2=Student("Алёна\t","Ткаченко","19","4","ИИБРТ РУ-223","122")
student2.show_info()

number_subject=Subject("Литература")
number_subject.show_info()

number_subject1=Subject("История")
number_subject1.show_info()
















