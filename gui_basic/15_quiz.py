from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장") # 타이틀바 설정
root.geometry("640x480") # 가로 * 세로 크기 설정

txt = Text(root) # 텍스트 위젯 생성 , 여러줄
txt.pack(fill="both", expand=True) # fill=both, expand =True : 전체공간 채우기
txt.insert(END,"")

def file():
    txt.delete("1.0", END)
    f = open("C:/Users/82102/Desktop/pythonworkstation/gui_basic/mynote1.txt",'r',encoding="utf-8") 
    i = f.read()
    for d in i:
        txt.insert(END,"{0}".format(d))
    f.close()    

def save_file():
    f = open("C:/Users/82102/Desktop/pythonworkstation/gui_basic/mynote1.txt",'a',encoding="utf-8")
    a =  txt.get("1.0", END)
    for x in a:
        f.write("{0}".format(x))
    txt.delete("1.0", END)
    f.close()

menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

menu.add_cascade(label="편집")
menu.add_cascade(label="서식") 
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

scrollbar = Scrollbar(txt)
scrollbar.pack(side="right",fill="y")

# set 이 없으면 스크롤을 내려도 다시올라옴
txt = Text(txt,width= 640, height=480, yscrollcommand=scrollbar.set)
d =  txt.get("1.0", END)
for f in d:
    txt.insert(END, "{0}".format(f))
txt.pack(side="left")
scrollbar.config(command=txt.yview)

root.config(menu=menu) # menu에다가 menu넣어주기
root.mainloop()
