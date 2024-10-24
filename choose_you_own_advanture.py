name = input("Type your name : ")
print("Welcome", name, "to this advanture!")

answare = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answare == 'left':
    answare = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answare == 'swim':
        print("You swam acrross and were eaten by an alligator.")
    elif answare == 'walk':
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose. ")

elif answare == 'right':
    answare = input("You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answare == 'back':
        print("You go backe and lose.")
    elif answare == 'cross':
        answare = input("You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")
        if answare == 'yes':
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answare == 'no':
            print("You ignore the stranger and they are offended and you lose.")
        else:
            print("Not a valid option, You lose.")
    else:
        print("Not a valid option, You lose.")
else:
    print("Not a valid option, you lose.")

print("Thank you for trying ", name)
    
