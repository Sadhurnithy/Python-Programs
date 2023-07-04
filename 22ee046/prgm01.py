
#finding factorial
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)


#Checking Palindrome
def palindrome(n):
    num=str(n)
    reverse=num[::-1]
    return num==reverse


#CALCULATING THE NUMBER OF DIGITS
def digit_count(n):
    return len(str(n))


#Main Function
def task():
    Number=int(input("Enter the number:"))

#Defining the Even part
    if Number%2==0:
        if palindrome(Number):
            print(f"The Given Number {Number} Is Palindrome.")
        else:
            print(f"The Given Number {Number} Is Not a Palindrome.")


#Defining the Odd part
    else:
        Fact=factorial(Number)
        digits=digit_count(Fact)

        print(f"The factorial of the number {Number} is {Fact}.")
        print(f"The number {Number} contains {digits} digits.")

task()

