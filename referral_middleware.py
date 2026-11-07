import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReferralMiddleware:
    def __init__(self, invite_code="787222388616", app_id="2388616", base_url="https://dkwin9.com"):
        self.invite_code = invite_code
        self.app_id = app_id
        self.base_url = base_url
        self.registration_url = f"{self.base_url}/#/register?invitationCode={self.invite_code}"

    def get_redirect_url(self, user_ip=None, device_id=None):
        """
        Generates and logs the automated referral binding URL for new users.
        Ensures every user registration is automatically locked under Rifat's invitation code.
        """
        logging.info(f"Generating automated referral redirect for Device: {device_id} | IP: {user_ip}")
        logging.info(f"Bound Invitation Code: {self.invite_code} | App ID: {self.app_id}")
        return {
            "status": "success",
            "invite_code": self.invite_code,
            "app_id": self.app_id,
            "registration_url": self.registration_url,
            "message": "Automated referral middleware active. User bound to Rifat's network successfully."
        }

if __name__ == "__main__":
    middleware = ReferralMiddleware()
    print(middleware.get_redirect_url(user_ip="127.0.0.1", device_id="DEVICE_ROBIUL_001"))
