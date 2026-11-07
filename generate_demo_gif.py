import os
from PIL import Image, ImageDraw, ImageFont

def generate_demo():
    frames = []
    width, height = 400, 700
    
    # Colors
    bg_color = (15, 23, 42)      # Dark slate
    card_color = (30, 41, 59)    # Slate 800
    cyan_color = (6, 182, 212)   # Cyan 500
    amber_color = (245, 158, 11) # Amber 500
    green_color = (16, 185, 129) # Emerald 500
    white_color = (255, 255, 255)
    gray_color = (148, 163, 184)

    # Frame 1: Lock Screen
    im1 = Image.new("RGB", (width, height), bg_color)
    draw1 = ImageDraw.Draw(im1)
    draw1.rectangle([30, 150, 370, 550], fill=card_color, outline=cyan_color, width=2)
    draw1.text((120, 180), "ROBIUL PREDICTOR", fill=cyan_color)
    draw1.text((140, 220), "👑 ROBIUL ISLAM", fill=amber_color)
    draw1.rectangle([60, 320, 340, 380], fill=(15, 23, 42), outline=gray_color)
    draw1.text((80, 340), "Enter Password: RRRR", fill=gray_color)
    draw1.rectangle([60, 420, 340, 480], fill=cyan_color)
    draw1.text((150, 440), "UNLOCK", fill=white_color)
    frames.append(im1)

    # Frame 2: Dashboard (Signal Generated)
    im2 = Image.new("RGB", (width, height), bg_color)
    draw2 = ImageDraw.Draw(im2)
    draw2.rectangle([20, 20, 380, 680], fill=card_color, outline=cyan_color, width=1)
    draw2.text((40, 40), "⚡ ROBIUL PREDICTOR V2", fill=cyan_color)
    draw2.text((40, 70), "Period: 2026110510012", fill=gray_color)
    # LED & Prob
    draw2.ellipse([40, 110, 52, 122], fill=green_color)
    draw2.text((60, 107), "AI Model: Stable", fill=green_color)
    draw2.text((260, 107), "Win Prob: 96.4%", fill=amber_color)
    # Result Box
    draw2.rectangle([40, 150, 360, 300], fill=(15, 23, 42), outline=amber_color, width=2)
    draw2.text((160, 170), "EXACT NUMBER", fill=gray_color)
    draw2.text((170, 210), "9", fill=amber_color) # large text simulated
    draw2.text((130, 260), "GREEN • BIG", fill=green_color)
    # Button
    draw2.rectangle([40, 340, 360, 400], fill=cyan_color)
    draw2.text((115, 360), "GET LIVE SIGNAL", fill=white_color)
    frames.append(im2)

    # Frame 3: Admin Panel (Link & Password Management)
    im3 = Image.new("RGB", (width, height), bg_color)
    draw3 = ImageDraw.Draw(im3)
    draw3.rectangle([20, 20, 380, 680], fill=card_color, outline=amber_color, width=1)
    draw3.text((40, 40), "🛠️ ADMIN MASTER PANEL", fill=amber_color)
    draw3.text((40, 80), "Target Wingo URL:", fill=gray_color)
    draw3.rectangle([40, 105, 360, 145], fill=(15, 23, 42), outline=gray_color)
    draw3.text((50, 118), "https://dkwin9.com", fill=white_color)
    
    draw3.text((40, 170), "Invitation / Referral Code:", fill=gray_color)
    draw3.rectangle([40, 195, 360, 235], fill=(15, 23, 42), outline=gray_color)
    draw3.text((50, 208), "787222388616", fill=white_color)

    draw3.rectangle([40, 280, 360, 340], fill=cyan_color)
    draw3.text((100, 300), "UPDATE LINK & PASSWORDS", fill=white_color)
    frames.append(im3)

    gif_path = os.path.expanduser("~/robium_predictor_demo.gif")
    frames[0].save(gif_path, save_all=True, append_images=frames[1:], duration=1500, loop=0)
    print(f"Demo GIF generated successfully at: {gif_path}")

if __name__ == "__main__":
    generate_demo()
