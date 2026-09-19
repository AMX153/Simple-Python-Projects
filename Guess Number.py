from random import randint

com_num = randint(1, 6)
tries = 0

while True:
    user_num = int(input("Enter your guess: "))
    tries = tries + 1
    if user_num > com_num:
        print("Kochiktar.")
    elif user_num < com_num:
        print("Bozorgtar.")
    else:
        print(f"Finish. You can find the number with {tries} tries.")
        break