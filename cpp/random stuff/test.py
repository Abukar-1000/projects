
# def pattern(n,counter,value):
#     if (counter == n):
#         return value
#     else:
#         return pattern(n + 1,counter + 1,value) * n

# print(pattern(1,0,0))

def pattern(n,limit,value):
    
    if (n == limit):
        return value 
    else:
        value = n * (n + 1)
        return pattern(n + 1,limit,value)

print(pattern(0,3,0))
def function(n):
    temp = 0
    temp = n * (n + 1)
    return function(temp + 1)