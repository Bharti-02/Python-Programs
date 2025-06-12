# multiple of 3 print Fizz , multiple of 5 print Buzz, multilple of 3,5 print fizzbuzz

n=int(input("Enter number:"))

for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
        