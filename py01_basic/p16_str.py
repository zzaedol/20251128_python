# String은 글자의 Unicode 코드로 이루어진 불변한 순서있는 집합.
# "" (쌍따옴표), ''(작은따옴표) 모두 사용

""" 이것은 멀티라인
 입력입니다.
"""
'''
이것도 멀티라인
'''

# 이스케이프 문자
a = "이스케이프 문자 \n 라인이 바뀜 \\ 쌍따옴표를 또 쓰기 \"\" "
print(a)

# 유니코드 문자열을 16진수로 바로 입력
print('\xe5')
print('\u0000')

# 컬렉션 접근
s = 'abcdef'
print(s[3])

# str():: int, float -> str 변환
print(type(str(396)), '396')
print(type(str(5.52)),'5.52')
print(type(str(6.02e10)),6.02e10) # 60200000000.0
print(type(str(6.02e20)),6.02e20) # 6.02e+20


# String 여러가지 메소드
print(','.join(['a', 'b', 'cde']))
print('a,b,cde'.split(','))
departure = "Seattle-Seoul".split('e')
print(departure)
# partition()은 3개의 값만 반환
departure, ttt, arrival = "Seattle-Seoul".partition('e')
print(departure, ttt, arrival)

print("Name: {}, Age: {}".format("철수", 13))
print("Name: {0}, Age: {1}".format("영희", 15))
print("Name: {0}, Age: {1}: {0}의 나이가 {1}".format("민수", 17))
print("Name: {name}, Age: {age}: {name}의 나이가 {age}".format(age=19, name='재석'))
pos = [12.5, 35, 90]
print("A의 좌표는 x = {p[0]}, y = {p[1]}, z = {p[2]}".format(p=pos))

import math

print('수학에서 파이= {m.pi}'.format(m=math))
print('수학에서 파이= {m.pi:.3f}'.format(m=math))
print('수학에서 파이= {m.pi:.2f}'.format(m=math))

a = "abcDef"
print(a.capitalize())
print(a.upper())
print(a.lower())

s = "  abc   "
print(s.strip())

print(len("abcd12345abcdefg"))