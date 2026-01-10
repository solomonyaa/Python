"""
Meeting Module
Defines the Meeting class for the FocusFlow Scheduler API.

Each Meeting object represents a scheduled time slot with:
- Title, start time (HH:MM), and duration (minutes)
- Automatic end time calculation
- Validation to prevent midnight-crossing meetings
- Comparison methods for heap-based sorting by start time
"""

import re
from datetime import datetime, timedelta

time_pattern = re.compile(r'(?:[01]\d|2[0-3]):[0-5]\d')


class Meeting:

    def __init__(self, title, start_time, duration):
        if not isinstance(title, str):
            raise TypeError("Title must be a string")

        if not isinstance(start_time, str) or not time_pattern.fullmatch(start_time):
            raise ValueError(f"Incorrect format of start time: {start_time}")

        if not isinstance(duration, int) or duration <= 0:
            raise ValueError(f"Duration must be a positive integer, got: {duration}")

        self.title = title
        self.start_time = datetime.strptime(start_time, "%H:%M")
        self.end_time = self.start_time + timedelta(minutes=duration)

        if self.end_time.day != self.start_time.day:
            raise ValueError(
                f"Meeting cannot cross midnight. "
                f"Start: {start_time}, Duration: {duration} min"
            )

    def __str__(self):
        return (
            f"Meeting: {self.title}, "
            f"Start: {self.start_time.strftime('%H:%M')}, "
            f"End: {self.end_time.strftime('%H:%M')}"
        )

    def get_title(self):
        return self.title

    def get_start_time(self):
        return self.start_time.strftime("%H:%M")

    def get_end_time(self):
        return self.end_time.strftime("%H:%M")

    def __lt__(self, other):
        if not isinstance(other, Meeting):
            return NotImplemented
        return self.start_time < other.start_time

    def __gt__(self, other):
        if not isinstance(other, Meeting):
            return NotImplemented
        return self.start_time > other.start_time
