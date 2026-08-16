import os
import time
from PIL import Image

# Путь к твоей гифке (можешь положить её рядом со скриптом или указать полный путь)
GIF_PATH = "/home/yui/lain-dance/lain.gif" 

def frame_to_ascii(image, width=80):
    # Набор символов от темных к светлым
    ASCII_CHARS = "@%#*+=-:. "
    
    # Изменяем размер кадра под ширину терминала, сохраняя пропорции
    W, H = image.size
    aspect_ratio = H / W
    height = int(width * aspect_ratio * 0.55) # 0.55 компенсирует вытянутость букв в терминале
    image = image.resize((width, height)).convert("L")
    
    pixels = image.getdata()
    ascii_str = "".join([ASCII_CHARS[pixel // 28] for pixel in pixels])
    
    # Разбиваем строку на строчки по ширине
    ascii_img = "\n".join([ascii_str[i:i+width] for i in range(0, len(ascii_str), width)])
    return ascii_img

def play_gif(path, loop=True):
    try:
        img = Image.open(path)
    except FileNotFoundError:
        print(f"Ошибка: Не найден файл гифки по пути '{path}'")
        return

    frames = []
    durations = []
    
    try:
        while True:
            frames.append(img.copy())
            durations.append(img.info.get('duration', 100)) # Длительность кадра в мс
            img.seek(len(frames))
    except EOFError:
        pass

    # Очищаем экран перед началом и скрываем курсор (опционально)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Загрузка танца Лайн в терминал...")
    time.sleep(1)

    try:
        while True:
            for frame, duration in zip(frames, durations):
                # Переводим кадр в ASCII (ширину можно подогнать под твой экран, например 70-100 символов)
                ascii_frame = frame_to_ascii(frame, width=80)
                
                # Возвращаем курсор в начало экрана вместо очистки (чтобы не было мерцания)
                print("\033[H" + ascii_frame, end="")
                
                # Задержка под скорость кадров гифки
                time.sleep(duration / 1000.0)
            if not loop:
                break
    except KeyboardInterrupt:
        # Корредктный выход по Ctrl+C
        print("\nТанец завершен.")

if __name__ == "__main__":
    play_gif(GIF_PATH)
