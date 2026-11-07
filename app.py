import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, render_template, request, jsonify
import config
from config import save_config, load_config

app = Flask(__name__)

BLOCKED_USERS = []

@app.route('/')
def index():
    cfg = load_config()
    reg_url = f"{cfg.get('TARGET_PLATFORM', 'https://dkwin9.com')}/#/register?invitationCode={cfg.get('INVITATION_CODE', '787222388616')}"
    return render_template('index.html', reg_url=reg_url)

@app.route('/api/auth', methods=['POST'])
def api_auth():
    data = request.json or {}
    password = data.get('password', '').strip()
    device_id = data.get('device_id', 'default_device')

    if device_id in BLOCKED_USERS:
        return jsonify({"status": "error", "message": "Device is blocked by Admin!"}), 403

    cfg = load_config()
    
    # Strict Admin Password security: ONLY Robiul25890 and Robiulislam25890 give admin access
    admin_passwords = ["Robiul25890", "Robiulislam25890"]
    normal_passwords = [cfg.get('NORMAL_PASS', 'RRRR'), "RRRR"]

    if password in admin_passwords:
        return jsonify({"status": "success", "redirect": "admin"})
    elif password in normal_passwords:
        return jsonify({"status": "success", "redirect": "dashboard"})
    else:
        return jsonify({"status": "error", "message": "Invalid Password! Access Denied."}), 401

@app.route('/api/signal', methods=['POST'])
def api_signal():
    from signal_generator import RobiulSignalGenerator as WingoSignalGenerator
    generator = WingoSignalGenerator()
    data = request.json or {}
    interval = data.get('interval', '30s')
    signal = generator.generate_instant_signal(interval=interval)
    return jsonify(signal)

@app.route('/api/admin/update-config', methods=['POST'])
def api_update_config():
    data = request.json or {}
    target_platform = data.get('target_platform', '').strip()
    invitation_code = data.get('invitation_code', '').strip()
    admin_pass = data.get('admin_pass', '').strip()
    normal_pass = data.get('normal_pass', '').strip()

    cfg = load_config()
    if target_platform:
        cfg['TARGET_PLATFORM'] = target_platform
    if invitation_code:
        cfg['INVITATION_CODE'] = invitation_code
    if admin_pass:
        cfg['ADMIN_PASS'] = admin_pass
    if normal_pass:
        cfg['NORMAL_PASS'] = normal_pass

    if save_config(cfg):
        return jsonify({"status": "success", "message": "Link & Passwords updated successfully!"})
    else:
        return jsonify({"status": "error", "message": "Failed to save configuration."}), 500

@app.route('/api/admin/block-user', methods=['POST'])
def api_block_user():
    data = request.json or {}
    target = data.get('target', '').strip()
    if target and target not in BLOCKED_USERS:
        BLOCKED_USERS.append(target)
    return jsonify({"status": "success", "message": f"User {target} blocked successfully!", "blocked_list": BLOCKED_USERS})

@app.route('/api/admin/unblock-user', methods=['POST'])
def api_unblock_user():
    data = request.json or {}
    target = data.get('target', '').strip()
    if target in BLOCKED_USERS:
        BLOCKED_USERS.remove(target)
    return jsonify({"status": "success", "message": f"User {target} unblocked successfully!", "blocked_list": BLOCKED_USERS})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
