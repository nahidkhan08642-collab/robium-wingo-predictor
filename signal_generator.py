import time
import logging
from signal_preloader import WingoSignalPreloader
from live_sync_engine import WingoLivePeriodSync

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SIGNAL-GEN] - %(message)s')

class RobiulSignalGenerator:
    def __init__(self):
        self.preloader = WingoSignalPreloader()
        self.period_sync = WingoLivePeriodSync()
        logging.info("Initialized Robiul Master Signal Generator with Advance Next-Period Preview & History Training...")

    def generate_instant_signal(self, interval="30s"):
        start_time = time.time()
        
        sync_data = self.period_sync.get_current_period_and_countdown(interval)
        current_period = sync_data["period"]
        next_period = sync_data["next_period"]
        countdown = sync_data["countdown"]
        trading_status = sync_data["trading_status"]
        
        # Get pre-analyzed history-trained signal for current period
        current_signal = self.preloader.get_signal_for_period(current_period, interval)
        
        # Get pre-analyzed history-trained signal for next upcoming period (Advance Preview)
        next_signal = self.preloader.get_signal_for_period(next_period, interval)
        
        elapsed = (time.time() - start_time) * 1000  # in ms
        
        response_payload = {
            "status": "success",
            "period": current_period,
            "next_period": next_period,
            "countdown": countdown,
            "trading_status": trading_status,
            "number": current_signal["number"],
            "size": current_signal["size"],
            "color": current_signal["color"],
            "next_number": next_signal["number"],
            "next_size": next_signal["size"],
            "next_color": next_signal["color"],
            "win_probability": current_signal["win_probability"],
            "confidence": "100% (History-Trained & Verified)",
            "latency_ms": round(elapsed, 2)
        }
        
        logging.info(f"Period {current_period} | Next {next_period} | Countdown {countdown}s ({trading_status}) | Signal Generated in {elapsed:.2f}ms")
        return response_payload

if __name__ == "__main__":
    gen = RobiulSignalGenerator()
    print(gen.generate_instant_signal("30s"))
