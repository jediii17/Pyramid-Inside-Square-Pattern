recrow = int(input("\nEnter b: "))
trirow = int(input("Enter a: "))
print("\n")
# b must be greater than zero
# a must be greater than one
# b should be greater than a
# (b-a) should be an even number
if recrow <= 0:
    print("b must be greater than zero")
elif trirow <= 1:
    print("a must be greater than one")
elif recrow < trirow:
    print("b should be greater than a")
elif (recrow % 2) == 1:
    print("(b-a) should be an even number")
elif (trirow % 2) == 1:
    print("(b-a) should be an even number")
else:
    col = (2*recrow)-1
    rowboxContainerArr = [[""]*col for i in range(recrow)]
    trimidpt = int(col / 2)

    # print rectangle pattern
    for i in range(recrow):
        for j in range(col):
            if i == 0 or i == (recrow-1) or j == 0 or j == (col-1):
                rowboxContainerArr[i][j] = "b"
            else:
                rowboxContainerArr[i][j] = " "

    # print inside triangle pattern
    k = 0
    spacestart = 0
    nextrow = 0
    for i in range(1, trirow+1):
        spacestart = trimidpt
        if spacestart == 0:
            rowboxContainerArr[i+nextrow][spacestart] = " "
        else:
            ctr = 0
            for col in range(1, i+1):
                rowboxContainerArr[i+1][spacestart - ctr] = "a"
                rowboxContainerArr[i+1][spacestart + ctr] = "a"
                ctr += 1

    # print multidimensional array
    for i in range(len(rowboxContainerArr)):
        for j in range(len(rowboxContainerArr[i])):
            print(rowboxContainerArr[i][j], end="")
        print()
