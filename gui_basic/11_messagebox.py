import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI") # 타이틀바 설정
root.geometry("640x480") # 가로 * 세로 크기 설정

# 기차 예매 시스템 이라고 가정
def info():
    msgbox.showinfo("알림","정상적으로 예매 완료되었습니다.") # 타이틀, 메세지

def warn():
    msgbox.showwarning("경고","해당 좌석은 매진되었습니다") # 타이틀, 메세지

def error():
    msgbox.showerror("에러","결제 오류가 발생되었습니다.") # 타이틀, 메세지

def okcancel():
    msgbox.askokcancel("확인 / 취소","해당 좌석은 유아동반석입니다. 예매하시겠습니다까?") # 타이틀, 메세지

def retrycancel():
    response = msgbox.askretrycancel("재시도 / 취소","일시적인 오류입니다. 다시 시도 하겠습니까??") # 타이틀, 메세지
    if response == 1: # 재시도
        print("재시도")
    elif response == 0: # 취소
        print("취소")

def yesno():
    msgbox.askyesno("예 / 아니오","해당 좌석은 역방향입니다. 예매하시겠습니까?") # 타이틀, 메세지

def yesnocancel():
    response =msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다. \n저장후 프로그램을 저장히겠습니까?") # 타이틀, 메세지
    # 네 : 저장후 종료
    # 아니오 : 저장하지않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업)
    print("응답:", response)
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()




root.mainloop()