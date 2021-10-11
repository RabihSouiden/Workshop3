from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.base import ColumnCollection
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import TIMESTAMP, Float
from flask_appbuilder import Model
from Geolocation import Geo
from MyPoint import MyPoint
from Vital_Signs import Vital
import geojson
import json

class Microchip(Model):
    timestamp = Column(TIMESTAMP)
    microchip = Column(String(120), unique=True, nullable=False,primary_key=True)
    pet_name = Column(String(120), unique=True, nullable=False)
    owner_name = Column(String(120), unique=True, nullable=False)
    species = Column(String(120), unique=True, nullable=False)
    geolocation = Geo()
    #point_instance = MyPoint(json.dumps(list(geolocation.longitude)), json.dumps(list(geolocation.latitude)))
    #geojson.dumps(point_instance, sort_keys=True)  
    vital_signs = Vital()

