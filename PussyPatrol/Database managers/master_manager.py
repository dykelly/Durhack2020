import sqlite3
import sightings_manager as sm

##This is where I'm gonna put all the functions that interact with multiple tables in the database for ease of access.
##Idk, might change that setup^


##When you've identified a sighting as a particular animal.  Adds the Animal ID to the sighting database, checks if that sighting already has an animal id first.
def sighting_identified(Asid,AnimalID):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""SELECT AnimalID FROM Sightings WHERE Asid = ?""", (Asid))
  existingId = c.fetchall()
  if existingId == []:
    ##add animalid to sighting
    sm.update_sighting_AnimalID(AnimalID,Asid)
  else:
    return "Animal is already Idenified"

## I'm gonna add a funciton to identify cats in an x mile radius from as much as n time ago I just need to work out how to use gps first