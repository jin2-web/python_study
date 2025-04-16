name = input('이름은?')
score = input('점수는?')
hakjum = input('학점은?')
# 자료형을 보기 type
print( type( score ) )
# 자료형을 str에서 int 바꾸기
score = int( score ) # int("60") 60 
print( type( score ) )

if( score >= 90):
    grade='A'
elif( score >= 80 ) :
    grade = 'B'
elif( score >= 70) :
    grade ='C'
elif( score >= 60):
    grade = 'D'
else:
    grade = 'F'                
print( name + '씨는 점수 ' + str(score) + '점은 ' + grade + '홍홍이고 ' + hakjum + '학점 입니다.' )
