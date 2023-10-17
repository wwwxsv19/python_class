# 붕어빵 맹들기

class FishCakeMaker:
    def __init__(self, **kwargs): # 가변인자 매개변수 : 이 안에 몇 개의 매개변수가 들어올지 모른다! 라는 뜻
        self.size = 10
        self.flavor = "팥"
        self.price = 400

        if "size" in kwargs:
            self.size = kwargs.get("size") # kwargs 딕셔너리 안에 size 라는 key 값의 value 가져오기
        if "flavor" in kwargs:
            self.flavor = kwargs.get("flavor")
        if "price" in kwargs:
            self.price = kwargs.get("price")

    def show(self):
        print("붕어빵 크기 {}".format(self.size))
        print("붕어빵 종류 {}".format(self.flavor))
        print("붕어빵 가격 {}".format(self.price))
        print('*' * 30)

fish1 = FishCakeMaker()
fish2 = FishCakeMaker(size  = 20, price = 30)
fish3 = FishCakeMaker(flavor = "초코", size = 15)

fish1.show()
fish2.show()
fish3.show()