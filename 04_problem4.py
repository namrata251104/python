'''
sum(n) = 1+2+3+4...n
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3
'''

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

print(sum(4))