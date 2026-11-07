import logging
from config import APP_ID, INVITATION_CODE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [TELEMETRY] - %(message)s')

class AppTelemetrySync:
    def __init__(self):
        self.app_id = APP_ID
        self.invitation_code = INVITATION_CODE
        logging.info(f"Initialized App Telemetry Sync for App ID: {self.app_id} | Ref Code: {self.invitation_code}")

    def verify_session(self, incoming_app_id):
        if incoming_app_id == self.app_id:
            logging.info(f"Session verified successfully for App ID: {incoming_app_id}")
            return True
        else:
            logging.warning(f"Unauthorized App ID attempt: {incoming_app_id}")
            return False

    def get_telemetry_headers(self):
        return {
            "X-App-ID": self.app_id,
            "X-Invitation-Code": self.invitation_code,
            "X-App-Name": "Robiul-Predictor"
        }

if __name__ == "__main__":
    telemetry = AppTelemetrySync()
    print("Telemetry Headers:", telemetry.get_telemetry_headers())
    print("Session check (2388616):", telemetry.verify_session("2388616"))
