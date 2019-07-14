from mgprint import gprint

class GrowPlace():
    def __init__(self, plant):
        self.plant = plant
        self.water = 0.0

    def add_water(self, water_in):
        gprint(" add %.2f water to %s" % (water_in, self.plant.NAME))
        self.water += water_in

    def gave_water(self, water_out):
        if self.water < water_out:
            water_taken = self.water
            self.water = 0.0
            return water_taken
        else:
            self.water -= water_out
            return water_out
