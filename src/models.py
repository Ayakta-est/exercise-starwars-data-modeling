import os
import sys
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Column, Integer, String, DateTime, Float, Boolean, ForeignKey
from datetime import datetime, timezone

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)  # 30 caracteres, obligatorio y único
    password = Column(String(30), nullable=False)
    email = Column(String(80), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    
# Relación con favoritos, lazy joined controla cómo se cargan las relaciones entre tablas cuando consultas los datos.
    favorites = relationship('Favorite', back_populates='user', lazy="joined")  

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    climate = Column(String(50), nullable=False)
    terrain = Column(String(50), nullable=False)
    population = Column(Integer, nullable=False) 
    diameter = Column(Integer, nullable=False)  # Diámetro en km
    rotation_period = Column(Integer, nullable=False)  
    orbital_period = Column(Integer, nullable=False)  
    gravity = Column(Float, nullable=False)  
    surface_water = Column(Integer, nullable=False)  # % de agua en la superficie
    moons = Column(Integer, nullable=False)

    favorites = relationship('Favorite', back_populates='planet', lazy="joined")
    residents = relationship("Person", back_populates="homeworld") 

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
    length = Column(Float, nullable=False)  
    weight = Column(Float, nullable=False) 
    cargo_capacity = Column(Float, nullable=False) 
    consumables = Column(String(50), nullable=False)  # Duración del suministro
    fuel_type = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    favorites = relationship('Favorite', back_populates='vehicle', lazy="joined")

class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    birth_year = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    species = Column(String(50), nullable=False)
    mass = Column(Float, nullable=False)
    skin_color = Column(String(50), nullable=False)
    hair_color = Column(String(50), nullable=False)
    eye_color = Column(String(50), nullable=False)
    affiliation = Column(String(50), nullable=False)
    force_sensitive = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))

    homeworld_id = Column(Integer, ForeignKey('planet.id'), nullable=False)
    homeworld = relationship("Planet", back_populates="residents")

    favorites = relationship('Favorite', back_populates='person', lazy="joined")

class Favorite(Base):
    __tablename__ = 'favorite'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    people_id = Column(Integer, ForeignKey('person.id'), nullable=True)

    # Relación para que se pueda navegar
    user = relationship("User", back_populates="favorites")
    vehicle = relationship("Vehicle", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    person = relationship("Person", back_populates="favorites")

    def to_dict(self):
        return {}

## Generar el diagrama
render_er(Base, 'diagram.png')
