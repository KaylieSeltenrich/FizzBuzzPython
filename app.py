numbers = [ 2, 13, 22, 50, 16, 18, 102, 222, 555, 543, 33, 30, 35, 20, 15]
     
def FizzBuzz(number):
        if(number % 3 == 0 and number % 5 == 0):
            print("FizzBuzz")
        elif(number % 3 == 0):
            print("Fizz")
        elif(number % 5 == 0):
            print("Buzz")

for number in numbers:
    FizzBuzz(number)