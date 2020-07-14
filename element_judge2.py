def element_judge2(a):
    flag = 0
    for i in range(0, len(a)):
        if a[i]:
            flag = 1
            print("Ture")
            return True
        else:
            flag = 0
    print("False")
    return False

if __name__ == '__main__':
    a = [0,0,0,[]]
    element_judge2(a)
    b = [0,0,1]
    element_judge2(b)