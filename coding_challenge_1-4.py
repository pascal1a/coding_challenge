


################ Problem 1 ################
def main():
    x = int(input())
    result = ((x // 3) * 2) + (0 if x % 3 == 0 else 1)
    print(result)
    
if __name__ == '__main__':
    main() 
       
################ Problem 2 ################
myList = [17 ,24 ,7 ,45 ,15 ,14 ,37 ,40 ,8 ,23 ,27 ,17]
z = 64
number = [i[0] for i in sorted(enumerate(myList), key=lambda x:x[1])]
no_of_stocks = 0
buy = 0
myList.sort()

for i in range(len(myList)):
    if(z > 0):
        buy = min(number[i], z //  myList[i])
        no_of_stocks += buy
        z-= buy*myList[i]   

def securitiesBuying(z, security_value):
    no_of_stocks=0
    #participants code here
    number = [i[0] for i in sorted(enumerate(security_value), key=lambda x:x[1])]
    security_value = [int(i) for i in security_value]
    security_value.sort()
    print(security_value)
    buy = 0
    money = int(z)
    for i in range(len(security_value)):
        if(int(money) > 0):
            buy = min(int(number[i]), money //  int(security_value[i]))
            y = range(len(security_value))
            no_of_stocks += buy
            print(buy)
            money-= buy*int(security_value[i])
    return no_of_stocks


def main():
    z = input()
    security_value = []
    security_value = input().split()
    no_of_stocks_purchased=securitiesBuying(z,security_value)
    print(no_of_stocks_purchased)

################ Problem 3 ################
def securitiesBuying(z, security_value):
    no_of_stocks=0
    #participants code here
    temp = [int(i) for i in security_value]
    security_value = [int(i) for i in security_value]
    security_value_unsorted = temp
    security_value.sort()
    buy = 0
    money = int(z[0])
    for i in range(len(security_value)):
        if(int(money) > 0):
            buy = min(int(security_value_unsorted.index(security_value[i])) + 1, money //  int(security_value[i]))
            y = range(len(security_value))
            no_of_stocks += buy
            money-= buy*int(security_value[i])
    return no_of_stocks


def main():
    z = input().split()
    security_value = []
    security_value = input().split()
    no_of_stocks_purchased=securitiesBuying(z,security_value)
    print(no_of_stocks_purchased)




if __name__ == '__main__':
    main()


################ Problem 4 ################
import math
import os
import random
import re
import sys

def portfolio_profit_maximisation(maxSum, a, b):
    # Write your code here
    total_sum_a = 0
    total_sum_b = 0
    iterator = 0
    

    for i in a:
        if i+total_sum_a <= maxSum:
            iterator+=1
            total_sum_a+=i
        else:
            break  
    i = iterator-1
    
    
     
    for j in range(len(b)):
        print(j)
        if (j < len(b)):
            if total_sum_b + b[j] <= maxSum:  
                if total_sum_a+b[j] <= maxSum:
                    total_sum_a+=b[j]
                    total_sum_b+=b[j]
                    j+=1
                    iterator+=1
                else :
                    total_sum_a-=a[i]
                    i-=1
                    total_sum_a+=b[j]
                    total_sum_b+=b[j]
                    j+=1
            else:
                break
    
    return (iterator)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    maxSum = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = portfolio_profit_maximisation(maxSum, a, b)
    print(result)

