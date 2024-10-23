print("Welcome to my computer quiz!")


playing = input('Do you want to play? ')

if playing.lower() == 'yes':
    quit()

print("ok, Let's play!")
score = 0

answare = input('what does CPU stand for? ')
if answare.lower() == 'central processing unit':
    print('Correct')
    score+=1
else:
    print("Incorrect")

answare = input("what does GPU stand for? ")
if answare.lower() == 'graphics processing unit':
    print("Correct")
    score+=1
else:
    print('Incorrect')

answare = input("what does RAM stand for? ")
if answare.lower() == 'randome access memory':
    print("Correct")
    score += 1
else:
    print('Incorrect')

answare = input("What does PSU stand for? ")
if answare.lower() == 'power suply unit':
    print('Correct')
    score += 1
else:
    print("Incorrect")


print('you got ' + str(score) + " questions correct!")
print('you got ' + str((score/4) * 100) + "%.") 


