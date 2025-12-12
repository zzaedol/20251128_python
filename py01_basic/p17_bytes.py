# bytes는 유니코드가 아닌 문자열을 사용하는 것과 유사함.
# bytes는 원시 이진 데이터로 사용되어지거나 1바이트 문자로 고정을 위해 사용.
# bytes HTTP 응답과 같은 파일과 네트워크 리소스는 바이트 스트림으로 전송되기 때문에 이해하는 것이 중요.
# 반면에 우리는 유니 코드 문자열의 편의성을 선호합니다. 그렇기에 상호변환을 하는 경우가 많다.

b = b'abcde'
print(b)
print(type(b))

s = b'abc def ghi'
print(s.split())

s = '파이썬을 활용하여 데이터를 다뤄봅시다!'
b = s.encode('utf-8')
print(b)
print(b.decode('utf-8'))


