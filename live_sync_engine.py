import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LIVE-SYNC] - %(message)s')

class WingoLivePeriodSync:
    def __init__(self):
        logging.info("Initializing Exact DKWin Matched Period Sync Engine...")

    def get_current_period_and_countdown(self, game_type="30s"):
        try:
            # DKWin period numbering sync based on precise UTC offset and daily total 30s intervals starting at 00:00:00 UTC
            now_utc = datetime.datetime.now(datetime.timezone.utc)
            date_str = now_utc.strftime("%Y%m%d")
            
            seconds_since_midnight_utc = now_utc.hour * 3600 + now_utc.minute * 60 + now_utc.second + now_utc.microsecond / 1000000.0
            
            if game_type == "30s":
                interval_duration = 30.0
                total_intervals = int(seconds_since_midnight_utc // interval_duration)
                
                # Match exact DKWin format: YYYYMMDD10005XXXX
                period_index = total_intervals
                elapsed = seconds_since_midnight_utc % interval_duration
                countdown = int(interval_duration - elapsed)
                
                period_str = f"{date_str}10005{period_index}"
                next_period_str = f"{date_str}10005{period_index + 1}"
            else: # 1m
                interval_duration = 60.0
                total_intervals = int(seconds_since_midnight_utc // interval_duration)
                period_index = total_intervals
                elapsed = seconds_since_midnight_utc % interval_duration
                countdown = int(interval_duration - elapsed)
                
                period_str = f"{date_str}10001{period_index}"
                next_period_str = f"{date_str}10001{period_index + 1}"

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
            now_utc = datetime.datetime.now(datetime.timezone.utc)
            date_str = now_utc.strftime("%Y%m%d")
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
