with open('../source/singer2.csv', "r") as inFp:
  header = inFp.readline()
  header = header.strip()
  header_list = header.split(',')
  print(header_list[1], header_list[6])
  for inStr in inFp:
    inStr = inStr.strip()
    findIdx = inStr.find('"')
    if(findIdx == -1):
      row_list = inStr.split(',')
      youtube = int(row_list[6])
      youtube = int(youtube / 10000)
      print(row_list[1], str(youtube) + "만", end="\t")
    else:
      row_list = inStr.split(',')
      youtube = inStr[inStr.find("\""):]
      print(row_list[1], youtube+"만")
    print()