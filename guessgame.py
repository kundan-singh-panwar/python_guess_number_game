n = 25
att = [1, 2, 3, 4, 5]

c = 1
print("Guess a number between 1 to 30 | you have 5 chances to win")
print("Go with your First Chance : ", c)
for c in att:
    uinp = int(input("guess the number : "))

    if uinp != n and uinp <= 30 and uinp >= 20:
        print("you are almost near to win ! pls try again" "your chance number :", c+1)
        print("your chance number :", c+1)
    elif uinp < 20 and uinp>10:
        print("you are far ! pls try again")
        print("your chance number :", c + 1)
    elif uinp < 10 and uinp > 5:
        print("you are very far ! pls try again")
        print("your chance number :", c + 1)
    elif uinp>30 or uinp < 5:
        print("you are out of range sorry ! pls try again")
        print("your chance number :", c + 1)
    elif uinp == n:
        print("Congratulation you are won! ")
        wonby = len(att)-c
        print("You are won by ", wonby, "chances")
        exit()

#i want to use function here for the game restart by using y or n condition
# print("Do You want To Start Again????")
# wish = input()
#wish1 = wish.Upper()
# if(wish == "y"):






