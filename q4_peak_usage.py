from datetime import datetime
from collections import Counter


def find_peak_usage(logs):
    hour_counts = Counter()

    for log in logs:
        dt = datetime.fromisoformat(log)
        hour_counts[dt.hour] += 1

    max_count = max(hour_counts.values())
    peak_hours = [hour for hour, count in hour_counts.items() if count == max_count]

    return min(peak_hours)


# Quick test to see it work
sample_logs = [
    "2026-08-04T13:21:18",
    "2026-08-04T13:45:02",
    "2026-08-04T09:10:00",
    "2026-08-04T13:59:59",
    "2026-08-04T09:30:00",
]

print(find_peak_usage(sample_logs))