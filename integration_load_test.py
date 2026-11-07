import time
import requests
import concurrent.futures
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LOAD-TEST] - %(message)s')

BASE_URL = "http://127.0.0.1:5000"

def test_auth_endpoint():
    start = time.time()
    res = requests.post(f"{BASE_URL}/api/auth", json={"password": "RRRR", "device_id": "test_device"})
    latency = (time.time() - start) * 1000
    return res.status_code == 200, latency

def test_signal_endpoint():
    start = time.time()
    res = requests.post(f"{BASE_URL}/api/signal", json={"interval": "30s"})
    latency = (time.time() - start) * 1000
    return res.status_code == 200 and res.json().get("status") == "success", latency

def run_load_test():
    logging.info("Starting Step 23: Full Project Integration & Load Testing...")
    
    total_requests = 50
    success_count = 0
    latencies = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(test_signal_endpoint) for _ in range(total_requests)]
        for future in concurrent.futures.as_completed(futures):
            success, latency = future.result()
            if success:
                success_count += 1
            latencies.append(latency)

    avg_latency = sum(latencies) / len(latencies) if latencies else 0
    logging.info(f"Load Test Completed! Total Requests: {total_requests}, Success: {success_count}, Avg Latency: {avg_latency:.2f} ms")
    
    assert success_count == total_requests, "Load test had failing requests!"
    print("[SUCCESS] Step 23: Full Project Integration & Load Testing Passed Successfully!")

if __name__ == "__main__":
    run_load_test()
