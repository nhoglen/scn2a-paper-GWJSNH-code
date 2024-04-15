from datetime import datetime, date
from dateutil.tz import tzlocal

def get_time_from_video(thisvid):
    vidsplit = thisvid.split()
    timeinfo = vidsplit[1]
    timeinfostrip = timeinfo[0:-4]
    timepieces = timeinfostrip.split('-')
    timepiecesint = []
    for i in timepieces:
        timepiecesint.append(int(i))
    return timepiecesint

def get_date_from_block(thisdate):
    datepieces = []
    datepieces.append(int(thisdate[0:4]))
    datepieces.append(int(thisdate[4:6]))
    datepieces.append(int(thisdate[6:]))
    return datepieces

def generate_recording_dtobj(datestring,timestring):
    recdate = get_date_from_block(datestring)
    rectime = get_time_from_video(timestring)
    dtobj = datetime(recdate[0],recdate[1],recdate[2],rectime[0],rectime[1],rectime[2],0,tzlocal())
    return dtobj
