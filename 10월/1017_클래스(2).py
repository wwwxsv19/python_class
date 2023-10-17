# 성적 출력 
class Grade:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def s_grade(self):
        if self.score >= 90:
            self.score = "A"
        else:
            self.score = "B"
    def __str__(self):
        return "%s: %c 등급" %(self.name, self.score)
    
a = Grade("강은", 86)
b = Grade("강호", 90)

a.s_grade()
b.s_grade()

print(a, b, sep="\n")