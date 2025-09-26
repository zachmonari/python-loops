# The for loop
for i in range(10):
    print(i)
print("End of first loop! ")
for i in range(0,10,2):
    print(i)
print("End of second loop! ")
for j in range(10,0,-1):
    print(j)
print("End of third loop! ")

# the while loop
while True:
    text=input("Enter something (quit to exit): ")
    if text.lower() == "quit":
        break
    else:
        print("You  typed: ",text)
print("End of program! ")

count=0
while count <=10:
    print(count)
    count=count+1
print("End of program! ")

count=5
while count >0:
    print(count)
    count=count-1
print("End of program! ")

text=""
while text.lower()!="quit":
    text=input("Enter something (quit to exit): ")
    print("You  typed: ",text)

# The 'if' loop
try:
    age = int(input("Enter your age: "))
    print("If you are", age, "years old")
    if 13 <= age < 18:
        print("You are a teenager!.")
    elif 18 <= age < 65:
        print("You are an adult eligible for work!.")
    elif 65 <= age < 100:
        print("You should be retired from work!.")
    else:
        print("You are a child!.")
except ValueError:
    print("Enter a valid number between 1 and 100!.")
print("End of program! ")