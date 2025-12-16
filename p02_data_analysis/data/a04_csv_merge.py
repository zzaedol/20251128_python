import csv

with open("../source/singerA.csv", "r") as inFpA :
    with open("../source/singerB.csv", "r") as inFpB:
        with open("../source/singerSum.csv", "w", newline='') as outFp:
            csvReaderA = csv.reader(inFpA)  # csv읽어드린 집합 객체
            csvReaderB = csv.reader(inFpB)  # csv읽어드린 집합 객체
            csvWriter = csv.writer(outFp)   # csv쓰기위한 집합 객체
            header_list = next(csvReaderA)  # 첫번째 라인을 읽음
            header_list = next(csvReaderB)  #위라인과 동일한 기능을 중복 적용함.
            csvWriter.writerow(header_list)

            for row_list in csvReaderA:
                csvWriter.writerow(row_list)
            for row_list in csvReaderB:
                csvWriter.writerow(row_list)

print('Save. OK~')






