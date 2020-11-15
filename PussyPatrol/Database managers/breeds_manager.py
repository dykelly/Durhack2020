import sqlite3
import uuid

## labelling as follows: BreedID = a uuid for that breed; Name = the name of the breed i.e. border collie; Tyype = the type of animal it is, i.e. dog.  (type is already a thing in python so I'm spelling it Tyype so to not get confused)


def create_table_breeds():
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS Breeds
  (BreedID VARCHAR PRIMARY KEY,
  Name VARCHAR NOT NULL,
  Tyype VARCHAR NOT NULL,""")

##Adds breed to database and produces a uuid for BreedID
def new_breed(Name, Animal_type):
  BreedID = uuid.uuid1()
  database = sqlite3.connect("database.db")
  c = database.cursor()
  try:
    c.execute("""INSERT INTO Breeds VALUES (?,?,?)""", (BreedID,Name,Animal_type))
  except:
    return False
  database.commit()
  database.close()


