string = input()
length = len(string)
for i in range(length // 2):
    if string[i] != string[length - i - 1]:
        print("No")
        break
else:
    print("Yes")