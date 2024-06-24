#!/usr/bin/python3
"""
Ce script crée la table 'states' dans la base de données MySQL.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    # Récupération des arguments (nom d'utilisateur, mot de passe et nom de la base de données)
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    # Création de l'engine SQLAlchemy
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(mysql_username, mysql_password, db_name), pool_pre_ping=True)
    
    # Création de toutes les tables
    Base.metadata.create_all(engine)
