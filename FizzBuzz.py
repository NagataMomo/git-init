string3="Fizz"
string5="Buzz"
string15="FizzBuzz"

for i in range(1, 101):
    if i % 15 == 0 :
        print(string15)
    elif i % 3 == 0:
        print(string3)
    elif i % 5 == 0:
        print(string5)
    else :
        print(i)
