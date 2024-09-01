def get_password(n):
    result = ""
    for i in range(1, n):
        for j in range(i+1, n+1):
            if (i + j) == n:
                result += str(i) + str(j)
            elif (i + j) % n == 0:
                result += str(i) + str(j)
    return result
for number in range(3, 21):
    print(f"{number} - {get_password(number)}")
