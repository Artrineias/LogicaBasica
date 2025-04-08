from time import sleep


def fatorial(num,show=False):
    """
    ->Calculates the factorial of a number.
    :To num:The number to be calculated.
    :To show: (Optional) Show or not the account.
    :return: The factorial value of a number
    
    """
    fatorial = 1
    for c in range(num,0,-1):
        if show:
            print(c,end="")
            if c > 1:
                print(" X ",end="")
            else:
                print(" = ",end="")
        fatorial *= c
    return fatorial



print(fatorial(5,True))
sleep(3)
help(fatorial)