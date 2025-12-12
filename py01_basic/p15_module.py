from urllib.request import urlopen

file_location = 'C:\\workspace\\spaceAI\\20251128_python\\py01_basic\\p15_import.py'


def fetch_lines():
  ''' 줄 단위로 읽어서 담기  '''
  with open(file_location, 'r', encoding='utf-8') as story:
    story_lines = []
    for line in story: story_lines.append(line)  # 라인으로 담기
  for line in story_lines:
    # 줄바꿈이 이미 포함되어 있으므로 end='' 사용
    if line.strip(): print(line, end='')


def fetch_words():
  '''단어 단위로 읽어서 담기'''
  with open(file_location, 'r', encoding='utf-8') as story:
    story_words = []
    for line in story:
      line_words = line.split()
      for word in line_words: story_words.append(word)
  for word in story_words: print(word)


def fetch_line_url():
  """
    url주소에서 파일을 가져와 라인을 반환합니다.
    :param url: 불러올 url
    :return:
  """
  with urlopen(file_location) as story:
    story_lines = []
    for line in story: story_lines.append(line)  # 라인으로 담기
  for line in story_lines: print(line)


# p12_module.py를 ctrl+shift+f10으로 직접 실행해보면 __main__ 출력됨.
print(__name__)

# 위의 print(__name__)을 주석 처리하고 직접 실행하시오.
# __name__은 script로 실행되는 것인지 아니면 import되는 것인지 구분이 가능
if __name__ == '__main__':
  fetch_lines()