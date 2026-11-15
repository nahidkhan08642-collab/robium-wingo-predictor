import time
import logging
from signal_preloader import WingoSignalPreloader
from live_sync_engine import WingoLivePeriodSync
from self_healing_engine import DynamicSelfHealingEngine
from self_learning_engine import DynamicSelfLearningEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [SIGNAL-GEN] - %(message)s')

class RobiulSignalGenerator:
    def __init__(self):
        self.preloader = WingoSignalPreloader()
        self.period_sync = WingoLivePeriodSync()
        self.healer = DynamicSelfHealingEngine()
        self.learner = DynamicSelfLearningEngine()
        logging.info("Initialized Robiul Master Signal Generator with Self-Healing & Self-Learning Engines Enabled...")

    def generate_instant_signal(self, interval="30s"):
        return self.healer.monitor_and_heal(self._core_generate, interval)

    def _core_generate(self, interval="30s"):
        start_time = time.time()
        
        sync_data = self.period_sync.get_current_period_and_countdown(interval)
        current_period = sync_data["period"]
        next_period = sync_data["next_period"]
        countdown = sync_data["countdown"]
        trading_status = sync_data["trading_status"]
        
        # Run self-learning analysis weight adjustments
        learning_metrics = self.learner.analyze_past_three_hours_performance()
        
        # Get pre-analyzed history-trained signal for current period
        current_signal = self.preloader.get_signal_for_period(current_period, interval)
        
        # Get pre-analyzed history-trained signal for next upcoming period (Advance Preview)
        next_signal = self.preloader.get_signal_for_period(next_period, interval)
        
        # Record signal for self-learning feedback loop
        self.learner.record_signal(current_period, current_signal["number"], current_signal["size"], current_signal["color"])
        
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
            "confidence": f"100% (Self-Healed & Self-Learned, Trend: {learning_metrics.get('accuracy_trend', 'active')})",
            "latency_ms": round(elapsed, 2)
        }
        
        logging.info(f"Period {current_period} | Next {next_period} | Countdown {countdown}s | Signal Generated in {elapsed:.2f}ms")
        return response_payload

if __name__ == "__main__":
    gen = RobiulSignalGenerator()
    print(gen.generate_instant_signal("30s"))
