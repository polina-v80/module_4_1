from fakemath import divide as fakedivide
from truemath import divide as truedivide

result1 = fakedivide(69, 3)
result2 = fakedivide(3, 0)
result3 = truedivide(49, 7)
result4 = truedivide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)