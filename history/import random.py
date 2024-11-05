import random

def game():
    number = random.randint(1, 100)
    guess = None

    while guess != number:
        guess = int(input("请猜测一个数字（1-100）："))

        if guess < number:
            print("太小了！")
        elif guess > number:
            print("太大了！")

    print(f"恭喜你！你猜测的数字是{number}！")

if __name__ == "__main__":
    game()