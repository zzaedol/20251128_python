print("{0:=^20}".format("반복문"))
print(f'{"반복문":=^20}')
'''
for 변수 in 리스트(또는 튜플, 문자열):
  수행 문장1
  수행 문장2
  ...
'''

ls = []
for i in range(10):
  ls.append(i)
print(ls)

# Python에서 권장하지 않는 패턴
ls = ["a", "b", "c"]
for i in range(len(ls)):
  print(ls[i])

# Python에서 권장하는 패턴
ls = ["a", "b", "c"]
for i in ls:
  print(i) # 원소를 출력

a = [(97, 'a'), [98, 'b'], (99, 'c')]
print(a,type(a))
for(i, v) in a:
  print(i, v)

marks = [90, 25, 67, 45, 80]
for i in marks:
  # if i >= 60: print(i)
  if i < 60: continue
  print(i)

for i in range(97, 97+26):
  print(chr(i), end=' ')
print()

a = "123a456"
result = 'Numeric' if (a.isnumeric()) else 'String'
print(result)

def two_digit(num):
  return str(num) if(num>9) else "0"+ str(num)

print(f'{"구구단":=^20}')
for i in range(2, 10):
  for j in range(1, 10):
    # print(f'{i} * {j} = {two_digit(i * j)}')
    print(f'{i} * {j} = {(i * j):2d}')
  print()

# range(start, stop, step)
for i in range(2, 10, 3):
  for j in range(1, 10):
    for k in range(0, 3):
      if not ((i + k) == 10):
        print(f'{i + k} * {j} = {(i + k) * j:2d}', end='\t')
    print()
  print()

a = list(range(0, 10)) # list 의 즉각적인 선언
print("a:", a)

i=0
while i < len(a):
  print("짝" if(a[i]%2==0) else "홀", end='\t')
  i+=1
print()

# python 에서는 변수가 선언만 따로 안됨.
password = "secret"
count = 0
while True:
  count += 1
  word = input("암호를 입력하세요: ").lower()
  if word == password:
    print("Welcome!")
    break
  if count > 5:
    print("접근 불허")
    break
print("password:", password)

# enumerate는 반복문 사용 시 몇 번째 반복문인지 확인이 필요할 때 사용
# 인덱스 번호와 컬렉션의 원소를 tuple형태로 반환
t = [1, 5, 7, 33, 39, 52]
for p in enumerate(t):
  print(p)

for i, v in enumerate(t):
  print("index : {}, value: {}".format(i, v))