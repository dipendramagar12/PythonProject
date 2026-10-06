marks = [ 75, 82, 68, 90, 55, 88, 72, 95]

print("Marks List:", marks)

total_marks = sum(marks)

average_marks = total_marks / len(marks)

highest_marks = max(marks)

lowest_marks = min(marks)

sum_marks = sum([1 for marks in marks if marks >= 70])

marks.sort(reverse=True)

number = int(input("Enter a number: "))
marks.append(number)

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")
print(f"Sum of Marks > 70: {sum_marks}")
print(f"Sorted Marks highest to lowest: {marks}")
print(f"Updated Marks List after adding {number}: {marks}")