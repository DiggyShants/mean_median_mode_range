from integers import numbers
import statistics

numberofnumbers = len(numbers)
numbers.sort()
print(numbers)

def mean():
    totalsum = sum(numbers)
    mean = totalsum//numberofnumbers
    print("Mean: ", mean)

def median():
    half = numberofnumbers // 2
    median = numbers[half - 1]
    print("Median: ", median)

def mode():
    mode = statistics.multimode(numbers)
    print("Mode: ", mode)

def range():
    range = numbers[numberofnumbers - 1] - numbers[0]
    print("Range: ", range)

response = input("Do you want the mean, median, mode or range? (mean/median/mode/range): ").lower().strip()

if response == "mean":
    mean()
elif response == "median":
    median()
elif response == "mode":
    mode()
elif response == "range":
    range()