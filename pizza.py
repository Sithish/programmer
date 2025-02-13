print("welcome to python pizza delivery.")
pizza_size = input("what size of pizza you want?S,M or L: ")
preparation_of_pizza = input("what you prepration of pizza? y or n: ")
extra_chesse = input("what you want extra chesse? y or n: ")

bill=0
if pizza_size == "S":
    bill += 15
    
elif pizza_size =="M":
    bill += 20
    

else:

    bill +=25
    
    
if preparation_of_pizza == "y":
    if pizza_size == "s":
        bill += 2
    else:
        bill += 3
    


if extra_chesse  == "y":

    bill += 1
print(f"youre final bill is: ${bill}.")




    
    

