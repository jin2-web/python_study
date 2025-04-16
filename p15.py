set1 = { 3,0, 8, 1,2,3,1,1}
print( len( set1 ) ) # 3
print( set1 ) 
list1 = [ 3,0, 8, 1,2,3,1,1 ]
print( list1 ) # 입력해준 순서대로 출력된다
tuple1 = ( 3,0, 8, 1,2,3,1,1 )
print( tuple1)
set2={ '연필', '펜', '공책', '연필','펜'}
print(set2)
color_list=['red','blue','red','green','pink','blue','black']
print(color_list)
color_list = set(color_list)
print(color_list)
color_tuple=('red','blue','red','green','pink','blue','black')
color_set =set( color_tuple )
print( color_set )

# set 만들기
set3 = { 1,2,3,1,1 }
set4 = set( range(1,11,2) )
set5 = set( [1,2,3,1,1] )
set6 = set( (1,2,3,1,1) )

set7 = {0,1,2,3,4}
set8 = {3,4,5,6,7}
print( set7 & set8 ) # 교집합 and 공통원소 
print( set7 | set8 ) # 합집합 or 모든 원소
print( set7 - set8 ) # 차집합 0 1 2
s1 = {'red','yellow','green','blue'}
print('red' not in s1)
print('white' not in s1)
sawon = {'홍길동', '이수지', '박상민', '강민우', '하누리'}
perception = { '홍길동', '이수지', '박상민' } #지각
absenteeism = {  '박상민', '하누리' }
# 지각과 결근 둘 중 한번이라도 한 사람들의 set생성
pa = perception | absenteeism
bonus = sawon - pa
print( "보너스 받으실 사원명 " + str(bonus) ) # 강민우
overtime = perception & absenteeism #야근
print("야근하실 사원명은  " + str(overtime) )