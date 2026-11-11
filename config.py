# ==========================================
# "Robiul" App Configuration & Referral Hardcoding (Dynamic State)
# ==========================================

import os
import json

CONFIG_STATE_FILE = os.path.join(os.path.dirname(__file__), "config_state.json")

# Default Values
DEFAULT_CONFIG = {
    "APP_NAME": "Robiul predictor001",
    "TARGET_PLATFORM": "https://dkwin9.com",
    "INVITATION_CODE": "787222388616",
    "APP_ID": "2388616",
    "ADMIN_PASS": "Robiulislam25890",
    "NORMAL_PASS": "RRRR",
    "TRIAL_DAYS_LIMIT": 7
}

def load_config():
    if os.path.exists(CONFIG_STATE_FILE):
        try:
            with open(CONFIG_STATE_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    # Initialize state file if missing
    save_config(DEFAULT_CONFIG)
    return DEFAULT_CONFIG.copy()

def save_config(new_config):
    try:
        with open(CONFIG_STATE_FILE, "w") as f:
            json.dump(new_config, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False

# Load current active config
_cfg = load_config()

APP_NAME = _cfg.get("APP_NAME", DEFAULT_CONFIG["APP_NAME"])
TARGET_PLATFORM = _cfg.get("TARGET_PLATFORM", DEFAULT_CONFIG["TARGET_PLATFORM"])
INVITATION_CODE = _cfg.get("INVITATION_CODE", DEFAULT_CONFIG["INVITATION_CODE"])
APP_ID = _cfg.get("APP_ID", DEFAULT_CONFIG["APP_ID"])
REGISTRATION_URL = f"{TARGET_PLATFORM}/#/register?invitationCode={INVITATION_CODE}"

ADMIN_PASS = _cfg.get("ADMIN_PASS", DEFAULT_CONFIG["ADMIN_PASS"])
NORMAL_PASS = _cfg.get("NORMAL_PASS", DEFAULT_CONFIG["NORMAL_PASS"])
TRIAL_DAYS_LIMIT = _cfg.get("TRIAL_DAYS_LIMIT", DEFAULT_CONFIG["TRIAL_DAYS_LIMIT"])

# Prediction Priorities
PRIORITY_TARGET_1 = "EXACT_NUMBER_0_9"
PRIORITY_TARGET_2 = "BIG_SMALL_SIZE"
PRIORITY_TARGET_3 = "COLOR_RGB"
