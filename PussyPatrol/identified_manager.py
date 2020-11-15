import sqlite3
import uuid

##Labelling as follows: AnimalID = uniquie ID given to the singular animal; Name = the animals name i.e Mittens; BreedID = The number given to the breed fetched from the breed type.  Username = Person who identified it; 

def create_table_identified():
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS Identified 
  (AnimalID VARCHAR PRIMARY KEY,
  Name VARCHAR NOT NULL,
  BreedID VARCHAR NOT NULL,
  Username VARCHAR NOT NULL)""")


## adds new identified animal to database.  Must have a sighting of it to enter

def new_identified(Name,BreedID, Username):
  AnimalID = str(uuid.uuid1())
  database = sqlite3.connect("database.db")
  c = database.cursor()
  try:
    c.execute("""INSERT INTO Identified VALUES (?,?,?,?)""", (AnimalID,Name,BreedID,Username))
  except:
    return False
  database.commit()
  database.close()
  return AnimalID



def new_name(NewName,Name, AnimalID):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""UPDATE Identified SET Name = ? WHERE Name = ? AND AnimalID = ?""", (NewName,Name,AnimalID))
  database.commit()
  database.close()
  return AnimalID

def retrieve_identity(AnimalID):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""SELECT * FROM Identified WHERE AnimalID = ?""", [AnimalID])
  occurance = c.fetchall()
  return occurance



#create_table_identified()
#a = new_identified("Katie","Siamese","AJC")
#print(retrieve_identity(a))
#print(new_name("Kat", "Katie",a))
##tests successful

