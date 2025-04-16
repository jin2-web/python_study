t = ()
t_1 = (1, )
print( type(t_1) )
numbers=tuple( range(10) )
print( numbers ) 
tuple_t = tuple( range(10, 71, 10))
# 10 + 30 + 50 
sum=tuple_t[0] + tuple_t[2] + tuple_t[4]
print( sum )
# 사용(접근) 가능 수정 안됨 - 읽기전용
#( 1,2,3...10, 1,2,3,...10, 1,2,3...10)
# 1단계 (1,2,...10)
a = (1,2,3,4,5,6,7,8,9,10)
a_1 = tuple( range(1, 11, 1) ) 
# 2단계  1단계 3번 반복하기 
a = a * 3
a_1 = a_1 * 3
# 3단계 출력하기
print( a )
print( a_1 )
a = a + a_1
print( a )
print( a[0:3])
print( a[:5])
print( a[10:])

str_red = 'RED'
list_color = ['Red','Yellow','Orange']
str_red_tuple = tuple( str_red )
list_color_tuple = tuple( list_color )
print( str_red_tuple ) #('R', 'E', 'D')
print( list_color_tuple )  #('Red', 'Yellow', 'Orange')
# ('Y','e','l','l','o','w')
print( list_color_tuple[1] )
aa = tuple( list_color_tuple[1] )
print( aa )

