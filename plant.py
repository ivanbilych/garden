import datetime
import json

from mgprint import gprint

class Plant():
    def __init__(self, name, value, water, frequency, grow_time):
        self.NAME = name
        self.VALUE = value
        self.WATER = water
        self.FREQUENCY = frequency
        self.GROW_TIME = grow_time
        self.REQUIRED_WATER = water/frequency

        self.is_alive = True
        self.grow_up = False

        self.plant_time = datetime.datetime.today()

    def drink_water(self, water):
        gprint("plant %s drinks %d of water" % (self.NAME, water))
        if water < self.REQUIRED_WATER:
            gprint("plant %s DIES" % self.NAME)
            self.is_alive = False

    def update_status(self):
        gprint("plant %s: ALIVE - %s, GROW UP - %s" % (self.NAME, self.is_alive, self.grow_up))
        if self.grow_up or not self.is_alive:
            return

        timedelta = datetime.datetime.today() - self.plant_time

        if timedelta.seconds > self.GROW_TIME:
            gprint("plant %s GROW UP" % self.NAME)
            self.grow_up = True

def json_to_plant(json_pkg):
    return Plant(json_pkg["name"], json_pkg["value"], json_pkg["water"], json_pkg["frequency"], json_pkg["grow_time"])
