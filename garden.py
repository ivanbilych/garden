import growplace
from mgprint import gprint
import nature
import plant

class Garden():
    grow_places = []

    def __init__(self, water):
        self.water_tank = float(water)
        self.nature_thread = nature.Nature(self.grow_places)
        gprint(" garden tank have %.2f of water" % water)

    def start(self):
        self.nature_thread.start()
        self.nature_thread.join()

        self.summary()

    def stop(self):
        gprint(" no more packages expected")
        self.nature_thread.stop()

    def get_water(self, water):
        if self.water_tank < water:
            water_taken = self.water_tank
            self.water_tank = 0.0
            return water_taken
        else:
            self.water_tank -= water
            return water

    def plant(self, plant):
        water = self.get_water(plant.WATER)

        if water:
            place = growplace.GrowPlace(plant)
            place.add_water(water)

            self.grow_places.append(place)
        else:
            gprint(" ERROR: no more water in tank, can't plant")

    def summary(self):
        number = 1
        total_value = 0

        print("SUMMARY")

        for place in self.grow_places:
            plant = place.plant
            status = "dead"

            if plant.is_alive:
                status = "alive"

            print("[%3d] %s = %d (%s)" % (number, plant.NAME, plant.VALUE, status))

            if plant.is_alive:
                total_value += plant.VALUE

            number += 1

        print("Total value: %s" % total_value)
