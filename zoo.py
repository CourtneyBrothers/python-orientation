aquarium = ("whale", "turtle", "seahorse", "starfish")
print(aquarium.index("turtle"))

if "turtle" in aquarium :
  print ("found it")

aquariumList = list(aquarium)
aquariumList.extend("dolphin","manateee","stingray")
tuple(aquariumList)