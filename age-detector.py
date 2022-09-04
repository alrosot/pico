import machine
import utime

LED = machine.Pin(15,machine.Pin.OUT)
LED.off()

# this program was written by an incredible kid

print("which year were you born in?")
bornyear = int(input())
print("you typed:",bornyear)

# here we check for time travellers
if bornyear >2022:
    print("Hey man from the future, you're not born yet!")
else:
    age=2022-bornyear
    print("your age is",age)

    if age < 12:
        print("Nice! You're still a child!")
        LED.on()
    else:
        print("you're an adult.sorry!")
