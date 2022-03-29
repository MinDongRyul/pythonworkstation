import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀바 설정
root.geometry("640x480") # 가로 * 세로 크기 설정

values = [str(i) + "일" for i in range(1, 32)] # 1 ~ 31까의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정 , 버튼 클릭을 통한 값 설정 가능

readonlycombobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonlycombobox.pack()
readonlycombobox.current(0) # 0번째 인덱스값 선택

def btncmd():
    print(combobox.get())
    print(readonlycombobox.get()) # 선택된 값 표시

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()