import random 

numlist = [ 5,9,30,1 ]
print( len( numlist) )
ss_list = [12, 'aa', [3,2], "1"]
print(  ss_list[2][0] )

list_ex1 = ['View','the', 'latest', 'news', 'and']
list_ex2 = ['breaking', 'news', 'today']
list_ex3 = ['for', 'world', 'weather', 'entertainment']
list_ex4 = ['politics', 'and', 'health']
list_5 = [] 
if( len(list_ex1[0] ) >=5 ):
    list_5.append( list_ex1[0] ) 
if( len(list_ex1[1] ) >=5 ):
    list_5.append( list_ex1[1] )     
if( len(list_ex1[2] ) >=5 ):
    list_5.append( list_ex1[2] ) 
if( len(list_ex1[3] ) >=5 ):
    list_5.append( list_ex1[3] )  
if( len(list_ex1[4] ) >=5 ):
    list_5.append( list_ex1[4] ) 
if( len(list_ex2[0] ) >=5 ):
    list_5.append( list_ex2[0] )
if( len(list_ex2[1] ) >=5 ):
    list_5.append( list_ex2[1] )     
if( len(list_ex2[2] ) >=5 ):
    list_5.append( list_ex2[2] )
if( len(list_ex3[0] ) >=5 ):
    list_5.append( list_ex3[0] ) 
if( len(list_ex3[1] ) >=5 ):
    list_5.append( list_ex3[1] )     
if( len(list_ex3[2] ) >=5 ):
    list_5.append( list_ex3[2] )                      
if( len(list_ex3[3] ) >=5 ):
    list_5.append( list_ex3[3] ) 
if( len(list_ex4[0] ) >=5 ):
    list_5.append( list_ex4[0] ) 
if( len(list_ex4[1] ) >=5 ):
    list_5.append( list_ex4[1] )      
if( len(list_ex4[2] ) >=5 ):
    list_5.append( list_ex4[2] )     
list_5.append("news")

print( list_5 ) 

