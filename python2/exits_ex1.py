# exits_ex1.py 
import os
inFp = None
fName = ""
inList = []
inStr = ""
while( True ):
    fName = input("파일명을 입력하세요? ")
    if( os.path.exists(fName) ):
        with open( fName, "r", encoding="utf-8") as inFp:
            inList = inFp.readlines()
        print(inList ) 
        break   
    else:
        print("%s 파일 없습니다" % fName)    
#만약에 파일 없다면 다시 파일 입력되게 코드 만들기
