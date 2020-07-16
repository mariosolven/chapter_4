# Python program to check if a number given is prime.

## Creating function.
def is_prime_or_not(num):
    ### If it's equal to 1, return False.
    if (num == 1): 
        return False
    ### If it's equal to 2, return True.
    elif (num == 2):
        return True;
    ### If the given number is > than 2 and its divisible by other number, return False.
    else:
        for j in range(2,num):
            if(num % j == 0):
                return False
        return True    

### Printing results.
print(is_prime_or_not(11))