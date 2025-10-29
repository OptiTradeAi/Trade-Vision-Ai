import datetime as dt
def next_m5_open(now=None):

    now = now or dt.datetime.utcnow()
    minute = (now.minute//5)*5
    this_open = now.replace(minute=minute, second=0, microsecond=0)
    nxt = this_open + dt.timedelta(minutes=5)
    ttn = int((nxt - now).total_seconds())
    return nxt, ttn
