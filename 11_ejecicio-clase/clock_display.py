import unittest
from datetime import datetime

class ClockDisplay:
    def __init__(self, hour=0, minute=0):
        self.set_time(hour, minute)

    def set_time(self, hour, minute):
        if 0 <= hour < 24 and 0 <= minute < 60:
            self.hour = hour
            self.minute = minute
        else:
            raise ValueError("Invalid time values")

    def get_time(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def tick(self):
        self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
            if self.hour == 24:
                self.hour = 0

    def add_minutes(self, minutes):
        if minutes >= 0:
            total_minutes = self.hour * 60 + self.minute + minutes
            self.hour = total_minutes // 60 % 24
            self.minute = total_minutes % 60
        else:
            raise ValueError("Invalid minutes value")

    def is_morning(self):
        return 0 <= self.hour < 12

    def is_evening(self):
        return 12 <= self.hour < 24

    def get_time_with_ampm(self):
        if self.is_morning():
            return f"{self.hour:02d}:{self.minute:02d} AM"
        else:
            return f"{self.hour - 12:02d}:{self.minute:02d} PM"
    
    @classmethod
    def create(cls):
        current_time = datetime.now()
        return cls(current_time.hour, current_time.minute)

    @classmethod
    def create(cls, time_api):
        return time_api.get_current_time_in_chile()