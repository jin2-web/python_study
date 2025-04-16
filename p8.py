list1 = [10,20, 'red', 12.43]
list2 = [] #빈리스트트
list3 = ['a', [ 1,2,3,['c','b']  ] ]
print( list1 ) 
print( list2 )
print( list3[1][3][0] )
list4 = [ 100,[ True, False ],200,300 ]
print( list4[1][1] )
a=[1,2,3,4]
# 4 3 2 1 출력하기
print( a[3], a[2], a[1], a[0])
print( a[-1], a[-2], a[-3], a[-4])
list_ex=[5,9,30,1,714,3776,9614]
high = 6
low = 3
print( list_ex[3+2] )
print( list_ex[ high - low ])
# print( list_ex[2 * 2.5])  # 오류: 실수형형
print( list_ex[ 5%4])
numlist = [0,10,20,30,40,50,60,70,80,90]
temp = 3
print( numlist[ temp*3] ) #90
print( numlist[ temp%2] ) #10
print( numlist[ temp+5] ) #80 
print( 10 in numlist) 
#numlist안에 요소가 10이 있느냐? 
print( 15 not in numlist) 
#numlist안에 요소가 15가 없느냐? 
names = ['김길수','최명희','박미자','김희영']
name = input("찾고 싶은 사람은?")
if( name in names ):
    print( name + "파이썬 반입니다")
else:
    print( name + "파이썬 반이 아닙니다.") 
fruit_list = [ '사과','귤','포도','망고', '바나나' ]      
price_list = [ 10000, 5000, 15000, 20000, 3000 ]
fruit = input("사고 싶은 과일은?")
if( fruit in fruit_list) :
    print("구매해 주셔서 감사합니다")
    if( fruit_list[0] == fruit) :
       print( "금액은 " + str(price_list[0]) + "원")
    elif( fruit_list[1] == fruit) :
       print( "금액은 " + str(price_list[1]) + "원")
    elif( fruit_list[2] == fruit) :
       print( "금액은 " + str(price_list[2]) + "원")
    elif( fruit_list[3] == fruit) :
       print( "금액은 " + str(price_list[3]) + "원")
    else:   
       print( "금액은 " + str(price_list[4]) + "원")   
else:
    print( fruit+"는 팔지 않습니다")    