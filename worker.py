import time
import threading

from mgprint import gprint

class Worker(threading.Thread):
    def __init__(self, garden):
        threading.Thread.__init__(self)
        self.stop_work = False
        self.garden = garden

    def check_plants(self):
        for place in self.garden.grow_places:
            if place.plant.is_alive and not self.stop_work:
                self.stop_work = False

    def add_water(self):
        for place in self.garden.grow_places:
            if place.plant.is_alive and place.water < float(place.plant.WATER/4):
                water = self.garden.get_water(place.plant.WATER)
                gprint(" WORKER: add %.2f water for %s place (%.2f left in tank)"
                    % (water, place.plant.NAME, self.garden.water_tank))
                place.add_water(water)

    def run(self):
        while not self.stop_work:
            self.add_water()
            time.sleep(1)
            self.check_plants()

        gprint(" WORKER: no more plants to work with")

    def stop(self):
        self.stop_work = True
