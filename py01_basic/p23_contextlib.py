from contextlib import closing


class OpenClose:

  def open(self):
    print("작업을 시작합니다.")

  def do_something(self):
    print("작업을 진행합니다...")
    print("작업을 진행합니다...")
    print("작업을 진행합니다...")

  def close(self):
    print("작업을 종료합니다========")


def doOpenClose():
  d = OpenClose()
  d.open()
  d.do_something()
  d.close()

doOpenClose()

def doOpenClose():
  with closing(OpenClose()) as d:
    d.open()
    d.do_something()

doOpenClose()