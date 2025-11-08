"""
https://medium.com/the-pythonworld/why-almost-nobody-uses-pythons-bisect-module-but-should-5acd74ce2e43
The bisect module in Python provides support for maintaining a list in sorted order without having to sort the list after each insertion.
It uses a bisection algorithm to find the correct insertion point for new elements, making it efficient for certain use cases.
When Not to Use bisect
Like any tool, bisect isn’t perfect for every scenario.

If you need frequent random insertions into very large lists, bisect may still be too slow due to shifting elements. In such cases, a balanced tree or external library like sortedcontainers is better.

If your dataset doesn’t need to stay sorted (you sort once after collecting everything), then simple sorting is fine.

Think of bisect as the sweet spot for medium-sized sorted lists with occasional insertions/searches.
"""
import bisect

scores = [100, 200, 250, 400]
pos = bisect.bisect_left(scores, 300)
print(f"{pos=}")  # 3
bisect.insort(scores, 300)
print(scores)  # [100, 200, 250, 300, 400]

# Scheduling and Timeline Management
# Need to insert events in chronological order? Perfect fit.
events = [("09:00", "Breakfast"), ("12:00", "Lunch")]
bisect.insort(events, ("_10:30", "Meeting"))
print(events)
# [('09:00', 'Breakfast'), ('10:30', 'Meeting'), ('12:00', 'Lunch')]

#Efficient Range Queries
#You can quickly find boundaries in sorted data.

numbers = [1, 3, 4, 5, 7, 9, 10, 11]

# Find numbers between 4 and 10 ( including both )
left = bisect.bisect_left(numbers, 4)
right = bisect.bisect_right(numbers, 10)
print(numbers[left:right])  # [4, 5, 7, 9, 10]

# Find numbers between 4 and 10 ( excluding 10 )
left = bisect.bisect_left(numbers, 4)
right = bisect.bisect_right(numbers, 9.9999999)
print(numbers[left:right])  # [4, 5, 7, 9]

# measure performance
import timeit

scores = [i for i in range(0, 1000000)]

start = timeit.default_timer()
bisect.insort(scores, 999999)
time_bisect = timeit.default_timer() - start
print(f"Time taken for bisect: {time_bisect} seconds")

start = timeit.default_timer()
scores.append(999999)
scores.sort()
time_sort = timeit.default_timer() - start
print(f"Time taken for sort: {time_sort} seconds, which is {(time_sort / time_bisect): .2f} times slower", )