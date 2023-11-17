Rivers = {'Tigris':'Turkey','Amazon':'Brazil','Huang He':'China'}
for river, country in Rivers.items():
 print("The " + river + " flows through " + country + ".")
print("\nThe following Rivers are included in this data set:")
for river in Rivers.keys():
  print('* ' + river)
print("\nThe following countries are included in this data set:")
for country in Rivers.values():
    print('* ' + country)