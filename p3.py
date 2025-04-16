detected_risks=['고온', '기계 과부하', '가스 누출']
print( detected_risks[2])

print( type(10) )
print( type(3.14))
print( type('abc')) #str 
print( type("love")) #str
print( type( True ) ) #bool 부울
print( type(False) ) 
list1 = [1,2,3,4] # list
# 요구사항 list1의 자료형을 출력하기
print( type( list1 ))
list2 = [1, 3.5, 'a', True]
print( type( list2 ))
tuple1 = (1,2,3,4)
print( type( tuple1 )) #tuple 
tuple2 = (1, 3.5, 'a', True)
print( type( tuple2 )) 
if( False ):
    print("참")
else:
    print("거짓")

login = False
if( not login ):
    id='admin'
    pw=1234  
    login = True   
if( login ) :
    print("로그온")        

tom = 'boy '
bob = 'I am a boy'
tom_bob = tom + bob 
print( tom_bob ) 
last_name = 'Hong'
first_name = 'Gil-dong'
full_name = last_name + first_name
print( full_name )
#요구사항 홍길동의 글자갯수?
print( len( full_name )  )

laughing='ha' * 3
print( laughing )
line = '-' * 50
print( line )
str1 = "Good" #길이 글자갯수 4
str2 = "Morning" # 7
# 결과 11
print( len( str1 + str2 ) )
san = 'mountain'
num1 = san[-4] # t를 출력하기
print( num1 ) 
# it를 출력하기
num1 = san[-2] + san[-4]
print( num1 ) 
name='hong'
print( name ) 
name = 'kim'
print( name )
# name[2] = 's' (X)
a = 123
print( a ) # kis
san = 'mountain'
p = '-'
print( san[1:3],p,san[4:7],p,san[0],p,san[-2:] ) # ou-tai-m-in 