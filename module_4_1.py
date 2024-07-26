import fake_math as fm
from true_math import divide as tm_divide

result1 = fm.divide(69, 3)
result2 = fm.divide(3, 0)
result3 = tm_divide(49, 7)
result4 = tm_divide(15, 0)
print(result1)
print(result2)
print(result3)
print(result4)
