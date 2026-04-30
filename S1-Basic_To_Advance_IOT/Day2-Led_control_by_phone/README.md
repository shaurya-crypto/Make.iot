#  Day 2 — Smart Phone LED Controller
### *Basic to Advance IoT Series by [@MakeIoT](https://www.instagram.com/make.iot/)*

> **What you'll build:** Turn your microcontroller into a tiny web server. Open your phone browser, tap buttons, control real LEDs — no app, no internet needed.

---

##  What You Need

| Item | Qty |
|:-----|:---:|
| ESP32 **or** ESP8266 **or** Raspberry Pi Pico W | 1 |
| LEDs (any color) | 2 |
| 220Ω or 330Ω Resistors | 2 |
| Breadboard | 1 |
| Jumper Wires | ~6 |

---

##  Wiring

> 📌 LED legs: **long leg = (+) positive** · **short leg = (−) negative**

### ESP32 / ESP8266

| LED | (+) Long Leg → Pin | (−) Short Leg → |
|:----|:-------------------|:----------------|
| LED 1 | `GPIO 12` | `GND` |
| LED 2 | `GPIO 14` | `GND` |

### Raspberry Pi Pico W

| LED | (+) Long Leg → Pin | (−) Short Leg → |
|:----|:-------------------|:----------------|
| LED 1 | `GP2` | `GND` |
| LED 2 | `GP3` | `GND` |

> ⚠️ Always place a **330Ω resistor** between the GPIO pin and the LED's long leg. Skipping it can burn your LED or damage the board.

---

## 💻 Setup

### Option A — MicroPython `(Pico W / ESP32 / ESP8266)`

1. Install **MicroPython** on your board using [Thonny IDE](https://thonny.org)
2. Open `main.py` from this folder in Thonny
3. Find these two lines and update them:
   ```
   WIFI_SSID     = "YOUR_WIFI_NAME"
   WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
   ```
4. Hit **Run** (▶). The Shell will print an IP like `192.168.1.42`
5. Open that IP on your phone browser — done!

## Soon Lauching my own ide with AI !
---

### Option B — C++ Arduino IDE `(ESP32 / ESP8266)`

1. Open **Arduino IDE** and install your board:
   - ESP32 → [Install Guide](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)
   - ESP8266 → [Install Guide](https://arduino-esp8266.readthedocs.io/en/latest/installing.html)
2. Open `Day2_SmartLight.ino` from this folder
3. Find these two lines and update them:
   ```
   ssid     = "YOUR_WIFI_NAME"
   password = "YOUR_WIFI_PASSWORD"
   ```
4. Select your board + COM port → click **Upload**
5. Open **Serial Monitor** at `115200` baud — it will print the IP
6. Open that IP on your phone browser — done!

---

##  Using the Web Interface

Once you open the IP address on your phone:

| Button | Action |
|:-------|:-------|
| **LED 1 Toggle** | Turns LED 1 ON or OFF |
| **LED 2 Toggle** | Turns LED 2 ON or OFF |
| **Disco Mode** | Alternates both LEDs automatically |

>  Your phone and the microcontroller **must be on the same Wi-Fi network.**

---

##  Troubleshooting

| Problem | Fix |
|:--------|:----|
| IP not showing in Serial Monitor | Check Wi-Fi name/password spelling |
| Page not loading on phone | Make sure phone is on same Wi-Fi, not mobile data |
| LEDs not lighting up | Check polarity (long leg to GPIO), check resistor placement |
| Board not detected by PC | Try a different USB cable (some are charge-only) |

---

*📸 Watch the full build video on Instagram → [@MakeIoT](https://instagram.com/MakeIoT)*