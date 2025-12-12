import tkinter
import tkinter.font
from tkinter import *

root = Tk()
root.title('MyWindow layout grid')
root.geometry('400x400')
root.config(bg="white")
# resizable은 0,1 또는 True, False 사용
root.resizable(1, True)
font = tkinter.font.Font(family="맑은 고딕", size=15)

btn1 = tkinter.Button(root, text="1", width=6)
btn2 = tkinter.Button(root, text="2", width=6)
btn3 = tkinter.Button(root, text="3", width=6)
btn4 = tkinter.Button(root, text="4", width=6)
btn5 = tkinter.Button(root, text="5", width=6)
btn6 = tkinter.Button(root, text="6", width=6)
btn7 = tkinter.Button(root, text="7", width=6)
btn8 = tkinter.Button(root, text="8", width=6)
btn9 = tkinter.Button(root, text="9", width=6)
# Grid는 지정한 프레임 내에서 격자 형태로 위젯을 행과 열로 배치
btn1.grid(row=3, column=1)
btn2.grid(row=3, column=2, columnspan=2, sticky=W+E+N+S)
# btn3.grid(row=3, column=3)
btn4.grid(row=2, column=1, rowspan=2, sticky=W+E+N+S)
btn5.grid(row=2, column=2)
btn6.grid(row=2, column=3)
btn7.grid(row=1, column=1)
btn8.grid(row=1, column=2)
btn9.grid(row=1, column=3)

btns = list()
for i in range(9):
  btns.append(tkinter.Button(root, text=i+1, width=6, font=font))
# print(btns)
idx = 8
# for i in range(1, 4, 1):
#   for j in range(1, 4, 1):
#     btns[idx].grid(row=i, column=j)
#     idx -= 1
# for i in range(1, 4, 1):
#   for j in range(1, 4, 1):
#     if j == 1 :
#       btns[idx].grid(row=i, column=j+2)
#     elif j == 3:
#       btns[idx].grid(row=i, column=j-2)
#     else:
#       btns[idx].grid(row=i, column=j)
#     idx -= 1
# for i in range(1, 4, 1):
#   for j in range(3, 0, -1):
#     btns[idx].grid(row=i, column=j)
#     idx -= 1

root.mainloop()
