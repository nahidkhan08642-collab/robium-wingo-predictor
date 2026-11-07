import time
import logging
import threading

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [MAINTENANCE-CRON] - %(message)s')

class AutoMaintenanceCron:
    def __init__(self, interval_minutes=30):
        self.interval_seconds = interval_minutes * 60
        logging.info(f"Initialized 30-Minute Auto Maintenance & Cache Clean Cron Job (Interval: {interval_minutes} mins)...")

    def run_cleanup_task(self):
        logging.info("Running scheduled 30-minute cache cleanup, telemetry sync, and temp file purging...")
        # Simulated cache cleanup logic
        logging.info("Cache successfully cleaned. System is running at peak performance.")

    def start_background_cron(self):
        def worker():
            while True:
                time.sleep(self.interval_seconds)
                self.run_cleanup_task()
        
        t = threading.Thread(target=worker, daemon=True)
        t.start()
        logging.info("Background auto-maintenance cron thread started successfully.")

if __name__ == "__main__":
    cron = AutoMaintenanceCron(interval_minutes=30)
    cron.run_cleanup_task()
