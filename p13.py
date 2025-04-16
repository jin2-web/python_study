# 튜플 만들기(생성)
# 1. ()
months = ('Jan', 'Feb', 'Dec')
days = ('Mon', 'Tue', 'Sun')
# months 튜플요소안에 'Jan'있나요? True
print( 'Jan' in months) 
# days 튜플에 '수' 추가할 수 없다.
# days.append( '수' ) 오류 발생
# days 튜플에서 'Mon' 삭제할 수 없다.
# days.remove('Mon') 오류 발생
# days[2] = 'Wed' 오류 발생

# 튜플은 수정, 삭제, 추가 안된다. 
# 튜플을 리스트로 고쳐서 리스트 수정, 삭제, 추가하고
# 다시 튜플로 고쳐요
days = ('Mon', 'Tue', 'Sun')
days_list = list( days )
print( type( days_list ) ) 
# 'Wed'추가하기
days_list.append('Wed')
# 'Mon'삭제하기
days_list.remove('Mon')
# 'Tue'를 'Thu' 바꾸기
days_list[1] = 'Thu'
print( days_list )
# 리스트 -> 튜플 고치기
days = tuple( days_list )
print( type(days) ) 

# 팁 1~50 리스트 
n_list = list( range(1,51,1) )
print( n_list ) 
# 10, 15, 20, ... 100 튜플을 만들기 
n_tuple = tuple( range( 10, 101, 5) )
print( n_tuple ) 


