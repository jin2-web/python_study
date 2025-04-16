price = { '오뎅': '2000원', '떡뽁이':'3000원' }
print( price['오뎅'] ) # 2000원
print( price['떡뽁이']) 
L = [20,40,60,80,100] 
T = ( 2,4,6,8,10)
lt = { } 
for i in range(0,5,1):
    lt[ T[i] ] = L[i]
print( lt )     

eng = ['apple', 'banana','orage']
kor = ( '사과', '바나나', '오렌지')
#사과: apple, 바나나 : banana, 오렌지:orage 
dic3 = {} 
for i in range(  len(eng) ) :
    dic3[ eng[i] ] =  kor[i] 
print( dic3 ) 

D = {'spring':'봄',  'summer':'여름',  'fall':'가을',  'winter':'겨울'}
print( D )
print( D['spring'])  #키가 아닌 값을 입력하면 에러

number = {1:'one',  2:'two',  3:'three',  4:'four',  5:'five' }
print(number)
print(number[2])
#키값들만 리스트로 만들기
keys_list = number.keys()
print( keys_list )

food = {'분식':['떡볶이','호떡'], '중식':['짜장면','탕수육']}
print(food['분식'][1])
del food['중식']
print(food)

# 딕셔너리 만들기
d1  = { 'k1': 70, 'k2': 70 }
print( d1['k1'] ) 
d2 = { 100: ['a','b','c'], 200:(True, False) }
print( d2[100][2] ) 
# 딕셔너리 추가하기
#예) d1에 'k3':85
d1[ 'k3'] = 85
#예) d2에 300:'kbs'
d2[ 300 ] = 'kbs'
# 딕셔너리의 원소를 삭제하기 
# 예) 'k2': 70 삭제하기
del d1['k2'] 

# list, tuple 딕셔너리
value_list1 = [ 100,25,83,94 ]
key_tuple = ('김','박','이','최') 
# {'김':100, '박':25,'이':83, '최':94 }
#문제1
menu_list = ('Americano', 'Cafe latte', 'Green Tea latte', 'Mocha latte' )
price_list = [2000,2500,3000,3500]
coffee_shop={}
for i in range( 0, len(menu_list), 1) :
    coffee_shop[ menu_list[i] ] = price_list[i]
print( coffee_shop )
order = input("메뉴를 주문하세요? ")
if( order in coffee_shop.keys() ):
    print("주문하신 " + order + "는 " )
    print( coffee_shop[order] )
else:
    print("주문하신 " + order + " 없습니다")