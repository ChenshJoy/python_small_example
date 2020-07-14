#print("Enter a number:")
while True:
    num = input("Enter a number to get abs or input End to exit:")
    if num == 'End':
        break
    else:
        num_abs = abs(int(num,10))
        print(num_abs)
        
        continue