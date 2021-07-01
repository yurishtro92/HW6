from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.middle_grade = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        for course in self.grades:
            self.middle_grade[course] = mean(self.grades[course])
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.middle_grade}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}\n'
        return result

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a student')
            return
        return sum((value) for value in self.middle_grade.values()) < sum(
            (value) for value in other.middle_grade.values())


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        for course in self.courses_attached:
            self.middle_grade = mean(self.grades[course])
        result = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.middle_grade}\n'
        return result

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a lecturer')
            return
        return self.middle_grade < other.middle_grade


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        result = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return result


cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_lecturer_1 = Lecturer('Awesome', 'Buddy')
cool_lecturer_1.courses_attached += ['Python']

cool_reviewer = Reviewer('Other', 'Buddy')
cool_reviewer.courses_attached += ['Python', 'Git']
cool_reviewer_1 = Reviewer('Another', 'Buddy')
cool_reviewer_1.courses_attached += ['Python', 'Git']

best_student = Student('Ruoy', 'Eman', 'gender')
best_student.courses_in_progress += ['Python', 'Git']
best_student.finished_courses += ['Введение в программирование']
best_student_1 = Student('Mike', 'Tyson', 'gender')
best_student_1.courses_in_progress += ['Python', 'Git']
best_student_1.finished_courses += ['Введение в html-верстку']

best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer, 'Python', 10)
best_student.rate_lecture(cool_lecturer_1, 'Python', 10)
best_student.rate_lecture(cool_lecturer_1, 'Python', 9)
best_student.rate_lecture(cool_lecturer_1, 'Python', 8)
best_student_1.rate_lecture(cool_lecturer, 'Python', 10)
best_student_1.rate_lecture(cool_lecturer, 'Python', 9)
best_student_1.rate_lecture(cool_lecturer, 'Python', 9)
best_student_1.rate_lecture(cool_lecturer_1, 'Python', 9)
best_student_1.rate_lecture(cool_lecturer_1, 'Python', 9)
best_student_1.rate_lecture(cool_lecturer_1, 'Python', 8)

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student, 'Git', 10)
cool_reviewer.rate_hw(best_student_1, 'Python', 10)
cool_reviewer.rate_hw(best_student_1, 'Python', 9)
cool_reviewer.rate_hw(best_student_1, 'Python', 9)
cool_reviewer.rate_hw(best_student_1, 'Git', 9)
cool_reviewer.rate_hw(best_student_1, 'Git', 8)
cool_reviewer.rate_hw(best_student_1, 'Git', 9)

cool_reviewer_1.rate_hw(best_student, 'Python', 10)
cool_reviewer_1.rate_hw(best_student, 'Python', 10)
cool_reviewer_1.rate_hw(best_student, 'Python', 10)
cool_reviewer_1.rate_hw(best_student, 'Git', 10)
cool_reviewer_1.rate_hw(best_student, 'Git', 10)
cool_reviewer_1.rate_hw(best_student, 'Git', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 10)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Python', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Git', 9)
cool_reviewer_1.rate_hw(best_student_1, 'Git', 8)
cool_reviewer_1.rate_hw(best_student_1, 'Git', 9)

print(cool_reviewer)
print(cool_reviewer_1)
print(cool_lecturer)
print(cool_lecturer_1)
print(best_student)
print(best_student_1)
print(
    f'Is lecturer {cool_lecturer.name, cool_lecturer.surname} better than lecturer {cool_lecturer_1.name, cool_lecturer_1.surname}? - {cool_lecturer > cool_lecturer_1}\n')
print(
    f'Is student {best_student.name, best_student.surname} better than student {best_student_1.name, best_student_1.surname} in {best_student.courses_in_progress}? - {best_student > best_student_1}\n')

course_name = 'Python'
students_list = [best_student, best_student_1]
lecturers_list = [cool_lecturer, cool_lecturer_1]


def total_grade_stud(students_list, course_name):
    total = []
    for student in students_list:
        total += [student.middle_grade[course_name]]
    return sum(total) / len(total)


def total_grade_lect(lecturers_list, course_name):
    total = []
    for lecturer in lecturers_list:
        if course_name in lecturer.courses_attached:
            total += [lecturer.middle_grade]
        else:
            return print(f'Lecturer does not teach {course_name}')
    return sum(total) / len(total)


print(
    f'Average rating for all students on the {course_name} discipline - {total_grade_stud(students_list, course_name)}\n')
print(
    f'Average rating for all lecturers on the {course_name} discipline - {total_grade_lect(lecturers_list, course_name)}\n')