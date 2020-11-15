import breeds_manager as bm
import identified_manager as im
import master_manager as mm
import pictures_manager as pm
import sightings_manager as sm
import users_manager as um

##I know theres a differetn way other than importing them all but fuck u

bm.create_table_breeds()
im.create_table_identified()
pm.create_table_pictures()
sm.create_table_sightings()
um.create_users_table()


##Creating a user called Stacy who spots 3 cats 2 with pics and changes her username to Stacy's_mum.

um.new_user("Stacy","123")
a = sm.new_sighting(54.7732,-1.5764, 123456789,"Cat","Stacy") ##This return Aisd for ease
pm.new_picture(a,"Cat.jpeg")
b = sm.new_sighting(54.7732,-1.5764, 123456798,"Cat","Stacy")
pm.new_picture(b,"catttt.jpeg")
sm.new_sighting(54.7732,-1.5764, 123456989,"Cat","Stacy")
um.update_username("Stacy","Stacys_mum","123")


##making a few breeds
si = bm.new_breed("Siamese", "Cat") ##returns breed ids
cr = bm.new_breed("Cross","Cat")

##Creating a user called Karen who identifies one of the stacy cats as carlMarx 

um.new_user("Karen","456")
sm.new_sighting(54.7732,-1.5764, 123456790,"Cat","Karen")
carl = im.new_identified("carlMarx", si, "Karen") ##returns animal id
mm.sighting_identified(a,carl)



##Another user called dick_sucker69 who ids another of stacys finds
um.new_user("dick_sucker69","345")
stonks = im.new_identified("stonks",cr,"Cat")##animalID
mm.sighting_identified(b,stonks)

##A mouse at dans house
um.new_user("Dachode","chode")
sm.new_sighting(54.7732,-1.5764, 123456989,"Mouse","Dachode")

##stop! Look! HOT PUSS IN YOUR AREA
mm.hot_puss_in_your_area(54.773, -1.5764 ,diagDistKm=5,dateTime=None,dayPrevious=None)


##54.7732° N, 1.5764° W