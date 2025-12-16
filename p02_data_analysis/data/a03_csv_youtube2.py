import csv

with open('../source/singer2.csv', "r") as inFp:
  csv_reader = csv.reader(inFp)
  header = next(csv_reader)
  print(header[1], header[6])
  for row_list in csv_reader:
    utube = int(row_list[6].replace(',', ''))
    utube = int(utube/10000)
    print(row_list[1], str(utube) + "만", end="\t")
    print()