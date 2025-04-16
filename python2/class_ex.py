# class_ex.py
# 1단계 설계한다
class  Car :
    # 필드 : 클래스 안에 선언한 변수 
    # 멤버 필드 
    color = ""
    speed = 0
    # method 메소드 : 클래스 안에 선언한 함수
    def upSpeed( self, value ) : # self 자기자신, 멤버 
        self.speed = self.speed + value 
    def downSpeed( self, value ) :
        self.speed = self.speed - value  
    def __init__(self,v1="흰색",v2=5): #생성자 
        # 생성자의 용도 : 객체생성하면 기본값을 셋팅할 때때
        self.color=v1
        self.speed =v2

# 2단계 인스턴스(객체)화 , 객체를 생성한다., 객체생성
myCar = Car() 
print( myCar.color ) 
print( myCar.speed ) 
myCar2 = Car('빨강', 30)
print( myCar2.color ) 
print( myCar2.speed ) 

myCar3 = Car('흰색', 50)
print( myCar3.color ) 
print( myCar3.speed ) 

myCar4 = Car('노랑색')
print( myCar4.color ) 
print( myCar4.speed ) 