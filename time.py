# Lucien Lo <khl.lucien@gmail.com>

from datetime import datetime

class Timer(object):
    def __init__(self):
        self.dateDivider = "-"
        self.timeDivider = "-"

    def makeTimeLabel(self):
        timeNow = datetime.now(tz=None)
        return timeNow.strftime(self.dateDivider.join(["%y","%m","%d"])+"_"+self.timeDivider.join(["%H","%M","%S"]))

    def makeDayLabel(self):
        timeNow = datetime.now(tz=None)
        return timeNow.strftime(self.dateDivider.join(["%y","%m","%d"]))
