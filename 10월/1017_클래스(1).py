# bssm 클래스로 클래스 공부하기

class bssm:
    def __init__(self, nick, age, name):
        self.nick = nick
        self.age = age
        self.name = name

    def intro(self):
        print("안녕하세요, 부소마에서 {0} 담당하고 있는 {1}살 {2}입니다.".format(self.nick, self.age, self.name))

ke = bssm("감자", 17, "박강은")
ke.intro()