with open('../source/singer1.csv', 'r') as inFp:
  with open('../source/singer1_copy.csv', 'w') as outFp:
    header = inFp.readline()
    header = header.strip()
    header_list = header.split(',')
    outFp.write(','.join(map(str, header_list)) + "\n")
    for inStr in inFp:
      inStr = inStr.strip()
      row_list = inStr.split(',')
      outFp.write(','.join(map(str, row_list)) + "\n")
print('Save Finished')
