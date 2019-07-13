import datetime

class Plant():
    def __init__(self, name, value, water, frequency, grow_time):
        self.NAME = name
        self.VALUE = value
        self.WATER = water
        self.FREQUENCY = frequency
        self.GROW_TIME = grow_time

        self.is_alive = True
        self.grow_up = False

        self.plant_time = datetime.datetime.today()

    def drink_water(seld, water):
        gprint("plant %s drinks %d of water" % (self.NAME, self.WATER))
        if water < self.WATER:
            gprint("plant %s DIES" % self.NAME)
            self.is_alive = False

    def update_status(self):
        if self.grow_up:
            return

        timedelta = datetime.datetime.today() - self.plant_time

        if timedelta.seconds > self.GROW_TIME:
            gprint("plant %s GROW UP" % self.NAME)
            self.grow_up = True
