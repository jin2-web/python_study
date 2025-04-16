# Module2.py파일안에 m3함수 입니다
# Module1.py의 func3()이 호출됨
# import Module1  Module1의 파일안에 있는 모든 함수 가져오기 
# import Module2
# from 모듈_파일명 import 함수명1 - 설명 : 모듈에서 해당 함수만 가져오기
from Module1 import func3
from Module2 import * # 모든 함수 
import sys #표준모듈
print(sys.builtin_module_names)
import math
print( math.log(10))
list_1 = [10,50,77,90]
print( math.fsum( list_1 ) )
a = 3
#거듭제곱
print( math.pow(5, 3))
print( math.pi ) 
import time
utc = time.time()  
#UTC 표준 시를 기준으로 한 현재시간 구함, 타임 스탬프 시간
# 1970년 1월 1일 0분 0초부터 현재까지의 초 값을 실수 
gm = time.gmtime(utc) 
#GMT 기준 시간 보이기기
print(gm)
tm = time.localtime( utc )
print(tm) 

# 현재 날짜 시간 출력하기
import time
tm  = time.localtime( time.time() )
print("현재년도 ", tm.tm_year )
print("현재 월 : " , tm.tm_mon )
print("현재 일 : " , tm.tm_mday )
print("현재 시 : " , tm.tm_hour)
print("현재 분 :", tm.tm_min)
print("현재 초 :", tm.tm_sec) 

string = time.ctime( time.time() )
print( string ) # Mon Apr 14 11:26:28 2025

tm = time.localtime( time.time() )
string = time.strftime( "%Y-%m-%d %I:%M:%S %p", tm)
# 2025-04-14 11:33:09 AM
print( string )

import datetime
today = datetime.date.today()
print( today )  # 2025-04-14

from datetime import datetime  as dt
# from 패키지명 import 모듈명 
# 패키지안에 있은 모듈을 import하기 
# 사용은 모듈명.함수명()   

now = dt.now() #현재의 날짜와 시간 
# AttributeError: module 'datetime' has no attribute 'now'
print( now ) # 2025-04-14 11:39:52.450871

today = dt.today()
print(today)   

# func3()
# m3()
# m2()
# m1()
# m4()

import random 
from tkinter.simpledialog import * 

