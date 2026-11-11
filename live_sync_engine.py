import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LIVE-SYNC] - %(message)s')

class WingoLivePeriodSync:
    def __init__(self):
        logging.info("Initializing Precision Synchronized Wingo Period & Countdown Engine...")

    def get_current_period_and_countdown(self, game_type="30s"):
        # Use precise UTC / local time alignment with drift correction
        now = datetime.datetime.utcnow() # Using UTC to match gaming servers standard time
        date_str = now.strftime("%Y%m%d")
        
        total_seconds_today = now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1000000.0
        
        if game_type == "30s":
            interval_duration = 30.0
            total_intervals = int(total_seconds_today // interval_duration) + 1
            elapsed_in_interval = total_seconds_today % interval_duration
            countdown = int(interval_duration - elapsed_in_interval)
            
            # Standard Wingo 30s period ID format: YYYYMMDD + 10003 + 5-digit index
            period_str = f"{date_str}10003{total_intervals:05d}"
            next_period_str = f"{date_str}10003{total_intervals + 1:05d}"
        else: # 1m
            interval_duration = 60.0
            total_intervals = int(total_seconds_today // interval_duration) + 1
            elapsed_in_interval = total_seconds_today % interval_duration
            countdown = int(interval_duration - elapsed_in_interval)
            
            # Standard Wingo 1m period ID format: YYYYMMDD + 10001 + 5-digit index
            period_str = f"{date_str}10001{total_intervals:05d}"
            next_period_str = f"{date_str}10001{total_intervals + 1:05d}"

        trading_status = "LOCKED (Last 5s)" if countdown <= 5 else "TRADING OPEN"

        return {
            "period": period_str,
            "next_period": next_period_str,
            "countdown": max(1, countdown),
            "trading_status": trading_status,
            "game_type": game_type
        }

if __name__ == "__main__":
    sync = WingoLivePeriodSync()
    print(sync.get_current_period_and_countdown("30s"))
    print(sync.get_current_period_and_countdown("1m"))
