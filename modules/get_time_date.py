import datetime
import dateutil.relativedelta
    
def get_time_date():
    now = datetime.datetime.now()
    get_date = now.strftime("%Y-%m-%d")
    return get_date

def get_system_time():
    now = datetime.datetime.now()
    get_time = now.strftime("%H-%M-%S")
    return get_time

def get_last_month(week):
    now = datetime.datetime.now()
    last_month = now + dateutil.relativedelta.relativedelta(weeks=-int(week))
    last_month = last_month.strftime("%Y-%m-%d")
    return last_month 

    