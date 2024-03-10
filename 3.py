class Human():
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def changing_name(self, new):
        self.new=new
        
class Student(Human):
    def __init__(self, name, age, vnz, grades=[]):
        super().__init__(name, age)
        self.vnz=vnz
        self.grades=grades
    def add_grade(self, grades):
        self.grades.append(grades)
    def average_grade(self):
        if not self.grades:
            return "Нема оцінок"
        total = sum(self.grades)
        count = len(self.grades)
        return total / count
        
student = Student("Василь", 20, "КНУ")
print("Ім'я студента:", student.name)
print("Вік студента:", student.age)
print("ВНЗ студента:", student.vnz)

student.changing_name("Петро")
print("Нове ім'я студента:", student.new)

student.add_grade(2)
student.add_grade(4)
student.add_grade(3)
student.add_grade(3)
student.add_grade(5)
print("Список оцінок студента:", student.grades)
print("Середня оцінка студента:", student.average_grade())