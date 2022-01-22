#program kalender

import calendar

def kalender(yy,mm):
    kalender = calendar.month(yy, mm)
    return kalender

print(kalender(2022,1))