import time
import threading

from mgprint import gprint
import plant

class Garden():
    grow_places = []

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
            self.no_more_plants = False
            self.grow_places = grow_places

        def check_plants(self):
            if self.no_more_plants:
                self.stop_nature = True

            for place in self.grow_places:
                if not place.plant.grow_up and place.plant.is_alive:
                    self.stop_nature = False
                place.plant.update_status()

        def drink_water(self):
            for place in self.grow_places:
                if place.plant.is_alive:
                    water = place.gave_water(place.plant.REQUIRED_WATER)
                    gprint(" we have %d water for %s" % (water, place.plant.NAME))
                    place.plant.drink_water(water)

        def run(self):
            while not self.stop_nature:
                self.drink_water()
                time.sleep(1)
                self.check_plants()

            gprint(" no more plants to grow")

        def stop(self):
            self.no_more_plants = True

    def __init__(self):
        self.water_tank = 150
        self.nature_thread = self.Nature(self.grow_places)

    def start(self):
        self.nature_thread.start()
        self.nature_thread.join()

        self.summary()

    def stop(self):
        gprint(" no more packages expected")
        self.nature_thread.stop()

    def plant(self, plant):
        place = self.GrowPlace(plant)
        place.add_water(plant.WATER)

        self.grow_places.append(place)

    def summary(self):
        number = 1
        total_value = 0

        print("SUMMARY")

        for place in self.grow_places:
            print("[%3d] %s = %d" % (number, place.plant.NAME, place.plant.VALUE))

            if place.plant.is_alive:
                total_value += place.plant.VALUE
            number += 1

        print("Total value: %s" % total_value)
