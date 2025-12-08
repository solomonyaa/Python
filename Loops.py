
# Control Flow
print("=" * 50, "\nControl Flow\n", "=" * 50, sep="")

myNum = 5

while myNum <= 50:
    if myNum == 5:
        print('first num is', myNum)
    elif myNum == 50:
        print('last num is', myNum)
    else:
        print('next num is', myNum)
    myNum += 5

##########################################################################
# 7 BOOM!
print("=" * 50, "\n7 BOOM!\n", "=" * 50, sep="")

myNum = 1

while myNum <= 100:
    if myNum % 7 == 0 or str(7) in str(myNum):
        print(f"BOOM! ({myNum})")
    else:
        print(myNum)
    myNum += 1

##########################################################################
# Star Triangles
print("=" * 50, "\nStars Triangles\n", "=" * 50, sep="")

print("Incremental:")
for i in range(1, 11):
    print("*" * i)

print("Decremental:")
for i in range(10, 0, -1):
    print("*" * i)