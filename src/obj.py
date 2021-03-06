# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon 

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon.

class Waypoint(LatLon):
    def __init__(self, name, lat, lon):
        super().__init__(lat, lon)
        self.name = name

    def formatting(self):
        return "{}: latitude {}, longitude {}".format(
            self.name, self.lat, self.lon)

# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?
class Geocache(Waypoint):
    def __init__(self, name, difficulty, size, lat, lon):
        super().__init__(name, lat, lon)
        self.size = size
        self.name = name
        self.difficulty = difficulty

    def formatting(self):
        return "{}: difficulty {}, size {}, latitude {}, longitude {}".format(
            self.name, self.difficulty, self.size, self.lat, self.lon)

# Make a new waypoint "Catacombs", 41.70505, -121.51521

newWaypoint = Waypoint("Catacombs", 41.70505, -121.51521)

# Print it

print(newWaypoint.formatting())

# Without changing the following line, how can you make it print into something
# more human-readable?
w = newWaypoint.formatting()
print(w)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

newGeocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)

# Print it--also make this print more nicely
g = newGeocache.formatting()
print(g)
