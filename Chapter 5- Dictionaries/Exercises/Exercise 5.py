Pets=[]
Pet= {'Animal type':'Dog','Name':'Coco','Owner':'Suzy'}
Pets.append(Pet)
Pet= {'Animal type':'Parrot','Name':'Maya','Owner':'Alex'}
Pets.append(Pet)
Pet= {'Animal type':'Turtle','Name':'Toto','Owner':'Max'}
Pets.append(Pet)
for Pet in Pets:
  print(f"\nHere's what I know about {Pet['Name'].title()}:")
  for key, value in Pet.items():
   print(f" {key}: {value}")
