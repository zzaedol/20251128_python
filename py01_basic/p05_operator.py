print(f"{" 산술 연산자 +,-,*,/,%,//,** ":=^20}")
a = 10
b = 3
print(a + b, a - b, a * b, a / b)
print(10 % 3)  # 나머지
print(10 // 3)  # 몫
print(10 ** 3)  # 제곱

print(f"{" 비트 연산자 &, |, ^, ~, >>, << ":=^35}")
print(bin(0b101 & 0b010))  # 비트 and
print(bin(0b101 | 0b010))  # 비트  or
print(bin(0b001 ^ 0b010))  # 비트  exclusive or
print(bin(~0b001))  # 비트  not
print("%s<<2 => %s" % (bin(2), bin(2 << 2)))  # shift <<, >>

# 대입연산자 :: +=,-=,*=,/=,%=,//=,**=
total = 0
for i in range(1, 10):
  total += i
print(total)

# 비교연산자 :: <,>,=,<=,>=,==,!=
# 논리연산자 :: and, or, not
print(a > 10 and b < 5)
print(a > 10 or b < 5)
print(a == 10 or b != 5)

num = 4
print(num, bin(num))
print(~num, bin(~num))  # 숫자에 ~를 붙이면 2의 보수가 출력

# 삼항연산자가 없다.
a = 3
a = 10 if a > 5 else 5
print(a)

# 문자열 연산자:: +, *
a = "hello "
print(a + "world")
# print(a + 10)  # 문자열은 타입이 같을 경우에만 +로 처리가능
print(a + str(10))
print(a * 3)
print("=" * 20)

# 문자열 slicing
print("Hello Python"[0])  # indexing 시작은 0 부터
print("Hello Python"[-4])  # indexing 끝은 -1 부터
# print("Hello Python"[20]) #IndexError: string index out of range
print("Hello Python"[0:4])  # slicing 끝 글자 미포함
print("Hello Python"[:5])  # slicing 0~4까지
print("Hello Python"[6:])  # slicing 6부터 끝까지
print("Hello Python"[0:20])  # slicing 에러 무발생
print("Hello Python"[0:20:3])  # 3 폭