import os
import requests
import subprocess

def push_code():
    app_dir = "/data/data/com.termux/files/home/robium_predictor_app"
    os.chdir(app_dir)
    
    # Remove push_to_github.py from git tracking to prevent secret scanning block
    if os.path.exists("push_to_github.py"):
        os.remove("push_to_github.py")
    
    commands = [
        "git add .",
        "git commit --amend -m 'Initial commit: Robiul Predictor V2 standalone app'",
        "git push -u origin main --force"
    ]
    
    for cmd in commands:
        print(f"Running: {cmd}")
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(res.stdout)
        print(res.stderr)

if __name__ == "__main__":
    push_code()
