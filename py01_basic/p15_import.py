# 파이썬에서의 모듈은 파이썬코드로 이루어진 파일.
# 함수나 변수, 클래스등의 코드를 파일로 정의하고
# 이것을 다른 파이썬 파일 그리고 다른 실행환경에서 import 하여 사용

import p15_module as module

print(type(module))  # <class 'module'>
# dir 내장함수는 객체가 가지고 있는 변수나 함수리스트를 보여줌
print(dir(module))  # 모든 것은 객체다.
print(module.fetch_words.__doc__) #모듈의 첫번째 줄의 큰따옴표,홑따옴표 3개

module.fetch_words()