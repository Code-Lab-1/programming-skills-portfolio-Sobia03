while True:
 money= input("How much money do you have?: ")
 money= int(money)
 if money < 100:
   print("You cannot buy only one item.")
 elif money > 100:
   print("You can buy three items.")
 else:
   print("You can buy many items.")