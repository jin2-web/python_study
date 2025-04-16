def calc_f():
  global n3 #지역변수를 전역변수로 바꾸기기 
  n3=100
  global n5
  n5=200
  print( f'{n1} {o1} {n2} {n3} {n5}' )

n1=10
n2=20
o1='+'

calc_f()
print(n3)
print(n5)


