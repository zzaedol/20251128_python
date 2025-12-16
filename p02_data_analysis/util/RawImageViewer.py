from tkinter import *
from tkinter.filedialog import *


def open_file():
  f = askopenfilename(
    initialdir='/',
    title="Select a file",
    filetypes=[('Raw Files', '.raw')])
  if (f.strip() != ""):
    loadImage(f)
    displayImage(inImage)


def loadImage(fname):
  global inImage, XSIZE, YSIZE
  fp = open(fname, 'rb')

  for i in range(0, XSIZE):
    tmpList = []
    for k in range(0, YSIZE):
      data = int(ord(fp.read(1)))
      tmpList.append(data)
    inImage.append(tmpList)
  fp.close()


def displayImage(image):
  global XSIZE, YSIZE
  rgbString = ""
  for i in range(0, XSIZE):
    tmpString = ""
    for k in range(0, YSIZE):
      data = image[i][k]
      tmpString += "#%02x%02x%02x " % (data, data, data)  # x 뒤에 한칸 공백
    rgbString += "{" + tmpString + "} "  # } 뒤에 한칸 공백
  paper.put(rgbString)


def info():
  info_view = Toplevel(window)
  info_view.geometry('300x50+350+400')
  info_view.title('Maker: LGH')
  # info_view.attributes('-topmost', 'true') # 항상 화면의 위쪽에 포진
  info_view.grab_set()  # modaless 적용
  lb = Label(info_view, text="널 위해 준비했어!!")
  lb.pack()


canvas = None
XSIZE, YSIZE = 256, 256
inImage = []  # 2차원 리스트 (메모리)
window = Tk()
window.title('Raw Viewer')
window.geometry('400x400+300+300')
window.resizable(1, 1)

# 메뉴프레임생성
menu = Menu(window)

# 첫번째 메뉴
menu_1 = Menu(menu, tearoff=0)
menu_1.add_command(label="Open", command=open_file)
menu_1.add_separator()
menu_1.add_command(label="Close", command=window.destroy)
menu.add_cascade(label='File', menu=menu_1)

# 두번째 메뉴
menu_2 = Menu(menu, tearoff=0)
menu_2.add_command(label="Info", command=info)
menu.add_cascade(label='Help', menu=menu_2)

# scrolledtext 창에 추가하기
canvas = Canvas(window, height=XSIZE, width=YSIZE)
paper = PhotoImage(width=XSIZE, height=YSIZE)
canvas.create_image((XSIZE / 2, YSIZE / 2), image=paper, state="normal")

# 메뉴 본창에 붙이기
window.config(menu=menu)
canvas.pack()
window.mainloop()