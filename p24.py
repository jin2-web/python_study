def para_func( *para ): # ( ( 10,-20, 50, 80,200,-30 ), )
    result = 0 #지역변수
    #print( para, '<== para' )
    max = -99999999 
    min = 999999999
    for p in para: #p값 ( 10,-20, 50, 80,200,-30 )
        for num in p:#num값 10
            if( min > num ):
                min = num
            # if( max < num):
            #     max = num
    return min

hap = 0 #전역변수
a = tuple(range( 1,101,1) )
a_data = ( 10,-20, 50, 80,200,-30 )
min=para_func( a_data ) #함수호출
print(min)
#가장 큰수 200출력하기 
