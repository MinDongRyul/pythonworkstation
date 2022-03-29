from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀바 설정
root.geometry("640x480") # 가로 * 세로 크기 설정

Label(root, text="메뉴 선택해주세요").pack(side="top")

Button(root, text="주문 하기").pack(side="bottom")

#버거프레임
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

#음료 프레임
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()
root.mainloop()