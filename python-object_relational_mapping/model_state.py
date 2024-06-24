#!/usr/bin/python3
"""
Ce fichier contient la définition de la classe State et une instance
Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Création de l'instance Base
Base = declarative_base()

class State(Base):
    """
    Classe State qui hérite de Base.
    Représente la table MySQL 'states'.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
