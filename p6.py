import random 
a = random.randint(0,3) # 0-앞면 1-뒷면
print("메뉴선택 프로그램")
if( a == 0 ):
    print("중국음식")
elif( a==1):
    print("한식")
elif( a==2):
    print("햄버거")
else:
    print("굶기")            

"""
word = input(" '내일'이라는 단어를 입력하기")
if( word =='tomorrow'):
    print('맞았습니다')
else:
    print('틀렸습니다')    



print("페이펄문구 계산")
pencil=int(input("연필갯수?"))
pen = int(input("펜갯수?"))
price=pencil * 1000 + pen * 2000
print("할인전금액 :" + str(price))
if( price >= 10000):
    sale = price * 0.1
    price = price - price*0.1
    print("할인금액 : " + str(sale) )
print("판매금액 :" + str(price))    


age = 10
if( age >= 6 and age<=12) :
    passenger_type="어린이"
    fare = 700
elif( age >= 13 and age<=18) :
    passenger_type="청소년"
    fare = 1100  
elif( age >= 19) :
    passenger_type="어른"
    fare = 1500  
print( passenger_type + "의 버스요금은 " + str(fare) + "원 입니다")


a = True
print( type(a) )
a=False
b=a
print( type(b) )
print(b, a) 
n = input('숫자입력하기')
flag = int(n) % 2 # 15 % 2 
print( flag == 1 ) 

p1 = int( input("상품가격은?") )
p2 = int( input("상품가격은?") )
p3 = int( input("상품가격은?") )
p4 = int( input("상품가격은?") )
sum = p1 + p2 + p3 +p4
if( sum >= 100000 ):
   print("상품권 수령하세요")
else:
   m = 100000 - sum 
   print(  str(m) +"원이 부족해서 상품권을 받을 수 없습니다.")
"""      