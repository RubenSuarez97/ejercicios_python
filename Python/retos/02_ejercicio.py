def is_positive(x):
    if x > 0:
        return True
    else:
        return False

#num = is_positive(-1)
#print(num)

def is_num(x):
    if isinstance(x,int) % 2 == 0:
        return True
    else:
        return False
    
num_2 = is_num(12.5)
print(num_2)
num_2 = is_num(5)
print(num_2)
num_2 = is_num(8)
print(num_2)
num_2 = is_num(-3)
print(num_2)

