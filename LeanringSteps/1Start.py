# Learning to Print and use Numbers



print ("Hello World!")

print ("Did you know 2+3 is: " , 2+3)

name = input("Do tell, what's your name? ")
print (f"Hello there, {name}!")

age = int(input("Now, how old are you? "))
print (f"Great! You're {age} years old!")

cpuAGE = 60

if age < cpuAGE:
    print (f"I'm a little bit older. I am a whole {cpuAGE} years old!")

elif age > cpuAGE:
    print (f"I'm a little bit younger. I am actually only {cpuAGE} years old.")

elif age == cpuAGE:
    print (f"Hey, we're the same age!")

print ("Look at this!")    
a = 3-4
b = 3+4
c = 3*4
d = 3/4
e = 3//4
f = 3%4
h = 3**4
print ("We have 3 blank 4. Let's fill in the blank!")

print(f"Sub: {a}  Sum: {b}  Multi: {c}  Divi1: {d}  Divi2: {e}  Divi3: {f}  Pow: {h}")
