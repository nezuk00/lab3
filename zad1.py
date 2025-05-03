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
student1=Student('Леха',52)
student1.add_grade(4)
student1.add_grade(7)
student1.add_grade(2)
student1.display_info()
