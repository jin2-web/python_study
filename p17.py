#list자료형 - 쓰기 전용이다다
menu_list = [ '아메리카노', '카프치노']
m = list( '김' )
#tuple자료형 - 읽기 전용이다
menu_tuple = ( '아메리카노', '카프치노' )
a_tuple = (1,)
ma = tuple( range(0,10,1) )
print( ma ) 
#dictionary - 사전 
d1={ '김':30, '이':20 }
print( d1['김'] )
#set - 집합 합집합 | 교집합 & 차집합 -
set1 = { 1,2,3,4 }
set2 = {3,4,5,6}
print( set1 - set2 )
d1 = {'a':[100, 150], 'b':(10,30), 'a':'홍길동' }
# 150 출력하기
print( d1['a'] ) 
# d1에 'c' : {1,2,3,1,2} 추가하기
d1['c'] = {1,2,3,1,2} 
print( d1 )
# d1에 'a':'홍길동'삭제하기
del d1['a']
print( d1 )
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update( new_product ) 
print( icecream )

a = [ 10,20,30,40,50 ]
b = ('a','b','c','d','e')
# {'a':10, 'b':20, 'c':30, 'd':40, 'e':50 }
# 방법1
dic_ab = {}
for  i in range( len(a) ): # 0 1 2 3 4
  dic_ab[  b[i] ] = a[i]
print( dic_ab )   
# 방법2
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
r = dict( zip( keys, vals ) )
print( r )

dic_ab = dict( zip( b, a) )
print( dic_ab )

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
# 알고 싶은 날짜는? 09/06
# 종가는 10300원 입니다. 
# 알고 싶은 날짜는? 10/06 
# 데이터가 없습니다. 
# 알고 싶은 날짜는? 99/99 
# 프로그램 종료합니다
while( True ) :
  in_date = input('알고 싶은 날짜는? ') # '09/06'
  if( in_date in close_table.keys() ):
    print("종가는 ", close_table[ in_date ], '원 입니다' )
  elif( in_date == '99/99'):
    print("프로그램종료")
    break 
  else :
    print("데이터가 없습니다") 