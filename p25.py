def dic_func( **para ): 
    print( para )  #{'심화반점수': [100, 75, 80]}
    
    for k in para.keys():
        sum = 0
        for score in para[k]:
           sum += score
        print( "%s --> %d" %(k,sum) )       
dic_func( 심화반점수=[100,75,80],
          기초반점수=[80, 90, 100, 50,80] )
