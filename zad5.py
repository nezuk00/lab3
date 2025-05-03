class Student:
    def __init__(self,name,student_id):
        self.name= name
        self.student_id=student_id
        self.grade=[]
    def add_grade(self,grade):
        if 0<=grade<=10:
            self.grade.append(grade)
        else:
            print('такой оценки не существует')

    def get_average(self):
        if not self.grade:
            print('нет оценок')
        else:
            return sum(self.grade)/len(self.grade)
    def display_info(self):
        print(f'Имя: {self.name}')
        print(f'ID: {self.student_id}')
        print(f'Оценки студента: {self.grade}')
        print(f'Средний бал: {self.get_average():.2f}')
        print('-'*20)

    def __str__(self):
        return f"Student({self.name}, ID: {self.student_id})"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grade)


if __name__ == "__main__":

    student1 = Student("Леха", "52")
    student2 = Student("Гришаня", "ID456")
    student3 = Student("Саня", "52")


    student1.add_grade(8)
    student1.add_grade(9)
    student1.add_grade(7)

    student2.add_grade(6)
    student2.add_grade(10)

   
    print("Тест __str__:")
    print(student1)
    print()

    print("Тест __eq__:")
    print(f"student1 == student2: {student1 == student2}")
    print(f"student1 == student3: {student1 == student3}")
    print()

    print("Тест __len__:")
    print(f"Количество оценок student1: {len(student1)}")
    print(f"Количество оценок student2: {len(student2)}")