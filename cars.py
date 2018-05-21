showroom = set()
showroom.update(["car","truck","tractor","trailer","camaro","orange car"])
print(len(showroom))

showroom.add("trailer")
print(showroom)
showroom.update(["other car", "another car"])
print(showroom)
showroom.discard("trailer")
print(showroom)

junkyard = set()
junkyard.update(["red car","green car", "car","truck","tractor"])
set2 = junkyard.intersection(showroom)
print("set 2", set2)

set3 = junkyard.union(showroom)
print ("bought junkyard",set3)

set3.discard("camaro")
print("got rid of camaro", set3)