import os
import time
from PIL import Image

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
GIF_PATH = os.path.join(SCRIPT_DIR, "lain.gif")

def frame_to_ascii(image, width=80):
    ASCII_CHARS = "@%#*+=-:. "
    
    W, H = image.size
    aspect_ratio = H / W
    height = int(width * aspect_ratio * 0.55)
    image = image.resize((width, height)).convert("L")
    
    try:
        pixels = image.get_flattened_data()
    except AttributeError:
        pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 28] for pixel in pixels])
    
    ascii_img = "\n".join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])
    return ascii_img

def play_gif(path, loop=True):
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Error: GIF file not found at '{path}'")
        return

    frames = []
    durations = []
    
    try:
        while True:
            frames.append(img.copy())
            durations.append(img.info.get('duration', 100))
            img.seek(len(frames))
    except EOFError:
        pass

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Loading Lain dance in terminal...")
    time.sleep(1)

    try:
        while True:
            for frame, duration in zip(frames, durations):
                ascii_frame = frame_to_ascii(frame, width=80)
                print("\033[H" + ascii_frame, end="")
                time.sleep(duration / 1000.0)
            if not loop:
                break
    except KeyboardInterrupt:
        print("\nDance completed.")

if __name__ == "__main__":
    play_gif(GIF_PATH)
