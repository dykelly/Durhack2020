import sqlite3
import sightings_manager as sm
import math
##dunno if this works  Someone plez test

##This is where I'm gonna put all the functions that interact with multiple tables in the database for ease of access.
##Idk, might change that setup^


##When you've identified a sighting as a particular animal.  Adds the Animal ID to the sighting database, checks if that sighting already has an animal id first.
def sighting_identified(Asid,AnimalID):
  database = sqlite3.connect("database.db")
  c = database.cursor()
  c.execute("""SELECT AnimalID FROM Sightings WHERE Asid = ?""", [Asid])
  existingId = c.fetchall()
  if existingId == [(None,)]:
    ##add animalid to sighting
    sm.update_sighting_AnimalID(AnimalID,Asid)
  else:
    return "Animal is already Idenified"

## I'm gonna add a funciton to identify cats in an x mile radius from as much as n time ago I just need to work out how to use gps first

##Using Gps as long and lat and datetime as epoch

def hot_puss_in_your_area(Lat, Lon ,diagDistKm=5,dateTime=None,dayPrevious=None):
  ##get radius of Gps, and time range, then search through for these

  R = 6378.1 #Radius of the Earth
  brng = 0.79 #Bearing os 45 degrees converted to radians.
  brng2 = 3.93 #Bearing of 225 converted to radians.
  d = diagDistKm #Distance in km
  lat1 = math.radians(Lat) #Current lat point converted to radians
  lon1 = math.radians(Lon) #Current long point converted to radians

  upperlat =math.degrees(math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng)))

  upperlon = math.degrees(lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(upperlat)))

  lowerlat = math.degrees(math.asin( math.sin(lat1)*math.cos(d/R) + math.cos(lat1)*math.sin(d/R)*math.cos(brng2)))

  lowerlon = math.degrees(lon1 + math.atan2(math.sin(brng2)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lowerlat)))

  
  if dateTime != None :
    epochPrev = dateTime - dayPrevious*86400
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT * FROM Sightings WHERE dateTime BETWEEN ? AND ? AND Lat BETWEEN ? AND ? AND Lon BETWEEN ? AND ?""", (epochPrev,dateTime,lowerlat,upperlat,lowerlon,upperlon))
    puss_in_area = c.fetchall()
  else:
    database = sqlite3.connect("database.db")
    c = database.cursor()
    c.execute("""SELECT * FROM Sightings WHERE Lat BETWEEN ? AND ? AND Lon BETWEEN ? AND ?""", (lowerlat,upperlat,lowerlon,upperlon))
    puss_in_area = c.fetchall()


  return puss_in_area


#a = sm.new_sighting(50,50,555512345,"AJC","Cat")
#print(sighting_identified(a,"B"))
#print(hot_puss_in_your_area(50,50,5,555512345,1))

##Testing almost complete:
##We're able to find hot_puss_in_your_area!!!
##need to test othe function and make a variation on the hot puss one















