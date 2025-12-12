import random
import sys
import threading
import time

# 클래스 Bomb 선언
class Bomb(threading.Thread):
  # 생성자
  def __init__(self):
    threading.Thread.__init__(self)
    self.life = random.randint(1, 2)
    self.state = False

  # Thread를 상속 받으므로 인해 비동기 프로그래밍 가능
  def run(self):
    for i in range(10, 0, -1):
      if self.state: break;
      print(i)
      time.sleep(0.5)
    if not self.state: print("Bomb~!")
    sys.exit()

  def choose(self, line):
    self.state = True
    try:
      line = int(line)
    except Exception as e:
      line = 1

    print(f'{line}을 선택하셨습니다')
    if (self.life == line):
      print('Alive~!')
    else:
      print('Bomb~!')