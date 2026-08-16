<div align="center">

# 🌐 lain-dance

*Let's all love Lain inside your terminal.*

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/license-MIT-purple?style=for-the-badge)
![Lain](https://img.shields.io/badge/Serial%20Experiments-Lain-pink?style=for-the-badge)

</div>

---

## ✨ Overview

`lain-dance` is a lightweight Python script that renders and plays animated ASCII art of **Lain Iwakura** dancing directly inside your Linux / macOS / Windows terminal emulator.

It parses GIF frames, converts grayscale brightness to ASCII character gradients, compensates for terminal font aspect ratios, and uses smooth, flicker-free ANSI cursor repositioning.

```
                              #**++##::::%#%
                            +:::*%%:::::::%*#
                          %%%*%%%%:::::::::=#
                      #-:#@%::%@%%%%::::::::
                     .+:+@%:=:--%@%%%::::::=
                    =....@=*-:::#=% %*:::::*
```

---

## 🚀 Features

- ⚡ **Flicker-Free Playback:** Uses ANSI cursor movement (`\033[H`) instead of clearing the screen, eliminating terminal flickering.
- 📐 **Aspect-Ratio Compensation:** Adjusts vertical scale automatically so the animation looks natural on standard terminal fonts.
- 🔁 **Endless Loop:** Plays continuously until interrupted with `Ctrl + C`.
- 📦 **Minimal Dependencies:** Requires only `Pillow` (PIL) and standard Python libraries.

---

## 🛠️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/lain-dance.git
cd lain-dance
```

### 2. Install dependencies
```bash
pip install pillow
```

### 3. Run the script
```bash
python3 lain-dance.py
```

---

## ⚡ Quick Access (Alias Setup)

Add `lain-dance` to your shell config for 1-command launch from anywhere:

### **Zsh (`~/.zshrc`)**
```bash
alias lain-dance="python3 ~/lain-dance/lain-dance.py"
```

### **Fish (`~/.config/fish/config.fish`)**
```fish
alias lain-dance="python3 ~/lain-dance/lain-dance.py"
```

---

## 🎨 Customization

You can tweak parameters in `lain-dance.py`:

```python
# Change terminal width (default: 80 characters)
ascii_frame = frame_to_ascii(frame, width=90)

# Replace with your own GIF path
GIF_PATH = "/path/to/your/custom.gif"
```

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

<div align="center">
<i>"No matter where you go, everyone's always connected."</i>
</div>
