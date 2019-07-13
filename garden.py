import time
import threading

from mgprint import gprint
import plant

class Garden():
    grow_places = {}

    class GrowPlace():
        def __init__(self, plant):
            self.plant = plant
            self.water = 0

        def add_water(self, water_in):
            self.water += water_in

        def gave_water(self, water_out):
            if self.water < water_out:
                water_taken = self.water
                self.water = 0
                return water_taken
            else:
                self.water -= water_out
                return water_out

    class Nature(threading.Thread):
        def __init__(self, grow_places):
            threading.Thread.__init__(self)
            self.stop_nature = False
            self.grow_places = grow_places

        def check_plants(self):
            self.stop_nature = True

            for place in self.grow_places:
                if place.plant.grow_up == False:
                    self.stop_nature = False
                    place.plant.update_status()

        def drink_water(self):
            for place in self.grow_places:
                if place.plant.is_alive:
                    water = place.gave_water(place.plant.WATER/place.plant.FREQUENCY)
                    place.plant.add_water(water)

        def run(self):
            while not self.stop_nature:
                gprint("nature checks plants...")
                self.drink_water()
                time.sleep(1)
                self.check_plants()

    def __init__(self):
        self.water_tank = 150
        self.nature_thread = self.Nature(self.grow_places)

    def start(self):
        self.nature_thread.start()
        self.nature_thread.join()

    def plant(self, plant):
        self.grow_places.append(GrowPlace(plant))
