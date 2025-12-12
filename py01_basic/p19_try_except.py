import sys


def convert(s):
  """int로 변환"""
  a = int(s)
  return a


print(convert("55"))


# print(convert("test"))  에러발생

def convert(s):
  """int로 변환"""
  try:
    a = int(s)
  except ValueError:
    a = -1
  return a


print(convert("55"))
print(convert("test"))


def convert(s):
  """int로 변환"""
  try:
    a = int(s)
    print('성공')
  except ValueError:
    print('실패')
    a = -1
  return a


print(convert("55"))
print(convert("test"))


# raise로 특정 에러를 발생
def convert(s):
  """int로 변환"""
  try:
    return int(s)
  except (ValueError, TypeError) as e:
    print('에러정보 : ', e, file=sys.stderr)
    # raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
  finally:
    print('여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.')


print(convert("55"))
# print(convert("test"))


# finally block
def convert(s):
  """int로 변환"""
  try:
    return int(s)
  except (ValueError, TypeError) as e:
    print('에러정보 : ', e, file=sys.stderr)
    # raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
  finally:
    print('여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.')


# else 블록
def convert(s):
  """int로 변환"""
  try:
    a = int(s)
  except (ValueError, TypeError) as e:
    print('에러정보 : ', e, file=sys.stderr)
    raise ValueError("Argument에 잘못된 값이 전달되었습니다.")
  else:
    print('에러가 발생하지 않을 경우 무조건 출력!')
  finally:
    print('여기는 에러가 발생할 때도, 안 할때도 무조건 실행됩니다.')
  return a

print(convert("55"))
# print(convert("test"))

# EAFP - 'It's Easier to Ask Forgiveness than Permission' 의 줄임말. 허락보다 용서구하는 것이 쉽다.
# LBYL - 'Look Before You Leap'의 줄임말입니다. 도약하기전에 봐라. 라는 뜻.
# LBYL 스타일은 어떤 것을 실행하기전에 에러가 날만한 요소들을 조건절로 검사를 하고 수행하는 스타일.
# EAFP 스타일은 예외처리를 활용하여 검사를 수행하지 않고 일단 실행하고 예외처리를 진행하는 스타일.
# 파이썬은 EAFP 스타일을 권장.
# EAFP는 Python에서 표준이며, 철학은 예외에 의해 가능합니다.
# 대신 오류 코드를 사용하는 예외가 없으면 오류 처리를 논리의 기본 흐름에 직접 포함시켜야합니다.
# 예외로 인해 메인 플로우가 중단되므로 예외적 인 경우가 아닌 로컬로 처리 할 수 ​​있습니다.
# EAFP와 결합 된 예외는 오류 코드 예외를 쉽게 무시할 수 없기 때문에 우수합니다.
# 기본적으로 예외는 큰 효과가 있지만 오류 코드는 기본적으로 무음이므로 예외 EAFP- 기본 스타일은 문제를 자동으로 무시하기 어렵게 만듭니다.


# LBYL 코딩 스타일
'''
if k in dic:
    process(dic[k])
else:
    process(None)
# As an expression:
process(dic[key] if key in dic else None)
'''

# EAFP 코딩 스타일
'''
try:
    process(dic[key])
except KeyError:
    process(None)
# As an expression:
process(dic[key] except KeyError: None)
'''


print(f'{"운영체제별 처리":=^20}')
'''
정확하게는 Windows와 유닉스계열(Mac, 리눅스)처리로 구분.
Python에서 콘솔에서 아무키나 누르는 것과 같은 단일 키 누르기를 감지하려면, 
운영체제별 모듈을 사용해야 함.
Windows - msvcrt
Linux, Mac - sys, tty, termios
'''
try:
  # Windows용 코드
  import msvcrt
  def getkey():
    """
    msvcrt.getch()사용자가 키를 누르는 즉시 해당 문자를 반환, 화면 출력없음
    input() 사용자가 enter키를 눌러야 프로그램이 입력받음(버퍼링방식)
    """
    print("아무키나 누르세요...")
    # key_byte = msvcrt.getch()
    # print(type(key_byte), key_byte)
    print(f"사용자가 누른키: {msvcrt.getch()}")
except ImportError:
  # Linux & Mac 용 코드
  import sys
  import tty
  import termios

  def getkey():
    """단일키 누르는 것을 받아옴"""
    fd = sys.stdin.fileno()
    original_attributes = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, original_attributes)
    return ch
  print("오류: 숫자를 입력해야 합니다.")

getkey()