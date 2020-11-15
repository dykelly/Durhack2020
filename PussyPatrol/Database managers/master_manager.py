import sqlite3
import sightings_manager as sm
from geopy import Point
from geopy.distance import geodesic
##dunno if this works

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

##Using Gps as long and lat and datetime as epoch

def hot_puss_in_your_area(Lat, Lon ,dateTime=None,diagDistKm=5,dayPrevious=None):
  ##get radius of Gps, and time range, then search through for these

  upperlat,upperlon = geodesic(kilometers=diagDistKm).destination(Point(lat, lon), 45).format_decimal()
  lowerlat, lowelon = geodesic(kilometers=diagDistKm).destination(Point(lat, lon), 225).format_decimal()
  epochPrev = dateTime - dayPrevious*86400
  database = sqlite3.connect("database.db")
  c = data.cursor()
  c.execute("""SELECT * FROM Sightings WHERE dateTime BETWEEN ? AND ? AND Lat BETWEEN ? AND ? AND Lon BETWEEN ? AND ?""", (epochPrev,dateTime,lowerlat,upperlat,lowerlon,upperlon))
  puss_in_area = c.fetchall()
  return puss_in_area



