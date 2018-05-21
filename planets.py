planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Neptune","Planet 9"])
planet_list.insert(1,"Venus")
planet_list.insert(2,"Earth")
planet_list.insert(7,"Pluto")

rocky_planets = planet_list[:5]
print(rocky_planets)

del planet_list[7]
print(planet_list)

#spacecraft tuple
spacecrafts = (('Mercury','messenger'),('Venus','Pioneer Venus Multiprobe'),('Mars','Viking 1 lander'),('Mars','Viking 2 lander'),('Mars','Pathfinder'),('Jupiter','Galileo'), ('Saturn','Cassini'))

for planet in planet_list:
  for spacecraft in spacecrafts:
    eachLanding = []
    if spacecraft[0] == planet: 
      eachLanding.append(spacecraft[1])
      print ("{0} : {1}".format(planet,spacecraft[1]))


