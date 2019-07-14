import time
import threading

from mgprint import gprint

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
                gprint(" GARDEN: we have %.2f water for %s (%.2f left)" % (water, place.plant.NAME, place.water))
                place.plant.drink_water(water)

    def run(self):
        while not self.stop_nature:
            self.drink_water()
            time.sleep(1)
            self.check_plants()

        gprint(" GARDEN: no more plants to grow")

    def stop(self):
        self.no_more_plants = True
