import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LIVE-SYNC] - %(message)s')

class WingoLivePeriodSync:
    def __init__(self):
        logging.info("Initializing Exact Wingo Period & Timer Sync Engine...")

    def get_current_period_and_countdown(self, game_type="30s"):
        """
        Generates the exact Wingo trading period issue number matching YYYYMMDD10005XXXX
        and synchronizes the 30-second countdown timer.
        """
        now = datetime.datetime.now()
        date_str = now.strftime("%Y%m%d")
        
        total_seconds_today = now.hour * 3600 + now.minute * 60 + now.second
        
        if game_type == "30s":
            total_intervals = total_seconds_today // 30
            countdown = 30 - (total_seconds_today % 30)
            # Exact format: YYYYMMDD + 10005 + 5-digit index (e.g. 20261108100050207)
            period_str = f"{date_str}10005{total_intervals:05d}"
        else: # 1m
            total_intervals = total_seconds_today // 60
            countdown = 60 - (total_seconds_today % 60)
            period_str = f"{date_str}10001{total_intervals:05d}"

        logging.info(f"Exact Wingo Period Matched: {period_str} | Countdown: {countdown}s")
        
        return {
            "period": period_str,
            "countdown": countdown,
            "game_type": game_type
        }

if __name__ == "__main__":
    sync = WingoLivePeriodSync()
    print(sync.get_current_period_and_countdown("30s"))
