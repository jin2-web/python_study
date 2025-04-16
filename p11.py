cnt = 0
while(True):
    n=input("문자를 입력하세요")
    if( n == 'x' or n=='X'):
        print("프로그램종료")
        break
    else: 
        print(n)
        cnt = cnt + 1
print( "입력하신 문자는 " + str(cnt) + "개 입니다")
# sum = 0
# i = 0
# while( sum <= 20 ) :
#     i += 1    # i=i+1
#     sum += i  # sum = sum + i
# print( i )
# print( sum )

# while(True):
#     n = int(input("enter the number"))
#     if( n==0 ):
#         print("EXIT")
#         break #반복문 밖으로 가기
#     elif( n%2 == 0 ):
#         print(n, 'is even number')
#     else:
#         print(n, 'is odd number')    
# print("반복문끝")

# omlet = ['egg','meat','onion','carrot']
# #원소갯수
# n = len( omlet )
# print("원소갯수 :" + str(n) )
# for i in range(0, n, 1) :
#    print( omlet[i] )

# 1~10까지 합을 구하기
# 2,4,6,8,10까지 합을 구하기    
# 1~20까지 홀수의 합 구하기
# for i in range(0,5):       #0 1 2 3 4
#   print('*' * (5-i) )      #5 4 3 2 1  
# a=1
# while (a <= 10): 
#    print(a)
#    a = a+1
# print("반복문끝")   
# count = 1
# while( count <= 5) :
#    print(count)
#    count += 1 # count = count + 1

# n = int(input('숫자를 입력하세요 ')) # 3
# step = 0
# sum = 0
# while( step <= n ) : # 0 <= 3, 1 <= 3, 2 <= 3  
#      sum += step # sum = sum + step
#      step += 1  # step = step + 1
# print(sum)