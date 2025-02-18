# v0.3) https://github.com/moaknock/2025_KEB_datastructure_algorithm 의
# v0.7 guess number 예제를 자동화하고 로그파일(guess.txt)를 남기도록 코드를 수정하시오.
# 단, 해당 프로그램이 로그시간을 갖도록한다.

import random

def auto_input_number(low,high) -> int:
    return(low + high)//2
   # pass

low = 1
high = 100
answer = random.randint(1,100)
chance = 7

while chance != 0:
    guess = int(input("Input guess number : "))
    if guess == answer:
        print(f'You win. Answer is {answer}')
        fp.write(f'You win. Answer is {answer}\n')
        return
    elif mid > answer:
        chance = chance -1
        print(f'{mid} is bigger. Chance left
