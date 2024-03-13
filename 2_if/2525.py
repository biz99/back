clock = list(map(int, input().split(" ")))
clock_time = list(map(int, input().split()))

result_minute = (clock[1]+clock_time[0])%60
temp = clock[1] + clock_time[0]

plus_hour = temp//60

if temp < 60:
    plus_hour = 0

result_hour = clock[0] + plus_hour

if result_hour > 23:
    result_hour -= 24

print(f"{result_hour} {result_minute}")