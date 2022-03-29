from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀바 설정
root.geometry("640x480") # 가로 * 세로 크기 설정

txt = Text(root, width=30, height=5) # 텍스트 위젯 생성 , 여러줄
txt.pack()
txt.insert(END, "글자를 입력하세요") # 기본값 제공

e = Entry(root, width=30) # 한줄
e.pack()
e.insert(0, "한 줄만 입력해요") # 현재는 값이 비어있으므로 end사용가능

def btncmd():
    # 내용출력
    print(txt.get("1.0", END)) # 텍스트 내용 가져오기 1.0: 첫번째 라인, 0: 0번째 column 위치
    print(e.get())

    # 내용삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text= " 클릭", command=btncmd)
btn.pack()

root.mainloop()
