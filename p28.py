import math
r = 5
area  = math.pow( r, 2) * math.pi
print( area ) 

import random
rint = random.randint(1, 100)
print( rint )
# 2025-04-14
import time
string = time.localtime( time.time() )
st = time.strftime("%Y-%m-%d", string)
print( st )

import datetime
today = datetime.datetime.today()
stm = today.strftime( "%Y-%m-%d" )
print( stm )