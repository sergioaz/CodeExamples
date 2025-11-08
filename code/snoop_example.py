"""
Example of snoop usage
"""
from snoop import snoop

@snoop
def collatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
    return 1

collatz(5)

"""
20:07:27.19 >>> Call to collatz in File "C:\Learn\CodeExamples\code\snoop_example.py", line 7
20:07:27.19 ...... n = 5
20:07:27.19    7 | def collatz(n):
20:07:27.19    8 |     while n != 1:
20:07:27.19    9 |         print(n)
20:07:27.19   10 |         if n % 2 == 0:
20:07:27.19   13 |             n = 3*n + 1
20:07:27.19 .................. n = 16
20:07:27.19    8 |     while n != 1:
20:07:27.19    9 |         print(n)
20:07:27.19   10 |         if n % 2 == 0:
20:07:27.19   11 |             n //= 2
20:07:27.19 .................. n = 8
20:07:27.19    8 |     while n != 1:
20:07:27.19    9 |         print(n)
20:07:27.19   10 |         if n % 2 == 0:
20:07:27.19   11 |             n //= 2
20:07:27.19 .................. n = 4
20:07:27.19    8 |     while n != 1:
20:07:27.19    9 |         print(n)
20:07:27.19   10 |         if n % 2 == 0:
20:07:27.19   11 |             n //= 2
20:07:27.19 .................. n = 2
20:07:27.19    8 |     while n != 1:
20:07:27.19    9 |         print(n)
20:07:27.19   10 |         if n % 2 == 0:
20:07:27.19   11 |             n //= 2
20:07:27.19 .................. n = 1
20:07:27.19    8 |     while n != 1:
20:07:27.19   14 |     return 1
20:07:27.19 <<< Return value from collatz: 1

Process finished with exit code 0
"""