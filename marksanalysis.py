marks = [45, 78, 62, 89, 55, 92, 38, 76]

total = sum(marks)
print("sum: ",total)

avg = total / len(marks)
print("average; ",avg)

highest = max(marks)
print("highest: ",highest)

lowest = min(marks)
print("lowest: ",lowest)

ascending = sorted(marks)
print("ascending: ", ascending)

above_avg = [mark for mark in marks if mark > avg]
print("Above average: ", above_avg)



