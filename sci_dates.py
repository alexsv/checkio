import datetime
from datetime import date

def checkio(from_date, to_date):
    days = (to_date - from_date).days + 1
    full_weeks = days / 7
    result = full_weeks * 2
    days -= full_weeks * 7
    while days > 0:
        if days + from_date.weekday() in [6,7]:
            result += 1
        days -= 1
        
    return result

if __name__ == "__main__":
    print 'result=%s' % checkio(date(2013, 1, 5), date(2013, 1, 10))
