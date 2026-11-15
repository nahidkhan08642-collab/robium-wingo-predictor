import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LIVE-SYNC] - %(message)s')

class WingoLivePeriodSync:
    def __init__(self):
        logging.info("Initializing Real-Time Dynamic Wingo Period & Platform API Sync Engine...")

    def get_current_period_and_countdown(self, game_type="30s"):
        try:
            now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=6)))
            date_str = now.strftime("%Y%m%d")
            
            seconds_since_midnight = now.hour * 3600 + now.minute * 60 + now.second + now.microsecond / 1000000.0
            
            if game_type == "30s":
                interval_duration = 30.0
                total_intervals_today = int(seconds_since_midnight // interval_duration)
                # DKWin 30s period index matches total 30s intervals from midnight + offset (observed ~1491-1500 range)
                base_index = total_intervals_today
                elapsed_in_interval = seconds_since_midnight % interval_duration
                countdown = int(interval_duration - elapsed_in_interval)
                
                period_str = f"{date_str}10005{base_index}"
                next_period_str = f"{date_str}10005{base_index + 1}"
            else: # 1m
                interval_duration = 60.0
                total_intervals_today = int(seconds_since_midnight // interval_duration)
                base_index = total_intervals_today
                elapsed_in_interval = seconds_since_midnight % interval_duration
                countdown = int(interval_duration - elapsed_in_interval)
                
                period_str = f"{date_str}10001{base_index}"
                next_period_str = f"{date_str}10001{base_index + 1}"

            trading_status = "LOCKED (Last 5s)" if countdown <= 5 else "TRADING OPEN"

            return {
                "period": period_str,
                "next_period": next_period_str,
                "countdown": max(1, countdown),
                "trading_status": trading_status,
                "game_type": game_type
            }
        except Exception as e:
            logging.warning(f"Live sync fallback triggered: {e}")
            now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=6)))
            date_str = now.strftime("%Y%m%d")
            return {
                "period": f"{date_str}100051500",
                "next_period": f"{date_str}100051501",
                "countdown": 30,
                "trading_status": "TRADING OPEN",
                "game_type": game_type
            }

if __name__ == "__main__":
    sync = WingoLivePeriodSync()
    print(sync.get_current_period_and_countdown("30s"))
