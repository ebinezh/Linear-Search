# Linear search
n = int(input("Enter the size of list: "))
lst = []
flag = False
print("Enter the elements")
for i in range(0, n):
    lst.append(int(input()))
print(lst)
x = int(input("Enter the element to search: "))
for i in range(0, n):
    if x == lst[i]:
        flag = True
        break
if flag:
    print("The element is found")
else:
    print("The element is not found")


# thanks for watching
# like share & subscribe to
# dream2code
