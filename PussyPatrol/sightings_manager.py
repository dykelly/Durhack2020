import sqlite3
import uuid

##Labelling as follows: Asid = animal sighting id; Gps and DateTime are obvious; AnimalID = type of animal??? (I think) ; Username = username of user who logged the sighting

##Sightings is the name of the table uwu

def create_table_sightings():
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS Sightings
  (Asid VARCHAR PRIMARY KEY,
  Gps VARCHAR NOT NULL,
  DateTime VARCHAR NOT NULL,
  AnimalID VARCHAR NOT NULL,
  Username VARCHAR NOT NULL)""")


##Adds new sighting and creates a uuid for Asid
def new_sighting(Gps, DateTime, AnimalID, Username ):
  Asid = uuid.uuid1()
  database = sqlite3.connect("database.db")
  c = database.cursor()
  try:
    c.execute("""INSERT INTO Sightings VALUES (?,?,?,?,?)""",(Asid, Gps, DateTime, AnimalID, Username))
  except:
    return False
  database.commit()
  database.close()

def update_sighting_Username(NewUserName,Username):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""UPDATE Sightings SET Username = ? WHERE Username = ? """, (NewUserName, Username))
  database.commit()
  database.close()
      



  


