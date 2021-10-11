from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.base import ColumnCollection
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import TIMESTAMP, Float

class Geo():
     latitude = Column(Float(120), unique=True, nullable=False),
     longitude = Column(Float(120), unique=True, nullable=False)
