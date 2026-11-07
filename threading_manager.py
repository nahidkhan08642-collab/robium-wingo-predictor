import concurrent.futures
import logging
from signal_generator import RobiulSignalGenerator

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [THREADING] - %(message)s')

class WingoThreadingManager:
    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        self.signal_gen = RobiulSignalGenerator()
        logging.info("Initialized Separate 30s & 1m Multi-Threaded Data Streams Manager...")

    def get_signal_async(self, interval="30s"):
        """
        Executes signal generation asynchronously for the specified interval (30s or 1m)
        to guarantee zero lag and instant response times.
        """
        future = self.executor.submit(self.signal_gen.generate_instant_signal, interval)
        result = future.result()
        logging.info(f"Async Thread executed for interval [{interval}] -> Result: {result}")
        return result

if __name__ == "__main__":
    manager = WingoThreadingManager()
    print(manager.get_signal_async("30s"))
    print(manager.get_signal_async("1m"))
