import sqlite3
import uuid
from PussyPatrol.Sighting import Sighting

##Labelling as follows: Asid = animal sighting id; Gps and DateTime are obvious; AnimalID = The ID for a specific individual animal i.e Mittens ; Username = username of user who logged the sighting

##Sightings is the name of the table uwu
##NOTE THAT IVE CHANGED GPS TO TWO SEPARATE VALUES OF LAT AND LON

def create_table_sightings():
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS Sightings
  (Asid VARCHAR PRIMARY KEY,
  Lat VARCHAR NOT NULL,
  Lon VARCHAR NOT NULL,
  DateTime VARCHAR NOT NULL,
  AnimalID VARCHAR,
  Username VARCHAR NOT NULL,
  AnimalType VARCHAR NOT NULL)""")


##Adds new sighting and creates a uuid for Asid
def new_sighting(Lat, Lon, DateTime, AnimalID, Username, AnimalType ):
  Asid = str(uuid.uuid1())
  print(Asid)
  database = sqlite3.connect("database.db")
  c = database.cursor()
  try:
    c.execute("""INSERT INTO Sightings VALUES (?,?,?,?,?,?,?)""",(Asid, Lat, Lon , DateTime, AnimalID, Username, AnimalType))
    database.commit()
    database.close()
    return Asid
  except Exception as e:
    print(f'Exception occured: {e}')
    return False


##updates spectifcally the AnimalID for a sighting, doesn't check it if an animalID is already assigned
def update_sighting_AnimalID(AnimalID,Asid):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""UPDATE Sightings SET AnimalID = ? WHERE Asid =? """, (AnimalID,Asid))
  database.commit()
  database.close()

def update_sighting_Username(NewUserName,Username):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""UPDATE Sightings SET Username = ? WHERE Username = ? """, (NewUserName, Username))
  database.commit()
  database.close()
      
def retrieve_sighting(Asid):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""SELECT * FROM Sightings WHERE Asid = ?""" , [Asid])
  occurance = c.fetchall()
  # sighting = Sighting()
  print(occurance)

create_table_sightings()
a = new_sighting(0,0,1605415843, 123, "AJC", "Dog")
retrieve_sighting(a)