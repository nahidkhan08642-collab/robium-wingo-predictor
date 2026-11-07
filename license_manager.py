import time
import json
import os
import hashlib
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [LICENSE-MANAGER] - %(message)s')

LICENSE_DB_FILE = os.path.join(os.path.dirname(__file__), "license_database.json")

class WingoLicenseManager:
    def __init__(self):
        logging.info("Initializing Multi-Device Activation & License Key Management System...")
        self.licenses = self.load_licenses()

    def load_licenses(self):
        if os.path.exists(LICENSE_DB_FILE):
            try:
                with open(LICENSE_DB_FILE, "r") as f:
                    return json.load(f)
            except Exception:
                pass
        return {}

    def save_licenses(self):
        try:
            with open(LICENSE_DB_FILE, "w") as f:
                json.dump(self.licenses, f, indent=4)
            return True
        except Exception:
            return False

    def generate_license_key(self, owner_name, days_valid=30, max_devices=2):
        """Generates a secure license key bound to max devices."""
        raw_seed = f"{owner_name}-{time.time()}-ROBIUL-KEY"
        key_hash = hashlib.sha256(raw_seed.encode()).hexdigest()[:20].upper()
        formatted_key = f"ROBIUL-{key_hash[:5]}-{key_hash[5:10]}-{key_hash[10:15]}-{key_hash[15:]}"

        self.licenses[formatted_key] = {
            "owner": owner_name,
            "created_at": time.time(),
            "expires_at": time.time() + (days_valid * 24 * 60 * 60),
            "max_devices": max_devices,
            "active_devices": []
        }
        self.save_licenses()
        logging.info(f"Generated new license key for {owner_name}: {formatted_key} (Valid for {days_valid} days, Max Devices: {max_devices})")
        return formatted_key

    def activate_license(self, license_key, device_id):
        """Activates a license key on a specific device, enforcing device limits."""
        if license_key not in self.licenses:
            return {"status": "error", "message": "Invalid License Key!"}

        lic = self.licenses[license_key]

        if time.time() > lic["expires_at"]:
            return {"status": "error", "message": "License Key has expired!"}

        if device_id in lic["active_devices"]:
            return {"status": "success", "message": "Device already activated!"}

        if len(lic["active_devices"]) >= lic["max_devices"]:
            return {"status": "error", "message": f"Device activation limit reached (Max: {lic['max_devices']})!"}

        lic["active_devices"].append(device_id)
        self.save_licenses()
        logging.info(f"License {license_key} activated successfully on device {device_id}.")
        return {"status": "success", "message": "License activated successfully!", "remaining_slots": lic["max_devices"] - len(lic["active_devices"])}

if __name__ == "__main__":
    mgr = WingoLicenseManager()
    test_key = mgr.generate_license_key("RifatVIP", days_valid=30, max_devices=2)
    print("Activation Test:", mgr.activate_license(test_key, "device_termux_01"))
    print("Activation Test 2:", mgr.activate_license(test_key, "device_phone_02"))
    print("Activation Test 3 (Over limit):", mgr.activate_license(test_key, "device_tablet_03"))
