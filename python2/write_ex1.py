# write_ex1.py
outF = None
outStr = ""
fName=input("저장할 파일명 입력 ")
outF = open( fName, "a", encoding="utf-8")
while( True ) :
    outStr = input("저장할 내용을 키보드로 입력 ? ")
    if( outStr != "") :
        outF.writelines( outStr + "\n")
    else:
        break  
outF.close()      
print("파일이 저장되었습니다")