import time
import threading
from keyboard import press_and_release

import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw

stop_loop = False

def create_image():
    print("[DEBUG] create_image() called - creating tray icon image.")
    width = 64
    height = 64
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    draw.ellipse((8, 8, width-8, height-8), fill="blue")
    return image

def on_exit_clicked(icon, item):
    global stop_loop
    print("[DEBUG] 'Exit' clicked - setting stop_loop to True.")
    stop_loop = True
    icon.stop()

def AlwaysActive():
    print("[DEBUG] AlwaysActive() started.")
    global stop_loop
    while not stop_loop:
        print("[DEBUG] Pressing F18 and F19.")
        press_and_release("F18")
        press_and_release("F19")
        print("[DEBUG] Sleeping for 60 seconds.")
        time.sleep(60)
    print("[DEBUG] AlwaysActive() has been stopped by user action.")

def run_tray_icon():
    print("[DEBUG] run_tray_icon() called - creating tray icon.")
    icon = pystray.Icon(
        "AlwaysActive",          # internal name
        create_image(),          # tray icon image
        "AlwaysActive Script",   # tooltip (hover text)
        menu=(
            item(
                "Exit", 
                on_exit_clicked   # function to call when clicked
            ),
        )
    )
    print("[DEBUG] Starting tray icon. Right-click -> 'Exit' to stop the script.")
    icon.run()
    print("[DEBUG] Tray icon stopped.")

if __name__ == "__main__":
    print("[DEBUG] Main started - launching AlwaysActive() in a separate thread.")
    loop_thread = threading.Thread(target=AlwaysActive)
    loop_thread.start()
    run_tray_icon()
    loop_thread.join()
    print("[DEBUG] Script fully terminated.")
