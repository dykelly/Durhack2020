import sqlite3
import uuid

## labelling as follows: BreedID = a uuid for that breed; Name = the name of the breed i.e. border collie; AnimalType = the type of animal it is, i.e. dog. 


def create_table_breeds():
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS Breeds
    (BreedID VARCHAR PRIMARY KEY,
    Name VARCHAR NOT NULL,
    AnimalType VARCHAR NOT NULL)""")

##Adds breed to database and produces a uuid for BreedID
def new_breed(Name, AnimalType):
  BreedID = str(uuid.uuid1())
  database = sqlite3.connect("database.db")
  c = database.cursor()
  try:
    c.execute("""INSERT INTO Breeds VALUES (?,?,?)""", (BreedID,Name,AnimalType))
  except:
    return False
  database.commit()
  database.close()
  return BreedID

def retrieve_breed(BreedID):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""SELECT * FROM Breeds WHERE BreedID = ?""" , [BreedID])
  occurance = c.fetchall()
  return occurance

#create_table_breeds()
#a = new_breed("Siamese","cat")
#print(retrieve_breed(a))
##Tests succesful


