print("welcome to my computer quizz ")

playing = input("Do you want to play ? : ")

if playing.lower() != "yes":
    quit()

print("Okay ! Let's play :) ")

score = 0

answer = input("what does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("correct !")
    score +=1
else:
    print("Incorrect !")

answer = input("what does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("correct !")
    score +=1
else:
    print("Incorrect !")

answer = input("what does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("correct !")
    score +=1
else:
    print("Incorrect !")
   
answer = input("what does CPU stands for ?")
if answer.lower() == "central processing unit":
    print("correct !")
    score +=1
else:
    print("Incorrect !")


print(f"You got {str(score)} questions correct")
print(f"you got {score/4 *100} %.")



