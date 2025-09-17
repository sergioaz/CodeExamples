def merge_intervals(intervals):
    # Sort intervals by the start time
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        # If merged is empty or current interval does not overlap with the last one
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Merge the intervals
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Example usage
intervals = [[15, 18], [8, 10],[1, 3], [2, 6] ]
result = merge_intervals(intervals)
print(result)  # Output: [[1, 6], [8, 10], [15, 18]]