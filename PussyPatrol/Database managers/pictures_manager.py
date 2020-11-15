import sqlite3
import uuid

##labelling as follows: Pid =  picture id, basically the unique id for each individual picture; Asid = animal id from the sightings thing; Image =  name of the image file

def create_table_pictures():
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""CREATE TABLE IF NOT EXISTS Pictures
  (Pid VARCHAR PRIMARY KEY,
  Asid VARCHAR NOT NULL,
  Image VARCHAR NOT NULL)""")


##Adds new pic to database and creates it's Pid (a uuid)
def new_picture(Asid,Image):
  Pid = str(uuid.uuid1())
  database = sqlite3.connect("database.db")
  c = database.cursor()
  try:
    c.execute("""INSERT INTO Pictures VALUES (?,?,?)""" , (Pid,Asid, Image))
  except:
    return False
  database.commit()
  database.close()
  return Asid

def retrieve_picture(Asid):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""SELECT * FROM Pictures WHERE Asid = ?""", [Asid])
  occurance = c.fetchall()
  return occurance

#create_table_pictures()
#c = new_picture("123","im.jpeg")
#print(retrieve_picture(c))
##Testing Successful

