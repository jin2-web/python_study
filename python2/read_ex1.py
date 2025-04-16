# 요구사항
# data1.txt 파일을 읽어서 화면 출력하기
inF = None # 자료형이 무엇이지 아직 정해지지 않았다.
# 변수를 만든데 무엇을 넣을지 미지정(정해지지 않음)
inF = open( "./temp/data1.txt", "r", encoding="utf-8")
while( True ):
    inStr = inF.readline()
    if inStr == "": # 참이면 EOF(End Of File) 이다.
        break
    else:
        print( inStr )
inF.close() #자원반납     
# data2.dat파일 읽어서 화면 출력하기
inF = open( "./temp/data2.dat", "r", encoding="utf-8")
while( True ):
    inStr = inF.readline()
    if inStr == "": # 참이면 EOF(End Of File) 이다.
        break
    else:
        print( inStr )
inF.close() #자원반납    
