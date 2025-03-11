import random
name=input("Enter your name:")
if name=="Varun":
    print(f"Hello! {name}")
print("End of Program 1.\n")
    

number = int(input("Enter a number:"))
if number%2==0:
  print("This is an even number.\n")
else:
  print("This is an odd number.\n")


height = float(input("Enter height(in m):"))
weight = float(input("Enter weight(in kg):"))
bmi=round(weight/pow(height,2),2)
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi<25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
else:
  print(f"Your BMI is {bmi}, you are obese.")

print("******Coin_Toss******")
Coin=random.randint(0,1)
if Coin==0:
    print("Tails.")
else:
    print("Heads.")
    
    
year = int(input("Enter an year:"))
if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
    print("Leap year")
else:
  print("Not leap year")
  