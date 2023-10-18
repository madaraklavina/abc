# abc

### Saturs

#### 1. Aprakstīt spēli
#### 2. Spēles loģika

dators nejauši ģenerē vienu skaitli no 1 līdz 100 un piedāvā spēlētājam uzminēt skaitli
spēles loģika aprakstīta šajā kodā:

```py
import random

repeat = True

while repeat:
    number = random.randint(1, 100)
    guess = 0
    tries = 0

    while guess != number:
        if guess > number:
            print("mazāk")
        else:
            print("vairāk")

        guess = int(input("Uzmini skaitli: "))
        tries += 1
    else:
        if tries < 4:
            print(f"tu uzminēji tikai pēc {tries} reizēm")
        elif tries < 7:
            print(f"uzmineji pēc {tries} reizem")
        else:
            print("hmm tomer uzminēji")   

    response = input("vai gribi turpināt? y/n: ")
    if response == "y":
        repeat = True
    else:
        repeat = False
        print("paldies par speli")

```

