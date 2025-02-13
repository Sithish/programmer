# height=int(input("enter your CM:"))

# if height > 120:
#     print("you can ride")
    
#     age=int(input("enter your age:"))
#     if age<12:
#         bill=5
#         print("if you age 12 charge amount is 5$.")
#     elif age<=18:
#         bill=7
#         print("if you age charge amount is 7$.")
#     elif age==18:
#         bill=12
#         print("if you age 18 charge amount is.12$") 
#         want_photos=input("you need photos:")
#         if want_photos=="yes":
# else:
#     print("you can't ride")

# a=int(input("enter the number:"))
# if (a%10==0):
#     print ("odd nuber")
# else:
#     print ("even number")

weight = 85
height = 1.85

bmi = weight / (height ** 2)
if bmi>=25:
    print("over weight")
elif bmi>=18.5:
    print("normal weight")
else:
    print("under weight")
    