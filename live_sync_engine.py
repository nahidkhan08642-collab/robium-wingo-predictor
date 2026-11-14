import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LIVE-SYNC] - %(message)s')

class WingoLivePeriodSync:
    def __init__(self):
        logging.info("Initializing Precision Synchronized Wingo Period & Countdown Engine...")

    def get_current_period_and_countdown(self, game_type="30s"):
        # Use precise local time (Bangladesh UTC+6)
        now = datetime.datetime.utcnow() + datetime.timedelta(hours=6)
        date_str = now.strftime("%Y%m%d")
        
        seconds_since_midnight = now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1000000.0
        
        if game_type == "30s":
            interval_duration = 30.0
            # Precise synced base index at midnight (721) + elapsed intervals today
            base_index = 721 + int(seconds_since_midnight // interval_duration)
            elapsed_in_interval = seconds_since_midnight % interval_duration
            countdown = int(interval_duration - elapsed_in_interval)
            
            period_str = f"{date_str}10005{base_index:04d}"
            next_period_str = f"{date_str}10005{base_index + 1:04d}"
        else: # 1m
            interval_duration = 60.0
            base_index = 361 + int(seconds_since_midnight // interval_duration)
            elapsed_in_interval = seconds_since_midnight % interval_duration
            countdown = int(interval_duration - elapsed_in_interval)
            
            period_str = f"{date_str}10001{base_index:04d}"
            next_period_str = f"{date_str}10001{base_index + 1:04d}"

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
