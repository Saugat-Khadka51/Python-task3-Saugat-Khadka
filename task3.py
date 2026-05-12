#Qno 5
print ("WELCOME TO SUPERMARKET!!!")
total_purchase_amount = int(input('Enter the amount:'))
if total_purchase_amount > 5000:
    membership_staus = input("Do you have a membership card?: ").lower()
    if membership_staus == 'yes':
        discount = total_purchase_amount * 0.3
        print(f'You get a discount of {discount}')
        after_discount = total_purchase_amount - discount
        print(f'You have saved: {discount}')
        print(f'Your final amount is: {after_discount}')
    else:
        print(total_purchase_amount)
else:
    print(total_purchase_amount)

#Qno 6

print("Welcome to Magic Forest")
direction = input("Choose between north and south: ").lower()
if direction == 'north':
    1 == "Cross the River"
    2 == "Follow the path"
    path = int(input("Choose a path (1 or 2): "))
    if path ==1:
        print("Game Over")
    else:
        path == 2
        character = input("Choose a character fairy, ogre or elf: ").lower()
        if character == 'fairy' or character == 'ogre':
            print("Game over!!")
        else:
            print("You win!!")
elif direction == 'south':
    print("Game over")
else:
    print("Enter valid direction.")

#Qno 10
weight=float(input("enter your weight in kg"))
height=float(input("enter your height in meters"))
bmi=weight/(height**2)
print("Your BMI is:",bmi)
if weight<18.5:
    print("You are underweight")
elif weight>=18.5 and weight<25:
    print("You are normal weight")
elif weight>=25 and weight<30:
    print("You are overweight")
else:
    print("You are obese")   

#You are developing a simple ticket booking system for a movie theatre.
#The ticket price depends on the age of the person and
#whether they have a membership card. If the person is under 12, the
#ticket is free. If the person is between 12 and 60: If they have a
#membership card, the ticket costs Rs. 150. If not, the ticket costs Rs.200
#If the person is above 60, they get a senior citizen discount,and the ticket costs Rs.100
# #Write a Python program using nested if-else to calculate and print the ticket price based on the user's age and membership status.
age = int(input("Enter your age: "))
membership_card=input("Do you have a membership card? (yes/no):") .lower()
if age < 12:
    print("Your ticket is free.")
elif age >= 12 and age <= 60:
    if membership_card == "yes":
        print("The cost of ticket is Rs. 150")
    elif membership_card == "no":
        print("The cost of ticket is Rs. 200")
    elif age >60:
        print("You are qualified for senior citizen discount.")
        print("Your ticket costs Rs. 100")

#A company decided to give bonus of 5% to employee if his/heryear of service is more than 5years. Ask user for their salary and year
#of service and print the net bonus amount.     
salary=float(input("Enter your salary:"))
years_of_service=int(input("Enter your years of service:"))
if years_of_service > 5:
    bonus=salary*0.05
    print("Your bonus amount is:", bonus)
else:
    print("you are not eligible for bonus")

#Write a python program which accepts the radius of circle from user and compute the area.
import math
radius=float(input("Enter the radius of the circle:"))
area=math.pi*radius**2
print("The area of the circle is:", area)

#Accept the age, gender ('M', 'F'), number of days and display the Wages accordingly.
age=int(input("Enter your age:"))
gender=input("Enter your gender (M/F):").upper()
number_of_days=int(input("Enter the number of days:"))
if age < 18:
    print("You are not eligible to work.")
elif age >= 18 and age <=60:
    if gender =="M":
        wages=number_of_days*1000
        print("Your wages are:", wages)
    elif gender =="F":
        wages=number_of_days*800
        print("Your wages are:", wages)
else:
    print("Your are not eligible to work.")

#A utility company charges different rates based on electricity usage:
#If usage < 100 units then cost Rs 5 per unit
#If usage is between 100 to 300 units:First 100 units: Rs 5 Next units: Rs 8
#If usage is > 300 units: First 100: Rs 5 Next 200: Rs 8 Remaining: Rs
#10 Write a Python program to calculate the electricity bill based on the above rates. Accept the number of units consumed from the user and print the total bill amount.
units_consumed=int(input("Enter the number of units consumed:"))
if units_consumed < 100:
    bill_amount=units_consumed*5
    print("Your electricity bill is Rs.", bill_amount)
elif units_consumed >= 100 and units_consumed <= 300:
    bill_amount=100*5+(units_consumed-100)*8
    print("Your electricity bill is Rs.", bill_amount)
else:
    bill_amount=100*5+200*8+(units_consumed-300)*10
    print("Your electricity bill is Rs.", bill_amount)

#A store gives a 20% discount if the total purchase is above RS 1000 AND the customer is a member, or a 10% discount if the
#purchase is above RS 1000 but the customer is not a member. Write a
#program that takes total_amount and is_member (True/False) as input and prints the final amount after applying the correct discount
#or no discount.
total_amount=float(input("Enter the total purchase amount:"))
is_member=input("Are you a member? (True/False):").lower()
if total_amount > 1000 and is_member == "true":
    discount=total_amount*0.20
    final_amount=total_amount-discount
    print("Your final amount after discount is Rs.", final_amount)
elif total_amount > 1000 and is_member == "false":
    discount=total_amount*0.10
    final_amount=total_amount-discount
    print("Your final amount after discount is Rs.", final_amount)
else:
    print("No discount applied. Your total amount is Rs.", total_amount)

#Create a weight conversion program that:
#Asks the user what their Earth weight is as a float. Asks the user for a planet number as an int.
#Then, use an if/elif/else statement to calculate the user's weight on the destination planet.
#To calculate the user's weight: destination weight=Earth weight × relative gravity
#If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'
earth_weight=float(input("Enter your Earth weight:"))
planet_number=int(input("Enter a planet number (1-7):"))
if planet_number == 1:
    relative_gravity=0.38
    destination_weight=earth_weight*relative_gravity
    print("Your weight on Mercury is:", destination_weight)
elif planet_number == 2:
    relative_gravity=0.91
    destination_weight=earth_weight*relative_gravity
    print("Your weight on Venus is:", destination_weight)
elif planet_number == 3:
    relative_gravity=1.00
    destination_weight=earth_weight*relative_gravity
    print("Your weight on Earth is:", destination_weight)
elif planet_number == 4:
    relative_gravity=0.38
    destination_weight=earth_weight*relative_gravity
    print("Your weight on Mars is:", destination_weight)
elif planet_number == 5:
    relative_gravity=2.34
    destination_weight=earth_weight*relative_gravity
    print("Your weight on Jupiter is:", destination_weight)
elif planet_number == 6:
    relative_gravity=0.93
    destination_weight=earth_weight*relative_gravity
    print("Your weight on Saturn is:", destination_weight)
elif planet_number == 7:
    relative_gravity=0.92
    destination_weight=earth_weight*relative_gravity
    print("Your weight on Uranus is:", destination_weight)
else:
        print("Invalid planet number")

#Qno 21
desired_floor=int(input("Enter the desired floor (0-10):"))
total_weight=float(input("Enter the total weight load in kg:"))
door_status=input("Is the door closed? (yes/no):").lower()
if desired_floor < 0 or desired_floor > 10:
    print("INVALID FLOOR")
elif total_weight > 500:
    print("OVERWEIGHT: LIFT CANNOT MOVE")
elif door_status == "no":
    print("WARNING: CLOSE THE DOOR")
else:    
    print("Elevator is cleared to move to floor", desired_floor)






                   

        