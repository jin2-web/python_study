mugu = {'연필':200, '펜':800, '지우개':500, '자':300}
mugu_keys = list( mugu.keys() )
mugu_vals = []
for mugu_key in mugu_keys :
     mugu_vals.append( mugu[ mugu_key ]  )
print( mugu_vals )  
mugu_values_list = list( mugu.values() ) 
print( mugu_values_list ) 
mugu_values_tuple = tuple( mugu.values() ) 
print( mugu_values_tuple ) 
mugu_values_set = set( mugu.values() ) 
print( mugu_values_set )  

#문제4
d1 = {'배':[2000,3], '사과':[1500,4], '딸기':[1800,1], '참외':[2300,5], '수박':[15000, 3]}
total = 0
#키값들을 리스트로 만드세요
d1_keys_list = list( d1.keys() ) #['배','사과'...]
total = 0
for key in d1_keys_list :
     if(5-d1[key][1] != 0):
        print( key, 5-d1[key][1], (5-d1[key][1]) * d1[key][0] )
        total += (5-d1[key][1]) * d1[key][0]
print( "총비용은", total )        
inventory = {'메로나':(300,2), '비비빅':(400,3),'죠스바':(250,100)}

"""
if( d1['배'][1] <= 5 ):
     p1 = 5-d1['배'][1]
     price1 = p1 * d1['배'][0]
     total = total + price1
if( d1['사과'][1] <= 5 ):
     p2 = 5-d1['사과'][1]
     price2 = p2 * d1['사과'][0]
     total = total + price2
if( d1['딸기'][1] <= 5 ):
     p3 = 5-d1['딸기'][1] 
     price3 = p3 * d1['딸기'][0]
     total = total + price3
if( d1['참외'][1] <= 5 ):
     p4 = 5-d1['참외'][1] 
     price4 = p4 * d1['참외'][0]  
     total = total + price4 
if( p1 != 0 ):
     print( '배', p1 , '개' , price1, '원' )
if( p2 != 0 ):
     print( '사과', p2 , '개' , price2, '원' )
if( p3 != 0 ):
     print( '딸기', p3 , '개' , price3, '원' )
if( p4 != 0 ):
     print( '참외', p4 , '개' , price4, '원' )               
print("총 비용 ", total )
"""
