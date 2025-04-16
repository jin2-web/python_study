class Car:
    speed = 0
    def upSpeed( self, value ) :
        self.speed = self.speed + value 
        print("현재 속도( 슈퍼클래스, 부모클래스 ) :%d"%self.speed) 
class Sedan( Car ) :
    def upSpeed( self, value ) :
        self.speed = self.speed + value + 20 
        print("현재 속도( 세단클래스  ) :%d"%self.speed) 
class Truck( Car ):
    def upSpeed( self, value ) :
        self.speed = self.speed + value - 20 
        print("현재 속도( 트럭클래스  ) :%d"%self.speed) 

mySedan = Sedan()       
myTruck = Truck()
myCar = Car()
mySedan.upSpeed(100)
myTruck.upSpeed(100) 
myCar.upSpeed( 100 )