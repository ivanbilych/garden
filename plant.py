import datetime

from mgprint import gprint

class Plant():
    def __init__(self, name, value, water, frequency, grow_time):
        self.NAME = name
        self.VALUE = value
        self.WATER = float(water)
        self.FREQUENCY = frequency
        self.GROW_TIME = grow_time
        self.REQUIRED_WATER = float(water/frequency)

        self.is_alive = True
        self.grow_up = False

        self.plant_time = datetime.datetime.today()

    def drink_water(self, water):
        gprint("  [%10s] drinks %.2f of water (required %.2f)" % (self.NAME, water, self.REQUIRED_WATER))
        if water < self.REQUIRED_WATER:
            gprint("  [%s] DIES" % self.NAME)
            self.is_alive = False

    def update_status(self):
        gprint("  [%10s] ALIVE: %s, GROW UP: %s" % (self.NAME, self.is_alive, self.grow_up))
        if self.grow_up or not self.is_alive:
            return

        timedelta = datetime.datetime.today() - self.plant_time

        if timedelta.seconds > self.GROW_TIME:
            gprint("  [%10s] GROW UP" % self.NAME)
            self.grow_up = True

def json_to_plant(json_pkg):
    return Plant(json_pkg["name"], json_pkg["value"], json_pkg["water"], json_pkg["frequency"], json_pkg["grow_time"])
