m_ex={ '달러':1167, '엔':1.096, '유로':1268, '위안':171}
keys_list = list(m_ex.keys())
while( True ) :
    a=input("환전할 금액과 단위입력(예: 100 달러)")
    money, unit = a.split(' ')
    print( money, unit  )
    money = int(money)
    if( unit == '종료'):
        break
    for key in keys_list:
        if( key == unit ):
            print( money * m_ex[ key ], '원')