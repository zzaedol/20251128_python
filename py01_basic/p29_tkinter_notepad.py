import tkinter
from tkinter import *
from tkinter.filedialog import *
from tkinter import scrolledtext
from tkinter.messagebox import askyesno


def new_file():
  if (len(str(scroll_text.get(1.0, END))) > 1):
    answer = askyesno("확인", "저장하시겠습니까?")
    print(answer)
    if (answer):
      save_file()
    else:
      scroll_text.delete(1.0, END)


def save_file():
  f = asksaveasfilename(
    initialfile='noname.txt',
    defaultextension='.txt',
    filetypes=[('Text Files', '.txt',)])

  if (f.strip() != ""):  # 저장하려고 할 때
    save_tmp = str(scroll_text.get(1.0, END))
    with open(f, 'w', encoding='UTF-8') as file:
      file.write(save_tmp + "\n")


def open_file():
  new_file()
  f = askopenfilename(
    initialdir='/',
    title="Select a file",
    filetypes=[('Text Files', '.txt'), ('CSV Files', '.csv'),
               ('Python Files', '.py')])
  # scroll_text.delete(1.0, END)  # 기존 텍스트 지우기
  if (f.strip() != ""):
    try:
      with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    except UnicodeDecodeError:
      with open(f, 'r', encoding='cp949') as file:  # 또는 euc-kr
        lines = file.readlines()

    scroll_text.pack()
    scroll_text.delete(1.0, END)  # 기존 텍스트 지우기
    content = ''.join(lines)
    scroll_text.insert(tkinter.CURRENT, content)


def info():
  info_view = Toplevel(window)
  info_view.geometry('300x50+350+400')
  info_view.title('Maker: LGH')
  # info_view.attributes('-topmost', 'true') # 항상 화면의 위쪽에 포진
  info_view.grab_set() # modaless 적용
  lb = Label(info_view, text="널 위해 준비했어!!")
  lb.pack()


window = Tk()
window.title('MyNotepad')
window.geometry('400x400+300+300')
window.resizable(1, 1)

# 메뉴프레임생성
menu = Menu(window)

# 첫번째 메뉴
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="New", command=new_file)
menu_1.add_command(label="Save", command=save_file)
menu_1.add_command(label="Open", command=open_file)
menu_1.add_separator()
menu_1.add_command(label="Close", command=window.destroy)
menu.add_cascade(label='File', menu=menu_1)

# 두번째 메뉴
menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="Info", command=info)
menu.add_cascade(label='Help', menu=menu_2)

# scrolledtext 창에 추가하기
scroll_text = scrolledtext.ScrolledText(window)
scroll_text.config(width="100", height="100")
scroll_text.pack(fill="both")

# 메뉴 본창에 붙이기
window.config(menu=menu)

window.mainloop()