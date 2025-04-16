# class_ex3.py
class Dog:
     c_var = "클래스변수"
     c_i_var = 100

     def __init__(self):
          self.in_var = "인스턴스 변수 "
          self.in_i = 200
myDog = Dog()          
print( myDog.c_var, myDog.c_i_var, myDog.in_var, myDog.in_i  ) 
print( Dog.c_var, Dog.c_i_var ) # 클래스안에 멤버 변수 출력
print( myDog.in_var, myDog.in_i ) #생성자안에 변수 출력 
#인스턴스 변수는 __init__ 생성자 선언 한 변수이다
# 사용하려면 반드시 객체생성(예 : myDog = Dog() ) 해야 한다. 
# 사용하는 방법 myDog.in_var 
# 용도 : 필요시에만 사용한다.
#클래스 변수는 class  밑에 써주는 변수명 
#  컴파일단계에서 스택 메모리에 올라간다.   
#  소멸은 프로그램종료할때 
#용도 : 프로그램 처음부터 끝까지 변수가 유지 되어야 할때 
#방법 : Dog.c_var  