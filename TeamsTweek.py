from time import sleep
from threading import Thread
from keyboard import press_and_release
from pystray import Icon
from pystray import MenuItem as item
from PIL import Image, ImageDraw
from os import path




script_directory = path.dirname(path.abspath(__file__))
file_name = "Key.txt"
file_path = path.join(script_directory, file_name)
try:
    with open(file_path, "r") as file:
        file_contents = file.read()
        print("Contents of the file:")
        print(file_contents)
except FileNotFoundError:
    print(f"The file '{file_name}' does not exist in the script's directory")
except Exception as e:
    print({e})



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
        press_and_release(file_contents)
        press_and_release(file_contents)
        print("[DEBUG] Sleeping for 60 seconds.")
        sleep(60)
    print("[DEBUG] AlwaysActive() has been stopped by user action.")

def run_tray_icon():
    print("[DEBUG] run_tray_icon() called - creating tray icon.")
    icon = Icon(
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
    loop_thread = Thread(target=AlwaysActive)
    loop_thread.start()
    run_tray_icon()
    loop_thread.join()
    print("[DEBUG] Script fully terminated.")
