from itertools import count


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecotrs(self,lector,course,grade):
        if isinstance(lector,Lectore) and course in self.courses_in_progress and course in lector.courses and (grade > 1 or grade < 10):
           les_grades = lector.grade_students.setdefault(course)
           if les_grades == None:
               les_grades = []
           les_grades.append(grade)
           lector.grade_students[course] = les_grades
        else:
            if not isinstance(lector,Lectore):
                print("Лектор не того типа")
            if not (course in self.courses_in_progress):
                print("Такого курса нет у студента", self.name)
            if not (course in lector.courses):
                print("Такого курса нет у лектора ", lector.name )
            if not (grade > 1 or grade < 10):
                print("Оценка должны быть от 1 до 10")

    def count_mid_grades(self,student):
        sum_rate = 0
        count = 0
        for val_grade in self.grades.values():
            for i in val_grade:
                sum_rate += i
                count += 1
        if count == 0:
            mid_rate = 0
        else:
            mid_rate = round(sum_rate / count, 1)
        return  mid_rate

    def __str__(self):
        mid_rate = self.count_mid_grades(self)

        #Курсы в процессе обучения
        strCours = ""
        for i in self.courses_in_progress:
            strCours = f"{i}, {strCours}"

        if strCours == "":
            printCours = " Нет курсов в процессе обучения"
        else:
            strCours = strCours[:-2]
            printCours = f" Курсы в процессе изучения: {strCours}"

        str_finish_Courses = ""

        for i in self.finished_courses:
            str_finish_Courses = f"{i}, {str_finish_Courses}"

        if str_finish_Courses == "":
            printCoursFinish = " Нет законченных курсов"
        else:
            str_finish_Courses = str_finish_Courses[:-2]
            printCoursFinish = f" Курсы в процессе изучения: {str_finish_Courses}"


        text = (f"Студент. \n Имя: {self.name} \n Фамилия: {self.surname} \n"
               f" Средняя оценка за домашнее задание: {mid_rate} \n"
               f" {printCours} \n"
               f" {printCoursFinish}")
        return text

    def __lt__(self, other):
        if not isinstance(other,Student):
            return
        mid_self = self.count_mid_grades(self)
        mid_other = self.count_mid_grades(other)

        return mid_self < mid_other
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname



#Это лекторы
class Lectore(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_students = {}
        self.courses = []

    def count_mid(self, lector):
        sum_rate = 0
        count = 0
        for val_grade in lector.grade_students.values():
           for i in val_grade:
               sum_rate += i
               count += 1
        if count == 0:
            mid_rate = 0
        else:
            mid_rate = round(sum_rate/count,1)
        return  mid_rate

    def __lt__(self, other):
        if not isinstance(other,Lectore):
            return
        mid_self = self.count_mid(self)
        mid_other = self.count_mid(other)

        return mid_self < mid_other

    def __str__(self):

        mid_rate = self.count_mid(self)
        text = f"Лектор. \n Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {mid_rate}"
        return text


#Это проверяющие ДЗ
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        text = f"Проверяющий. \n Имя: {self.name} \n Фамилия: {self.surname}"
        return text

def count_mid_rate_students(listStudents,name_cours):
    mid_rate = 0
    sum_rate = 0
    count = 0
    for stud in listStudents:
        courses = stud.grades
        for key,val in courses.items():
            if key == name_cours:
                count += len(val)
                for i in val:
                   sum_rate = sum_rate + i
    if count != 0:
        mid_rate = round(sum_rate / count, 2)
    else:
        mid_rate = 0

    return mid_rate

def count_mid_rate_lectors(listLectors,name_cours):
    mid_rate = 0
    sum_rate = 0
    count = 0
    for lect in listLectors:
        courses = lect.grade_students
        for key,val in courses.items():
            if key == name_cours:
                count += len(val)
                for i in val:
                   sum_rate = sum_rate + i
    if count != 0:
        mid_rate = round(sum_rate / count, 2)
    else:
        mid_rate = 0

    return mid_rate

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['1C']
best_student.courses_in_progress += ['Mathematica']
best_student.courses_in_progress += ['Psyhologia']

bad_student = Student('Alex', 'Maksimov', 'your_gender')
bad_student.courses_in_progress += ['Python']
bad_student.courses_in_progress += ['1C']
bad_student.courses_in_progress += ['Mathematica']
bad_student.courses_in_progress += ['Psyhologia']

lectorIlias = Lectore("Ilias","Nizamutdinov")
lectorIlias.courses = ["1C","Mathematica","Psyhologia",'Python']

lectorStas = Lectore("Stas","Petrov")
lectorStas.courses = ["Psyhologia"]

reviewerOlga = Reviewer("Петрова","Ольга")
reviewerOlga.courses_attached = ['Python','Mathematica','Psyhologia','1C']

reviewerVera = Reviewer("Васильева","Вера")
reviewerVera.courses_attached = ['Python','Mathematica','Psyhologia','1C']

#проверяем дз
reviewerOlga.rate_hw(best_student,'Python',8)
reviewerOlga.rate_hw(best_student,'Mathematica',9)
reviewerOlga.rate_hw(bad_student,'Python',4)
reviewerOlga.rate_hw(bad_student,'Mathematica',3)
reviewerOlga.rate_hw(bad_student,'1C',5)

reviewerVera.rate_hw(best_student,'Python',8)
reviewerVera.rate_hw(best_student,'Psyhologia',9)
reviewerVera.rate_hw(best_student,'1C',8)
reviewerVera.rate_hw(best_student,'1C',9)


#выставляем оценки лекторам

best_student.rate_lecotrs(lectorIlias,"1C",8)
best_student.rate_lecotrs(lectorIlias,"1C",9)
best_student.rate_lecotrs(lectorIlias,"Psyhologia",5)
best_student.rate_lecotrs(lectorIlias,"Mathematica",9)
best_student.rate_lecotrs(lectorIlias,"Mathematica",10)
best_student.rate_lecotrs(lectorIlias,"Python",2)

bad_student.rate_lecotrs(lectorStas,"Psyhologia",2)
bad_student.rate_lecotrs(lectorIlias,"1C",3)
bad_student.rate_lecotrs(lectorIlias,"Mathematica",4)
bad_student.rate_lecotrs(lectorIlias,"Python",4)

#выводим студентов
print(best_student)
print(bad_student)

#Сравниваем студентов
print("Первый лучше второго? ",bad_student > best_student)
print("")

#выводим лекторов
print(lectorIlias)
print(lectorStas)

#Сравниваем
print("Первый лучше второго?", lectorIlias > lectorStas)
print("")

#выводим проверяющих
print(reviewerOlga)
print(reviewerVera)

#Подсчитаем оценку

list_students = [best_student,bad_student]
list_lectors = [lectorIlias,lectorStas]

mid_rate_students_1c = count_mid_rate_students(list_students,"1C")
mid_rate_students_python = count_mid_rate_students(list_students,"Python")

mid_rate_lectors_1C = count_mid_rate_lectors(list_lectors,"1C")
mid_rate_lectors_python = count_mid_rate_lectors(list_lectors,"Python")

print("")
print("Средняя оценка по питону у студентов: ", mid_rate_students_python)
print("Средняя оценка по 1C у студентов: ", mid_rate_students_1c)
print("")
print("Средняя оценка по питону у лекторов: ", mid_rate_lectors_python)
print("Средняя оценка по 1C у лекторов: ", mid_rate_lectors_1C)

