from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql.base import ColumnCollection
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.sqltypes import TIMESTAMP, Float

class Vital():
     temperature = Column(Float(120), unique=True, nullable=False),
     heart_rate = Column(Float(120), unique=True, nullable=False),
     breathing_frecuency = Column(Float(120), unique=True, nullable=False)