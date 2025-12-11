import decimal

print("=== Python의 특징 ===")
'''
정적타입 언어 : 자료형을 컴파일 타임에 결정하는 언어
동적타입 언어 : 자료형을 런타임(실행 시점)에 결정하는 언어
약타입 언어 : 자료형이 맞지 않을 시에 암묵적으로 타입을 변환하는 언어
강타입 언어 : 자료형이 맞지 않을 시에 에러 발생, 암묵적 변환을 지원하지 않음
Python은 동적타입이면서, 약타입 언어, 변수 타입을 강제 지정 불가
'''

print("=== 파이썬 변수의 자료형 ===")
'''
변수의 type
Scalar 타입 : int, float, None, bool 4가지: 단수의 값
Composite 타입 : str, list, tuple, dict, set: 복수의 값

불 자료형: True, False
숫자 자료형: int, float, complex
군집 자료형: str, list, tuple, dict, set
help(str) # 각타입별 설명 출력
'''

print("=== 변수의 명명규칙 ===")
'''
1) 변수나 함수는 Snake case, 클래스는 Pascal
2) _, 영문자(대소문자 구별), 숫자(시작 안됨) 사용, 그외 문자 불가
3) 예약어 안됨(if, for, ...)
4) 특수문자, 공백 X
5) null 대신 None을 사용
'''

# 변수의 재선언(O), 업데이트(O), 타입 고정(X)
a = 10
a = True
print(a)
print(type(a))  # 객체지향적 언어

b = True
c = 3.14
print(type(a), type(b), type(c))

d = complex(3, -4)
e = 10 + 3j + 5J
print(type(d), type(e), d.real, d.imag)
s = 'hello'
print(s, type(s), )

# k = (a = 10 + 20) # 할당문이 다른 할당문을 포함할 수 없다.
k = a = 10 + 20
print("k, a : ", k, a)
k = b = a
print(k, type(k), )
n1 = 1;
n2 = 2
print("n1 = {}, n2 = {}".format(n1, n2))
print(f'n1 = {n1}, n2 = {n2}')
print("n1 = %d, n2 = %d" % (n1, n2))

a = 1; b = 2;
print('변수 교환전: a=%d, b=%d' % (a, b))
print("a = {}, b = {}".format(a, b))
print(f'a = {a}, b = {b}')
a, b = b, a
print('변수 교환후: a=%d, b=%d' % (a, b))

del a
# print(a)

# Python float는 내부적으로 C의 double을 그대로 사용
# Python에서 실수를 저장할때는 가까운 2진 부동소수점 형태로 변환.
# 소수점 16~17자리의 차이는 float 정밀도 한계라서
# 각각의 환경에 따라 반올림, 또는 근사값으로 반올림됨
a = 10.1234567890123452
b = 10.1234567890123453
print(a, type(a))
print(b, type(b))
print(a == b)
from decimal import Decimal
a = 10.1234567890123452
b = 10.1234567890123453
print(decimal.Decimal(a), type(a)) # 내부적으로 저장된 수
print(decimal.Decimal(b), type(b)) # 내부적으로 저장된 수
print(a == b)
# 정확하게 소수를 표현하려면 Decimal()을 사용
a = Decimal("10.1234567890123452")
b = Decimal("10.1234567890123453")
print(a)
print(b)
print(a == b)

print("a={}".format(a))
print("a=%f" % a)
print(f'a={a}')
print(f'소수 첫째 자리 반올림: a={round(a,2)}')
print(f'소수 첫째 자리 반올림: a={a:.2f}')
print('소수 첫째 자리 반올림: a={:.2f}'.format(a))
print('소수 첫째 자리 반올림: a=%.2f' % a)

# 변수의 영역 확인
print(f'{"변수 scope":=^20}')
# 파이썬 변수 scope 룰을 LEGB 룰
# 변수가 값을 찾을 때, Local -> Enclosed -> Global -> Built-in
# local - 가장 가까운 함수안 범위.
# Enclosed - 파이썬은 함수 안에 함수가 정의 될수 있는데, 가장 가까운 함수가 아닌 두번째 이상의 함수 가까운 함수범위.
# Global - 함수 바깥의 변수 또는 import된 module
# Built-in - 파이썬안에 내장되어 있는 함수 또는 속성들.
# 로컬변수를 확인하는 locals()
# 글로벌변수를 확인하는 globals()
print('math' in globals())
import math
print('math' in globals())
from math import factorial
print('factorial' in globals())

# 지수 표현
print("1)", 123e2, type(123e2))
print("2)", 123e-2, type(123e-2))

# 복소수 표현
print(f"{"complex":=^20}")
a = 10 + complex(3)
print(a, type(a))
print(a.real, a.imag)

# None 표현
print(f"{"None":=^20}")
print(type(None), None)
print('' == None)
a = None
a: int | None  # Python 3.10 이상
a = True
print(a, type(a))

print(f"{"문자형":=^20}")
print("hello", type("hello"))

print(f"{"형변환 함수":=^20}")
print("int 형변환함수", int(12.74), type(int(12.74))) #절삭
print("float 형변환함수", float(123), type(float(123)))
print("complex 형변환함수", complex(3, 4), type(complex(3, 4)))
print("bool 형변환함수 bool(-1)", bool(-1))
print("bool 형변환함수 bool(0)", bool(0))
print("bool 형변환함수 bool(1)", bool(1))
print("bool 형변환함수 bool(0.1)", bool(0.1))
print("bool 형변환함수 bool('')", bool(''))
print("bool 형변환함수 bool(None)", bool(None))
print("str 형변환함수 str(None)", str(None))
print("str 형변환함수 str(97)", str(97))
print("chr 형변환함수 chr(97)", chr(97))
try:
  b = int("a10")  # 문자열, 수치자료를 int type 변경
  b = float("a0.12")  # 문자열, 수치자료를 float type 변경
except:
  print("숫자가 아닌 문자열이 포함되어 있습니다.")

string = "abc123def456"
number_string = ""
for char in string:
    if char.isdigit():
        number_string += char
number = int(number_string)
print(number, type(number)) # 출력: 123456

a="A";
print(ascii(a), end=' '); print(str(a), end=' '); print(ord(a));
a=65;
# chr()는 매개변수가 숫자여야만 함.
print(ascii(a), end=' '); print(str(a), end=' '); print(chr(a));

print("=" * 10)
print("Hello Python"[0])
print("Hello Python"[-3])
print("Hello Python"[0:12:3])  # [a:b:c] c폭

# python에는 상수가 없다.  python은 동적언어이기 때문에 상수가 불필요
from typing import Final
SIZE:Final = 5
SIZE = 10
print(SIZE)

import p04_constant as const
const.PI = 3.14
print(const.PI)

# 에러 발생. 재할당이 안됨.
# const.PI = 3.141592
# print(const.PI)

word = None
print(word)