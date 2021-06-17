class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lectures) \
                and course in lecturer.courses_attached \
                and course in self.courses_in_progress and grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Ошибка'


    def get_avg_grade(self):
        if self.grades:
            sum_hw = 0
            counter = 0
            for grades in self.grades.values():
                sum_hw += sum(grades)
                counter += len(grades)
                return round(sum_hw / counter, 2)
        else:
            return 'Ошибка'

    def __str__(self):
        some_stud = f'Имя: {self.name}\n' \
                    f'Фамилия: {self.surname}\n' \
                    f'Средняя оценка за дз: {self.get_avg_grade()}\n'
        return some_stud

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не наш студент')
            return
        else:
            try:
                compare = self.get_avg_grade() < other.get_avg_grade()
                if compare:
                    print(f'{self.name} учиться хуже чем {other.name} {other.surname}')
                else:
                    print(f'{other.name} {other.surname} учиться хуже чем {self.name}')
                return compare
            except Exception:
                print(f'Ошибочное сравнение значений')
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        #self.grades = {}

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in (student.courses_in_progress or student.finished_courses):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        some_rewiewer = f'Имя: {self.name}\nФамилия: {self.surname}'
        return some_rewiewer

class Lectures(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []    # список оценок

    def __str__(self):
        some_lecture = f'Имя: {self.name}\n' \
                       f'Фамилия: {self.surname} \n' \
                       f'Средняя оценка за лекции: {sum(self.grades) / len(self.grades) :.2f}\n'
        return some_lecture




def get_avg_hw_garde(student_list, course):
    total_sum = 0

    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)


def get_avg_lecture_grade(list_lectures):
    total_sum = 0

    for lecturer in list_lectures:
        total_sum += sum(lecturer.grades) / len(lecturer.grades)
    return total_sum / len(list_lectures)




best_student = Student('Гермиона', 'Грейнджер', 'F')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

best_student_1 = Student('Иван', 'Иванов', 'M')
best_student_1.courses_in_progress += ['Python']
best_student_1.courses_in_progress += ['GIT']

cool_reviewer = Reviewer('Миневра', 'Макгонагалл')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['GIT']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 7)

cool_reviewer.rate_hw(best_student_1, 'Python', 6)
cool_reviewer.rate_hw(best_student_1, 'Python', 7)
cool_reviewer.rate_hw(best_student_1, 'Python', 5)


print(best_student.grades)

cool_lecturer = Lectures('Some', 'Name')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Git']
next_lecturer = Lectures('Some', 'Name')
next_lecturer.courses_attached += ['Python']
next_lecturer.courses_attached += ['Git']

best_student.rate_lecturer(cool_lecturer, 'Python', 4)
best_student.rate_lecturer(cool_lecturer, 'Git', 10)
best_student_1.rate_lecturer(next_lecturer, 'Python', 10)
best_student_1.rate_lecturer(next_lecturer,  'Git', 10)

print(next_lecturer.grades)
print(cool_lecturer.grades)

print(best_student.grades)
print(best_student_1.grades)

print(best_student > best_student_1)

print(best_student)
print(cool_lecturer)

print(get_avg_hw_garde([best_student, best_student_1], 'Python'))
print(get_avg_lecture_grade([cool_lecturer, next_lecturer]))