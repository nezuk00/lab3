class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Teacher(Person):
    def __init__(self, name, subject, age):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            if student not in self.students:
                self.students.append(student)
                print(f"Студент {student.name} успешно добавлен.")
            else:
                print(f"Студент {student.name} уже в списке.")
        else:
            print("Можно добавить только объект класса Student.")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"Студент {student.name} успешно удалён.")
        else:
            print("Студент не найден.")

    def list_students(self):
        if not self.students:
            print(f"У преподавателя {self.name} пока нет студентов.")
        else:
            print(f"Студенты преподавателя {self.name}:")
            for student in self.students:
                print(f"- {student.name} (ID: {student.student_id})")



if __name__ == "__main__":

    math_teacher = Teacher("Абоба Абобавна", "Блаблаведение", 42)


    student1 = Student("ЛЕха Пиво", "S001")
    student2 = Student("Иля Никитенко", "S002")


    math_teacher.add_student(student1)
    math_teacher.add_student(student2)
    math_teacher.add_student(student1)


    math_teacher.list_students()


    math_teacher.remove_student(student1)
    math_teacher.remove_student(Student("Несуществующий", "S999"))  


    math_teacher.list_students()