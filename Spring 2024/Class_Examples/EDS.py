from datascience import *
import time                # Python time functions
from time import strptime 
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import matplotlib.dates as mdates
from matplotlib import ticker
import numpy as np
def Tdate(date_string):
    return time.mktime(strptime(date_string, '%m/%d/%Y'))
def FilterTdate(tbl,d1,d2,datec=0,fmtdate='%m/%d/%Y'):
    mkd1=Tdate(d1)
    mkd2=Tdate(d2)
    print("Filtering Table dates between",d1,d2)
    if type(tbl[datec][0])!= np.float64:
        tbl.set_format(datec, DateFormatter(format='%Y-%m-%d',))    
    tbl_out = tbl.where(datec,are.between(mkd1,mkd2))
    return tbl_out    
def ptrend(tbl,datec,datac,fmtdate="%b-%Y"):
    """  Takes Datascience Table and plots time trend, returns number of days """
    # Input Data to plot
    datetrend = tbl.column(datec).astype("datetime64[s]")  # Need to convert to a datetime64[s] object
    data = tbl.column(datac)
    loc = mdates.AutoDateLocator()  # Fancy function for dates
    fmt = mdates.AutoDateFormatter(loc)
    plt.gca().xaxis.set_major_formatter(fmt)
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(fmtdate))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter(fmtdate))
    plt.gca().tick_params(axis="x", which="minor", direction="out", top=True)
    plt.plot(datetrend, data,label=datac)
    plt.legend(loc='center left', bbox_to_anchor=(1.1, 0.5), labelspacing=3)  
    plt.gcf().autofmt_xdate()
    days= (datetrend.max()-datetrend.min()).astype('timedelta64[D]')/np.timedelta64(1, 'D')
    return days