clock = input().split(" ")
clock_result = [0, 0]

clock = list(map(int, clock))
clock_result = list(map(int, clock_result))
    
if clock[1] < 45:
    if clock[0] == 0:
        clock[0] = 24
    clock_result[1] = clock[1] + 15
    clock_result[0] = clock[0] - 1
else:
    clock_result[1] = clock[1] - 45
    clock_result[0] = clock[0]

print(clock_result[0], clock_result[1])