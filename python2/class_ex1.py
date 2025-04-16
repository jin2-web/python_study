# class_ex1.py
# 클래스에서 생성자의 가매개변수의 갯수를 유동적으로로 하려면
#  *매개변수 - 튜플형식으로 저장됨 
#  **매개변수 - 딕셔너리형식으로 저장됨 
class Car:
    #멤버필드
    color =""
    price = 0
    speed = 0
    # 생성자 :객체생성 Car() 할때 자동으로 호출된 곳곳
    def __init__( self, *v1):
        for i in range( len(v1) ) :
           if( i==0):
              self.color = v1[0]
           if (i==1):
              self.price = v1[1]
           if (i==2) :
              self.speed = v1[2]
myCar =Car( "빨강", 1000, 30  )
print(myCar.color, myCar.price, myCar.speed) 
myCar2 =Car( "파랑", 2000  )
print(myCar2.color, myCar2.price, myCar2.speed) 
myCar3 =Car( "노랑"  )
print(myCar3.color, myCar3.price, myCar3.speed) 