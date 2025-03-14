import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er
from sqlalchemy import Column, Integer, String, DateTime, Float
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer(), primary_key=True)
    username = Column(String(30), nullable=False, unique=True) #30 caracteres,obligatorio un valor y único
    password = Column(String(30), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now(timezone.utc))

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer(), primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(timezone.utc))
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(String(50), nullable=False)
    diameter = Column(String(50), nullable=False)
    rotation_period = Column(String(50), nullable=False)
    orbital_period = Column(String(50), nullable=False)
    gravity = Column(String(50), nullable=False)
    surface_water = Column(String(50), nullable=False)
    moons = Column(String(50), nullable=False)
   

class Vehicle(Base):
    __tablename__ = 'vehicle'  

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    manufacturer = Column(String(50), nullable=False)
    vehicle_class = Column(String(50), nullable=False)
    crew = Column(Integer, nullable=False)  # Personas necesarias para conducirlo
    passengers = Column(Integer, nullable=False)  
    max_speed = Column(Float, nullable=False)  
    length = Column(Float, nullable=False)  # Longitud del vehículo
    weight = Column(Float, nullable=False) 
    cargo_capacity = Column(Float, nullable=False) 
    consumables = Column(String(50), nullable=False)  # Duración del suministro
    fuel_type = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now(timezone.utc))


class Person(Base):
    __tablename__ = 'person'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    addresses: Mapped[list["Address"]] = relationship(back_populates="person")


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    street_name: Mapped[str]
    street_number: Mapped[str]
    post_code: Mapped[str] = mapped_column(nullable=False)
    person_id: Mapped[int] = mapped_column(ForeignKey("person.id"))
    person: Mapped["Person"] = relationship(back_populates="address")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
