def calc_sum(n):
    result = 0
    
    for i in range (1, n + 1):
        result = result + i
        
    return result

total = calc_sum(5)
print("The output is: ", total)
