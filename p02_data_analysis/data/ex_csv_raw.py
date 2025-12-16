import csv
import struct

## 전역 변수부
inRawName = '../source/cat256.raw' # 원본
csvName =  '../source/cat256.csv'  # csv
outRawName = '../source/cat256_out.raw' # 흑백
row, col = 256, 256

## 메인 코드부
## RAW --> CSV로 저장
rawFp = open(inRawName, 'rb') # rb: 이진 파일을 읽는 모드
csvFp = open(csvName,'w', newline='')
csvWriter = csv.writer(csvFp)
csvWriter.writerow(['행', '열', '픽셀 값'])
for i in range(row) :
    for k in range(col) :
        tmp = rawFp.read(1) # 1 픽셀씩 읽어 드림
        value = int(ord(tmp))  # 1픽셀에 대한 value
        print(tmp, '/', value)
        row_list = [i, k, value]
        csvWriter.writerow(row_list)
rawFp.close()
csvFp.close()

## CSV 파일을 흑백으로
csvFp = open(csvName,'r')
csvReader = csv.reader(csvFp)
headerList = next(csvReader)
csvList = []
for cList in csvReader :
    value = int(cList[2]) #[i, k, value]
    if value > 128 :
        value = 255 # 백으로만 표현
    else :
        value = 0   # 흑으로만 표현
    csvList.append([cList[0], cList[1], value])

## CSV --> RAW
rawFp = open(outRawName, 'wb') # write binary
for cList in csvList :
        x, y, value = map(int , cList)
        rawFp.write(struct.pack('B', value))
rawFp.close()
print('Save. OK~')

