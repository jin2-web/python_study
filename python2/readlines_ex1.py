# readlines_ex1.py 
inF = None
inStr = ""
#print( type( inF ) )
#print( type( inStr ) )

inF = open( "./temp/data1.txt", "r", encoding="utf-8")
inStr = inF.readlines()
print( inStr )
inF.close()

with open( "./temp/data1.txt", "r", encoding="utf-8") as inF:
   inStr = inF.readlines() 
   print(inStr )

#문제3 
f = input("파일명을 입력하세요?")
with open( f, "r") as inF :
   inStr = inF.readlines()
   print( inStr )
  
 