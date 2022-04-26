def arr_and_operation():
    arr1 = []
    num = int(input("enter the number elements wants to insects into the array :"))
    for i in range(num):
        el = int(input("enter the element : "))
        arr1.append(el)

    print(arr1)
    s1 = int(input("enter the  elements you wants to search  : "))
    a = 1
    for j in arr1:
        if s1 == j:
            print("the element found in position at : ", a)
        a += 1

arr_and_operation()