# passwor genrators
import random

let = ['`', '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '+', '!', '@', '#', '$', '%', '^', '&', '*',
       '(',
       ')',
       'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
       'w',
       'x', 'y', 'z']

def passwordmaker():
    number = int(input("enter the length of the password : "))
    num=int(number)
    while num != 0:
        x = int(random.randint(0, 49))
        print(let[x], end="", flush=True)
        num -= 1


passwordmaker()
