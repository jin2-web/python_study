driver_speed=110 #속도
lane_change_frequency=2 #차선변경빈도
braking_intensity=1 #급제동 1, 0(X)
acceleration = 40 #가속도강도
smartphone_usage=0 #스마트폰 사용여부 1, 0(X)
# 차선변경빈도 3회 이상이면 "나쁜 운전습관"
if( lane_change_frequency >= 3 ):
      print("나쁜 운전습관")      
# 스마트폰 사용하면 "나쁜 운전습관"
if( smartphone_usage == 1 ):
      print("나쁜 운전습관") 
# 급제동하면 "나쁜 운전습관"
if( braking_intensity == 1 ):
      print("나쁜 운전습관") 

# 차선변경빈도 3회 이상이면 "나쁜 운전습관"
if( lane_change_frequency >= 3 and smartphone_usage == 1 and braking_intensity == 1):
      print("아주 나쁜 운전습관")      
if( lane_change_frequency >= 3 or smartphone_usage == 1 or braking_intensity == 1):
      print("조심 운전해야할 사람람")      

# 속도 0~50 저속주행 
# 51~75  보통주행 76~100 고속주행 
# 101이상이면 과속주행
if( driver_speed >= 0 and driver_speed <= 50) :
      print("저속주행")
elif( driver_speed >= 51 and driver_speed <= 75):
      print("보통주행")
elif( driver_speed >= 76 and driver_speed <= 100):
      print("고속주행")
else:
      print("과속주행")



