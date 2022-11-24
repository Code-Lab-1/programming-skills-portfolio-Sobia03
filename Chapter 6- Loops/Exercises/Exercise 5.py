Sandwich_orders= ['Roast beef','Pastrami','Chicken mayo','Pastrami','Tuna melt','Pastrami']
Finished_sandwiches= []
print("I'm sorry, we have run out of Pastrami.")
while 'Pastrami' in Sandwich_orders:
  Sandwich_orders.remove("Pastrami")
while Sandwich_orders:
  now_sandwich= Sandwich_orders.pop()
  print("Your " + now_sandwich + " is being prepared." )
  Finished_sandwiches.append(now_sandwich)
for sandwich in Finished_sandwiches:
  print("I'm done making your " + sandwich + ".") 