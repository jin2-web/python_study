int_num_a = [0,1,2,3]
int_num_b = [2,3,4,5,6]
int_num_ab = int_num_a + int_num_b
print( int_num_ab )
int_num_a3 = int_num_a * 3
print(int_num_a3) 

list_odd=[1,3,5,7,9]
list_even=[2,4,6,8,10]
print( list_odd[-3] ) 
print( list_odd[2])
print( list_even[1+3]) #10
# [1,3,5,7,9,2,4,6,8,10]
print( list_odd + list_even) 
# [1,3,5,7,9,1,3,5,7,9]
print( list_odd * 2 )
print( list_odd[ 0:3 ] ) # 0,1,2 인덱스값 
print( list_even[:]) 
print(list_odd[3:]) 
print(list_even[:2]) 
spell = ['h','a','n','d','i','c','r','a','f','t']
print( spell[1:5] ) # andi
print( spell[:]) # 전부다 
print( spell[:4]) # hand
print(spell[5:])
print( spell[:2] + spell[9:])
list_name = ['e','a','q','f','d','1', 'A','P']
list_name.sort()
print( list_name )
list_num = [10, -20, 55, 200, 0]
list_num.sort() #숫자 오름차순으로 정렬
print( list_num )

score = []
a = int(input( "점수?"))
score.append( a )
a = int(input( "점수?"))
score.append( a )
a = int(input( "점수?"))
score.append( a )
a = int(input( "점수?"))
score.append( a )
a = int(input( "점수?"))
score.append( a )
print( score )
#sum = score[0] + score[1] + score[2] + score[3] + score[4]
sum_value = sum(score)
print( sum_value)
