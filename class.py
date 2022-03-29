class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def show_info(self):
        print("이름 : ", self.name, "/ 색상 : ", self.color)
    def __del__(self):
        print("인스턴스가 삭제되었습니다")

class car_num(Car):
    def __init__(self, name, color, num):
        self.name = name
        self.color = color
        self.num = num
    def attack(self):
        print(self.name, "이(가) 들이 박습니다.")
    
car1 = car_num("아반테","빨간색","6407")
car1.show_info()
car1.attack()