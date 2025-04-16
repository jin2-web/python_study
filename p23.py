g_var = '홍길동'
def func():
    result = 100 #지역변수수
    return result
def func2():
    result = 200
    print(result, g_var, point)     
def func3( ):
    global point #global 예약어 사용 지역변수 -> 전역변수 
    point=100
    r = 10
    r1 = 20
    r_list = [r,r1]
    print(r_list, g_var)
    return r_list
# 함수에 2개 값을 반환하게 하기 (X)
# 함수에서 return(반환)은 한개만 가능하다
def  func4(n1, n2=50) : #매개변수, 인수, 파라미터터
     result = n1+n2
     print(n1, n2, '<==func4')
     return result
def func4( s1, s2, s3, s4 ):
    return s1 + s2 

def func4(n1,n2,n3):
    result = n1 + n2 + n3
    return  result 

print( func4( 'a','b','c','d' ) ) 

func3()

print( func() ) 
hap = func()
print( hap )
func2()
