import geojson

class MyPoint():
     def __init__(self, x, y):
         self.x = x
         self.y = y

     @property
     def __geo_interface__(self):
         return {'type': 'Point', 'coordinates': (self.x, self.y)}