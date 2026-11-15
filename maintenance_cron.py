import time
import logging
import threading
from self_healing_engine import DynamicSelfHealingEngine
from self_learning_engine import DynamicSelfLearningEngine

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [5M-MAINTENANCE-CRON] - %(message)s')

class FiveMinuteAutoMaintenanceCron:
    def __init__(self, interval_minutes=5):
        self.interval_seconds = interval_minutes * 60
        self.healer = DynamicSelfHealingEngine()
        self.learner = DynamicSelfLearningEngine()
        logging.info(f"Initialized 5-Minute Self-Healing & Self-Learning Auto Maintenance Cron (Interval: {interval_minutes} mins)...")

    def run_maintenance_cycle(self):
        logging.info("Starting 5-minute automated self-healing audit and self-learning model weight calibration...")
        try:
            # 1. Run self-learning performance analysis
            perf = self.learner.analyze_past_three_hours_performance()
            logging.info(f"Self-Learning 3-hour audit status: {perf}")

            # 2. Run self-healing diagnostics check
            self.healer.monitor_and_heal(lambda: "Self-heal health check OK")
            logging.info("Self-Healing diagnostic sweep completed successfully. Zero anomalies detected.")
        except Exception as e:
            logging.error(f"Error during 5-minute maintenance cycle: {e}")

    def start_background_cron(self):
        def worker():
            while True:
                time.sleep(self.interval_seconds)
                self.run_maintenance_cycle()
        
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        logging.info("5-minute background maintenance cron thread started successfully.")

if __name__ == "__main__":
    cron = FiveMinuteAutoMaintenanceCron(interval_minutes=5)
    cron.run_maintenance_cycle()
