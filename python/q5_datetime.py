# Hint:  use Google to find python function
from datetime import datetime as dt
####a) Use Python to compute the days between start and stop date
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date1=dt.strptime(date_start,'%m-%d-%Y')
date2=dt.strptime(date_stop,'%m-%d-%Y')
ndays1=(date2-date1).days

####b)  
date_start = '12312013'  
date_stop = '05282015'  
date1=dt.strptime(date_start,'%m%d%Y')
date2=dt.strptime(date_stop,'%m%d%Y')
ndays2=(date2-date1).days
####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  
date1=dt.strptime(date_start,'%d-%b-%Y')
date2=dt.strptime(date_stop,'%d-%b-%Y')
ndays3=(date2-date1).days