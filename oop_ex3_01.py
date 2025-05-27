class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("สวัสดีฉันชื่อ", self.name, "อายุ", self.age, "ปี")

# สร้าง object
s1 = Student("วรวุฒิ", 18)
s1.introduce()