import os
import subprocess
from PIL import Image, ImageDraw, ImageFont

def make_video():
    frames_dir = os.path.expanduser("~/robium_frames")
    os.makedirs(frames_dir, exist_ok=True)
    
    width, height = 720, 1280  # 9:16 vertical video format (Phone screen size)
    
    # Colors
    bg_color = (10, 15, 30)
    card_color = (20, 30, 50)
    cyan_color = (6, 182, 212)
    amber_color = (245, 158, 11)
    green_color = (16, 185, 129)
    white_color = (255, 255, 255)
    gray_color = (148, 163, 184)

    def draw_base_screen(title):
        im = Image.new("RGB", (width, height), bg_color)
        draw = ImageDraw.Draw(im)
        # Header bar
        draw.rectangle([0, 0, width, 100], fill=(15, 23, 42))
        draw.text((50, 35), title, fill=cyan_color)
        return im, draw

    # Generate sequence of frames (e.g. 90 frames for 3 seconds per screen at 30 fps)
    frame_count = 0

    # Scene 1: Lock Screen (Frames 0 to 45)
    for i in range(45):
        im, draw = draw_base_screen("ROBIUL PREDICTOR V2 - LOCK SCREEN")
        draw.rounded_rectangle([60, 250, width-60, 950], radius=30, fill=card_color, outline=cyan_color, width=3)
        draw.text((150, 350), "👑 ROBIUL ISLAM", fill=amber_color)
        draw.text((180, 420), "SECURE ACCESS GATEWAY", fill=white_color)
        
        # Password box
        draw.rounded_rectangle([100, 550, width-100, 670], radius=15, fill=(10, 15, 30), outline=gray_color, width=2)
        draw.text((130, 590), "Password: RRRR", fill=gray_color)
        
        # Unlock button
        draw.rounded_rectangle([100, 750, width-100, 870], radius=15, fill=cyan_color)
        draw.text((260, 790), "UNLOCK APP", fill=white_color)
        
        frame_path = os.path.join(frames_dir, f"frame_{frame_count:04d}.png")
        im.save(frame_path)
        frame_count += 1

    # Scene 2: Dashboard Signal Generation (Frames 46 to 90)
    for i in range(45):
        im, draw = draw_base_screen("LIVE 30s PREDICTION DASHBOARD")
        draw.rounded_rectangle([40, 150, width-40, 1150], radius=30, fill=card_color, outline=cyan_color, width=2)
        
        draw.text((80, 200), "Period: 2026110510015", fill=gray_color)
        draw.text((width-220, 200), "Countdown: 18s", fill=amber_color)
        
        # LED & Prob Header
        draw.ellipse([80, 280, 105, 305], fill=green_color)
        draw.text((120, 280), "AI Model: Stable (10 Models)", fill=green_color)
        draw.text((width-240, 280), "Win Prob: 97.2%", fill=amber_color)
        
        # Result Box
        draw.rounded_rectangle([80, 350, width-80, 650], radius=20, fill=(10, 15, 30), outline=amber_color, width=3)
        draw.text((220, 390), "🎯 EXACT NUMBER TARGET", fill=gray_color)
        draw.text((320, 470), "7", fill=amber_color)
        draw.text((230, 570), "🟢 GREEN • BIG SIZE", fill=green_color)
        
        # Button
        draw.rounded_rectangle([80, 800, width-80, 920], radius=20, fill=cyan_color)
        draw.text((200, 845), "⚡ GET INSTANT SIGNAL", fill=white_color)
        
        frame_path = os.path.join(frames_dir, f"frame_{frame_count:04d}.png")
        im.save(frame_path)
        frame_count += 1

    # Scene 3: Admin Panel (Frames 91 to 135)
    for i in range(45):
        im, draw = draw_base_screen("ADMIN MASTER PANEL")
        draw.rounded_rectangle([40, 150, width-40, 1150], radius=30, fill=card_color, outline=amber_color, width=2)
        
        draw.text((80, 220), "🛠️ LINK & ACCOUNT MANAGEMENT", fill=amber_color)
        
        draw.text((80, 320), "Target Platform URL:", fill=gray_color)
        draw.rounded_rectangle([80, 360, width-80, 460], radius=12, fill=(10, 15, 30), outline=gray_color)
        draw.text((110, 395), "https://dkwin9.com", fill=white_color)
        
        draw.text((80, 520), "Invitation / Referral Code:", fill=gray_color)
        draw.rounded_rectangle([80, 560, width-80, 660], radius=12, fill=(10, 15, 30), outline=gray_color)
        draw.text((110, 595), "787222388616", fill=white_color)
        
        draw.rounded_rectangle([80, 800, width-80, 920], radius=20, fill=cyan_color)
        draw.text((120, 845), "UPDATE LINK & PASSWORDS", fill=white_color)
        
        frame_path = os.path.join(frames_dir, f"frame_{frame_count:04d}.png")
        im.save(frame_path)
        frame_count += 1

    video_path = os.path.expanduser("~/robium_predictor_demo.mp4")
    
    # Run ffmpeg to generate mp4
    cmd = [
        "ffmpeg", "-y", "-framerate", "15", "-i", os.path.join(frames_dir, "frame_%04d.png"),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", video_path
    ]
    subprocess.run(cmd, check=True)
    print(f"MP4 Video generated successfully at: {video_path}")

if __name__ == "__main__":
    make_video()
