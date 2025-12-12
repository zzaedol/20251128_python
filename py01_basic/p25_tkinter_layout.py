import tkinter.font
from tkinter import *

window = Tk()
window.title('MyWindow')
window.geometry('400x400+300+300')
window.config(bg="skyblue")
# resizable은 0,1 또는 True, False 사용
window.resizable(1, True)

# Tkinter 위젯 배치 방법
# 1) pack (상대위치)
btn1 = Button(window, text="Left", relief="solid",
              overrelief="groove", anchor="s")
btn1.pack(side="left", fill="y")

btn2 = Button(window, text="Right", font=tkinter.font.Font(size=15))
btn2.pack(side="right")

# width=100 (100픽셀을 의미), windth=100m(100mm를 의미), 버튼의 width는 보통 6
font = tkinter.font.Font(family="맑은 고딕", size=20, slant="italic")
btn3 = Button(window, text="Top", width=15, height=5, anchor="se", font=font)
btn3.pack(side="top")

btn4 = Button(window, text="Close", command=window.quit)
btn4.pack(side="bottom")

entry = Entry(window)
entry.pack()  # 상대 위치 지정안하면 top에서 시작

window.mainloop()