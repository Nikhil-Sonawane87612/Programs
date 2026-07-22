class Student:
    def __init__(self, name, course, score):
        self.name=name
        self.course=course
        self.score=score
    def display_info(self):
        print(f"Student : {self.name}")
        print(f"Course : {self.course}")
        print(f"Score : {self.score}")
        
    def has_passed(self):
        if self.score>=40:
            return "Passed"
        else:
            return "Failed"
    
s1=Student("Nikhil", "BCA", 75)
s1.display_info()
print(s1.has_passed())