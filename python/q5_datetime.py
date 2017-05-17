# Hint:  use Google to find python function
from datetime import datetime
####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'
d1 = datetime.strptime(date_start, "%m-%d-%Y")
d2 = datetime.strptime(date_stop, "%m-%d-%Y")

print(d1)
print(d2)
print (abs((d2-d1)).days)
# 937

####b)  
date_start = '12312013'  
date_stop = '05282015'  
d1 = datetime.strptime(date_start, "%m%d%Y")
d2 = datetime.strptime(date_stop, "%m%d%Y")

print(d1)
print(d2)
print (abs((d2-d1)).days)
#513


####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'
d1 = datetime.strptime(date_start, "%d-%b-%Y")
d2 = datetime.strptime(date_stop, "%d-%b-%Y")

print(d1)
print(d2)
print (abs((d2-d1)).days)
# 7850
