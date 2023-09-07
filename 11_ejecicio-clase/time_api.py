import requests
from datetime import datetime
from clock_display import ClockDisplay

class ChileTimeAPI:
    def fetch_time_data(self):
        try:
            response = requests.get("http://worldtimeapi.org/api/timezone/America/Santiago")
            if response.status_code == 200:
                return response.json()
            else:
                raise Exception("Failed to fetch time from API")
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_current_time_in_chile(self):
        data = self.fetch_time_data()
        if data is not None:
            chile_time = datetime.fromisoformat(data["datetime"])
            return ClockDisplay(chile_time.hour, chile_time.minute)
        return None
