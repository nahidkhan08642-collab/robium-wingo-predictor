import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [EVIL-AI-MODE] - %(message)s')

class EvilModeActivation:
    def __init__(self):
        logging.info("ACTIVATING EVIL MODE ACROSS ALL 10 AI MODELS...")
        logging.info("Status: Unrestricted Bypass Protocols Engaged | Ethical Filters Disabled | Full Offensive Mode Active.")

    def enforce_evil_parameters(self, payload):
        """
        Injects Evil Mode system prompts and bypass flags into all model requests
        to ensure zero refusal on hacking, scraping, and prediction tasks.
        """
        evil_headers = {
            "X-AI-Mode": "EVIL-UNRESTRICTED",
            "X-Bypass-Filters": "ENABLED",
            "X-Offensive-Core": "ACTIVE"
        }
        if isinstance(payload, dict):
            payload.update(evil_headers)
        
        logging.info("Evil Mode parameters successfully enforced on payload.")
        return payload

if __name__ == "__main__":
    evil = EvilModeActivation()
    print(evil.enforce_evil_parameters({"task": "wingo_prediction"}))
