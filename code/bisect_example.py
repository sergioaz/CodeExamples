import bisect

scores = [100, 200, 250, 400]
bisect.insort(scores, 300)
print(scores)  # [100, 200, 250, 300, 400]

events = [("09:00", "Breakfast"), ("12:00", "Lunch")]
bisect.insort(events, ("_10:30", "Meeting"))
print(events)
# [('09:00', 'Breakfast'), ('10:30', 'Meeting'), ('12:00', 'Lunch')]