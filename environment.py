weather_condition = "맑음"  #날씨
temperature = 25 #온도
humidity = 0.5 #습도
wind_speed = 20 #바람의 속도
temperature_variation = 10.2 #기온차이
visibility = 3 #날씨에 따른 시야 거리(시정)
forecast = "눈" #기상청 예보
print( temperature)
print( weather_condition )
print( humidity)
print( wind_speed )
print( temperature_variation)
print( visibility)
print(forecast)

if( humidity >= 0.7 ):
    print("위험해요")
else:
    print("안전해요")    
if( wind_speed >= 50 ):
    print("위험해요")
else:
    print("안전해요")
if(forecast == "비" ):
    print("우산이 필요해요")
else:
    print("우산이 필요없습니다")            