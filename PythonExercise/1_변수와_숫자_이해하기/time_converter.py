time = 12345
hour = time // 3600
time %= 3600
minute = time // 60
time %= 60

print("12345초는", hour, "시간", minute, "분", time, "초입니다.")
