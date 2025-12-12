import time

def task1():
    print("Task 1 시작")
    time.sleep(2)  # 2초 대기 (블로킹)
    print("Task 1 완료")

def task2():
    print("Task 2 시작")
    time.sleep(1)  # 1초 대기
    print("Task 2 완료")

# task1()
# task2()

import asyncio

async def task1():
    print("Task 1 시작")
    await asyncio.sleep(2)  # 비동기 대기 (논블로킹)
    print("Task 1 완료")

async def task2():
    print("Task 2 시작")
    await asyncio.sleep(1)
    print("Task 2 완료")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

import p20_Bomb as Bomb
from tkinter import simpledialog

b = Bomb.Bomb()
b.start()
score = simpledialog.askinteger("Input", "Your choose(Red = 0, Blue = 1)?", parent=None)
b.choose(score)