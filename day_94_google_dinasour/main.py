import pyautogui
from PIL import ImageGrab
import time

# Adjust these based on your screen
BOX = (180, 820, 280, 860)
 # (left, top, right, bottom)

def is_obstacle(pixel):
    """Return True if pixel looks dark (cactus/bird)."""
    return pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100

def detect_obstacle():
    """Check the defined BOX for any dark pixel."""
    screenshot = ImageGrab.grab(bbox=BOX)
    pixels = screenshot.load()
    width, height = screenshot.size
    for x in range(width):
        for y in range(height):
            if is_obstacle(pixels[x, y]):
                return True
    return False

# --- Calibration step (optional, can be commented out) ---
def calibrate_box():
    """Save a calibration snapshot to verify the detection area."""
    img = ImageGrab.grab(bbox=BOX)
    img.save("calibration_preview.png")
    print("📸 Saved 'calibration_preview.png' to check your detection zone.")

# Uncomment once to test where the bot looks
# calibrate_box()

print("🦖 Get ready! You have 5 seconds to switch to the Dino game.")
time.sleep(5)
print("🤖 Bot running... press Ctrl+C to stop.")

try:
    while True:
        if detect_obstacle():
            pyautogui.press("space")
            print("Jump!")
            time.sleep(0.1)  # small cooldown
except KeyboardInterrupt:
    print("\n🛑 Bot stopped.")
  