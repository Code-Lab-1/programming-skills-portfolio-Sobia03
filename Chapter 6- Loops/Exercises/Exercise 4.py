Sandwich_orders= ['Roast beef','Chicken mayo','Tuna melt']
Finished_sandwiches= []
while Sandwich_orders:
  now_sandwich= Sandwich_orders.pop()
  print("Your " + now_sandwich + " is being prepared." )
  Finished_sandwiches.append(now_sandwich)
print("\n")
for sandwich in Finished_sandwiches:
  print("I'm done making your " + sandwich + ".")