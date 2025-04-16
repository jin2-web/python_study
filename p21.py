#함수를 만든다 (생성한다, 정의한다)
def plus(v1, v2): # v1 가매개변수, 인수, 파라미터
   result = 0
   result = v1 + v2
   return result 

hap = plus( 10, 20 ) #함수호출   # 10 실매개변수 
print( hap )
hap = plus(300, -500)
print( hap )

# 숫자3개를 함수 보내서 큰수 리턴 받기
# 1단계 함수만들기 2단계 함수 호출 
# def max_fun( n1, n2, n3  ):
#    #...
#    return max_value

# max_v = max_fun( 10,8,90 )
# print(max_x)

# 문자 2개 함수로 보내서 길이의 합을 출력하는 함수 
def char_len_hap( s1, s2):
   return len(s1) + len(s2)

r = char_len_hap( 'abc', 'defg') #함수호출
print( r )
r = char_len_hap( 'student', 's')

# 숫자2개 문자1개를 함수로 보내서
# 숫자는 곱셈을 하고 문자는 연산자로 결과 반환받는 함수수
# 예1) 1,5, '*'  1*5를 리턴하기 
# 예2) 10, 5, '-' 10-5를 리턴하기
def calc_f( n1, n2, o1):
   if( o1 == '+'): 
      r = n1 + n2
   elif( o1 == '-'): 
      r = n1 - n2
   elif( o1 == '*'): 
      r = n1 * n2      
   elif( o1 == '/'): 
      r = n1 / n2 
   print( f'{n1} {o1} {n2} = {r}')

num1 = int(input('첫번째 수는?'))
num2 = int(input('두번째 수는?'))
op = input('연산자(+,-,*,/)는?')
calc_f( num1, num2, op)
