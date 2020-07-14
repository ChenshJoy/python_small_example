def element_judge(a):
    flag = 0
    for i in range(0, len(a)):
        if a[i]:
            flag = 1
        else:
            flag = 0
            print("False")
            return False
    print("True")
    return True

if __name__ == '__main__':
    a = [1,0,3,6]
    element_judge(a)
    b = [1,2,3]
    element_judge(b)



