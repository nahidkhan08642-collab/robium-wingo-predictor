import requests
import logging
import time
from config import TARGET_PLATFORM

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LIVE-API-HOOK] - %(message)s')

class WingoLiveApiHook:
    def __init__(self, target_url=TARGET_PLATFORM):
        self.target_url = target_url
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Linux; Android 12; Mobile) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36",
            "Referer": f"{target_url}/",
            "Accept": "application/json, text/plain, */*"
        })

    def fetch_live_game_data(self, game_type="30s"):
        """
        Hooks into target platform live game API endpoint to fetch current round period and recent history.
        Falls back gracefully if network or firewall blocks direct socket access.
        """
        api_endpoint = f"{self.target_url}/api/web/getData"
        payload = {"typeId": 1 if game_type == "30s" else 2, "pageNo": 1, "pageSize": 10}
        
        try:
            logging.info(f"Connecting to target platform live socket/API: {api_endpoint} for {game_type}...")
            response = self.session.post(api_endpoint, json=payload, timeout=3)
            if response.status_code == 200:
                data = response.json()
                logging.info("Live API hook connected successfully! Live data retrieved.")
                return {"status": "live", "data": data}
            else:
                logging.warning(f"Live API responded with status {response.status_code}. Using sync fallback.")
                return {"status": "fallback", "message": f"HTTP {response.status_code}"}
        except Exception as e:
            logging.warning(f"Live API connection intercepted/blocked: {e}. Operating on secure local sync mode.")
            return {"status": "offline_sync", "message": str(e)}

if __name__ == "__main__":
    hook = WingoLiveApiHook()
    print(hook.fetch_live_game_data("30s"))
