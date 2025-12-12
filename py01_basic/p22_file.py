# 파이썬에서 파일 다룰 때는 기본 내장함수 open() 함수를 활용.
# open() 함수의 사용법
# 첫번째 인수 file경로만이 필수.
# mode를 작성할 때 r(읽기), w(쓰기), a(추가하기) 세가지중 하나와
# t(텍스트)와 b(바이너리) 둘중 하나와 반드시 결합해야하며,
# 나머지는 optional하게 사용가능
'''
'r' : 읽기 용으로 열림 (기본값)
'w' : 쓰기 위해 열기, 파일을 먼저 자른다.
'x' : 베타적 생성을 위해 열리고, 이미 존재하는 경우 실패
'a' : 쓰기를 위해 열려 있고, 파일의 끝에 추가하는 경우 추가합니다.
'b' : 2진 모드(바이너리 모드)
't' : 텍스트 모드 (기본값)
'+' : 업데이트 (읽기 및 쓰기)를 위한 디스크 파일 열기
'U' : 유니버설 개행 모드 (사용되지 않음)
'''

# 파일 다루기 기본
file = "test.txt"
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 파일 쓰기
f = open('test.txt', mode='wt', encoding='utf-8')
# help(f)
f.write('파이썬으로 파일을 작성하고 있습니다.')
f.write('newline 문자로 개행해봅니다.\n')
f.write('개행이 잘되었나요?')
f.close()

r = open('test.txt', mode='rt', encoding='utf-8')
r.read(2)

# 파일 추가하기
a = open('test.txt', mode='at', encoding='utf-8')
a.writelines(['writelines로 추가합니다.', '내부 원소는 개행이 안되는군요.', '개행을 하려면 개행문자를 입력해야합니다.\n', '마지막에는 안붙여도 개행문자가..'])
a.close()

# Iterable한 파일 객체의 특성을 이용한 읽기
import collections
r = open('test.txt', mode='rt', encoding='utf-8')
# isinstance(r, collections.Iterable)

try:
    f = open('test.txt', mode='wt', encoding='utf-8')
    f.write('파이썬으로 파일을 작성하고 있습니다.')
    f.write('newline 문자로 개행해봅니다.\n')
    f.write('개행이 잘되었나요?')
finally:
    f.close()

with open('test.txt', mode='wt', encoding='utf-8') as f:
  f.write('파이썬으로 파일을 작성하고 있습니다.')
  f.write('newline 문자로 개행해봅니다.\n')
  f.write('개행이 잘되었나요?')
