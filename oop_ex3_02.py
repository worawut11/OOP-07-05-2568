class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print("สวัสดีฉันชื่อ", self.name, "อายุ", self.age, "ปี")

    def next_year_age(self):
        print("ปีหน้าฉันจะอายุ", self.age + 1, "ปี")

# สร้าง object นอกคลาส
s1 = student("วรวุฒิ", 18)
s1.introduce()
s1.next_year_age()