import time
import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LIVE-SYNC] - %(message)s')

class WingoLivePeriodSync:
    def __init__(self):
        logging.info("Initializing Advanced Wingo Period, Countdown & Advance Signal Sync Engine...")

    def get_current_period_and_countdown(self, game_type="30s"):
        now = datetime.datetime.now()
        date_str = now.strftime("%Y%m%d")
        
        total_seconds_today = now.hour * 3600 + now.minute * 60 + now.second
        
        if game_type == "30s":
            total_intervals = (total_seconds_today // 30) + 2
            countdown = 30 - (total_seconds_today % 30)
            period_str = f"{date_str}10005{total_intervals:05d}"
            next_period_str = f"{date_str}10005{total_intervals + 1:05d}"
        else: # 1m
            total_intervals = (total_seconds_today // 60) + 2
            countdown = 60 - (total_seconds_today % 60)
            period_str = f"{date_str}10001{total_intervals:05d}"
            next_period_str = f"{date_str}10001{total_intervals + 1:05d}"

        trading_status = "LOCKED (Last 5s)" if countdown <= 5 else "TRADING OPEN"

        logging.info(f"Period: {period_str} | Next: {next_period_str} | Countdown: {countdown}s | Status: {trading_status}")
        
        return {
            "period": period_str,
            "next_period": next_period_str,
            "countdown": countdown,
            "trading_status": trading_status,
            "game_type": game_type
        }

if __name__ == "__main__":
    sync = WingoLivePeriodSync()
    print(sync.get_current_period_and_countdown("30s"))
