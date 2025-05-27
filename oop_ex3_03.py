class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("สวัสดีฉันชื่อ", self.name, "อายุ", self.age, "ปี")

class Teacher(Student):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduct(self):
        print("สวัสดีฉันชื่อ", self.name, "อายุ", self.age, "ปี สอนวิชา", self.subject)

# สร้าง object ของคลาส Teacher
t1 = Teacher("สมชาย", 35, "คณิตศาสตร์")
t1.introduct()