def a(str, len=20):
  print(f'{str:=^{len}}')


def print2d(list):
  max_val = max_2d(list)
  formatstr = f'%{len(str(max_val))}d'

  # for i in range(len(list)):
  #   for j in range(len(list[i])):
  #     print(formatstr % list[i][j], end='')
  #   print()
  for row in list:
    for col in row:
      print(formatstr % col, end='')
    print()
  print()

def max_2d(list):
  max_val = max(map(max, list))


