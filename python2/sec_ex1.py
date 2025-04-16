# sec_ex1.py
print( ord('파') ) # ord("문자") 문자의 유니코드값 반환
num = ord('파')
print( chr( num ) ) #chr( 숫자 )
# 숫자에 해당되는 유니코드 문자 반환
aa = chr( num + 100 ) # 54128의 유니코드문자
num = ord(aa)
print( chr(num - 100) ) 

inF, outF = None, None
inStr, outStr = "", ""
i=0
secu = 0

secuYN = input("1. 암호화  2. 암호해석  선택? ")
inFname=  input("입력 파일명은? ")
outFname = input("출력 파일명은? ")

if( secuYN == '1'):
    secu = 100
elif( secuYN == '2'):
    secu =  -100
inFp = open(inFname, 'r', encoding = 'utf-8')
outFp = open(outFname, 'w', encoding = 'utf-8')
while True :
    inStr = inFp.readline()    #"abcd"   
    if not inStr :
        break
    outStr = ""
    for i in range(0, len(inStr)):
        ch=inStr[i]
        chNum = ord(ch) 
        chNum = chNum + secu
        ch2  = chr( chNum ) 
        outStr = outStr + ch2
    outFp.write( outStr )
outFp.close()
inFp.close()        
print(' %s --> %s 변환 완료' % (inFname, outFname))