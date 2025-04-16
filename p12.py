# 1~30출력하기
# for i in range(1,31,1):
#     print(i, end=" ")
# 문방구 상품리스트 '펜','지우개개','샤프','자'
# 사고 싶은 상품은? 마우스
# 마우스는 없어요.
# 사고 싶은 상품은? 지우개
# 지우개 여기 있습니다.
# print()
# shop_list = ['펜','지우개','샤프','자'] 
# while( True ):
#   buy = input('사고 싶은 상품은?(종료 no)')
#   if( buy  in  shop_list ):
#      print( buy + " 여기 있습니다")
#   elif( buy == 'no'):
#      break
#   else:
#      print( buy + "는(가) 없습니다")

# student_list = ['구윤서', '함선아','박민수', '선상준']
# 학생이름(종료 exit)? 홍길동
# 홍길동은 학생명단에 없습니다
# 학생이름(종료 exit)? 함선아
# 함선아씨는 우리반 학생입니다
# 학생이름(종료 exit)? exit
# 오늘도 수고 많이 하셨습니다. 우리반은 4명입니다
# print()
# while( True ):
#   name = input('학생이름은?(종료 exit)')
#   if( name  in  student_list ):
#      print( name + " 우리반 학생입니다다")
#   elif( name == 'exit'):
#      print( '오늘도 수고 많이 하셨습니다. 우리반은 ' + str(len( student_list )) + '명입니다')
#      break
#   else:
#      print( buy + "는(가) 없습니다")

# 반찬가게 관리 프로그램
food_list = ['김치','멸치볶음']
while(True):
   print()
   print( '1.추가 2. 삭제 3. 전체목록 9. 종료')
   menu = int(input('메뉴를 선택하기 '))
   if( menu == 1) :
      food_append=input('추가하고 싶은 반찬종류는? ')
      if( food_append not in  food_list):
         food_list.append( food_append  )
      else: 
         print("이미 목록있는 반찬입니다")   
   elif( menu == 2 ):
      food_remove = input('삭제하려는 반찬명은?')
      if( food_remove in food_list ):
         food_list.remove( food_remove )
      else:
         print( food_remove + " 반찬은 목록에 없어요")   
   elif( menu == 3) :
      for food in food_list :
         print( food, end=" ")
   elif( menu == 9 ) :
      break      

#리스트 원소를 추가하기 append
#리스트 원소를 삭제하기 리스트명.remove(리스트원소값)   
#리스트 원소를 삭제하기 del 리스트명[인덱스번호호]
# a_list = [1,2,3]
# a_list.remove( 3 )
# del  a_list[0]  
# print( a_list )

# b_list = ['사과','배','복숭아']
# b_list.remove('복숭아') #복숭아를 삭제하기기
# del b_list[0] #0인덱스를 삭제하기
# print( b_list )