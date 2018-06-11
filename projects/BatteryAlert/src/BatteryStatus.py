from Bsettings import Bpath
from Bsettings import SetLevel
from Config import Config
import logging
import os
import psutil


class Battery(Config):
    """
        Module to fetch battery status
    """

    def __init__(self):
        if not os.access(Bpath.POWER_SUPPLY_PATH, os.R_OK):
            raise RuntimeError("Unable to read {path}.\
                ".format(path=Bpath.POWER_SUPPLY_PATH))
        else:
            logging.debug("All ok!")
            self.charging = False

   
    def secs2hours(secs):
        mm, ss = divmod(secs,60)
	hh,mm  = divmod(mm,60)
	return "%d:%02d:%02d" % (hh,mm,ss)

    def get_power_level():
        battery= psutil.sensors_battery();
        battery
    
    def get_low_battery_warning_level(self):
        power_percent=battery.percent
        if power_percent < POWER_LOW_PERCENT_LIMIT
            alert = true

        elif power_percent > POWER_SAFE_PERCENT_LIMIT
            alert = false

        return alert
