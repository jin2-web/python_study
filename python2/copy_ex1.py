# copy_ex1.py
inF, outF = None, None
inStr = ""
source =input("소스파일명을 입력하세요:")
target = input("타킷 파일명을 입력하세요:")
inF = open( source, "rb" )
outF = open( target, "wb")
'''
while( True) :
    i = inF.read() #입력파일에서 한 바이트씩 읽어오기
    if( i == ""): #파일을 끝까지 읽으면
        break
    else:
        outF.write(i) #출력파일에 한 바이트씩 써주기
'''
for i in inF.readlines():
    outF.write(i)
inF.close()
outF.close()    