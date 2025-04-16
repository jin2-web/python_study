# ohlc = [["open", "high", "low", "close"], [100, 110, 70, 100], [200, 210, 180, 190], [300, 310, 300, 310]] 
# # 'close' 가격 출력하기
# for  i  in ohlc[1:]:
#     print( i[3] )
# # 0~90 8 
# list_0_90 = list( range( 0,  91, 8)  ) 
# list_0_9 = list( range(  10)) 
# print( list_0_90, '<===!!!!' )
# print( list_0_9)

# str ='abcde'

# for i in range( len(str) ):
#   i1 = i+1  
#   print(  f'{i1}번째 알파벳 {str[i] }' )
#   #print( i1 ,'번째 알파벳', str[i])

# #문제2
# n=  int(input("숫자는?"))
# f = 1
# for i in range( n, 0, -1):
#    f = f*i 
# print( f'{n}! = {f}' )  

mix_list = ['apple', 5, 'banana', 'grape', 3, 8, 6,'melon']
num_list = []
str_list = [] 
for i in range( len(mix_list) ) : 
  if( type(mix_list[i]) == str):
     str_list.append( mix_list[i] )
  elif( type(mix_list[i]) == int):  
     num_list.append( mix_list[i] )  
print( "숫자리스트 : ", num_list )
print( "문자리스트 : ", str_list )
# 결과 num_list에 [5,3,8,6], str_list에 ['apple','banana',]   
