def classify(value):
    if value < 78:
        return "Below range"
    elif value <= 82:
        return "In range"
    else:
        return "Above range"


def calculate_average(total, count):
    average_snapshot = total / count
    average_result = average_snapshot
    return average_result



n = int(input("Enter the number of ribbons: "))

total = 0
below = 0
in_range = 0
above = 0

for i in range(n):
    length = int(input("Enter the ribbon length: "))

    res = classify(length)
    print(res)
    total = total + length

    if res == "Below range":
        below = below + 1
    elif res == "In range":
        in_range = in_range + 1
    elif res == "Above range":
        above = above + 1

avg = calculate_average(total, n)



print(f"Total length: {total} cm")
print(f"Average length: {avg} cm")
print(f"Below range: {below}")
print(f"In range: {in_range}")
print(f"Above range: {above}")