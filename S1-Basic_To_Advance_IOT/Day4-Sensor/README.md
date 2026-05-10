# 👀 Day 4: HC-SR04 Ultrasonic Sensor (Giving Machines Eyes)

Welcome to Day 4 of the Basic to Advance IoT series! This repository contains the wiring diagrams and code required to read distance using the **HC-SR04 Ultrasonic Sensor**. 

Instead of a camera, this sensor uses echolocation (sound waves) to detect obstacles and measure exact distances. We have included code for three of the most popular microcontroller environments:

1. **Raspberry Pi Pico / Pico W** (MicroPython)
2. **ESP32 / ESP8266** (MicroPython)
3. **Arduino Uno / Nano** (C++)


## 🔌 Hardware Wiring Guides

### 1. Raspberry Pi Pico / Pico W
* **Language:** MicroPython
* **Code File:** [`pico.py`](pico.py)

| HC-SR04 Pin | Connects to Pico W |
| :--- | :--- |
| **VCC** (Power) | **3v3** (Physical Pin 36 - Provides 3.3v) |
| **GND** (Ground)| **GND** (Physical Pin 38) |
| **TRIG** (Fire) | **GPIO 14** (Physical Pin 16) |
| **ECHO** (Catch)| **GPIO 15** (Physical Pin 17) |

---


### 3. Arduino Uno / Nano / Mega
* **Language:** C++
* **Code File:** [`arduino.ino`](arduino.ino)

| HC-SR04 Pin | Connects to Arduino |
| :--- | :--- |
| **VCC** (Power) | **5V** |
| **GND** (Ground)| **GND** |
| **TRIG** (Fire) | **Digital Pin 12** (`D12`) |
| **ECHO** (Catch)| **Digital Pin 11** (`D11`) |

---

## 🧠 How the Math Works (In the Code)
If you look at the code, you will notice this formula: 
`Distance = (Time * 0.0343) / 2`

1. **Time:** How many microseconds it took for the sound to return.
2. **0.0343:** The speed of sound in centimeters per microsecond.
3. **/ 2:** We divide by 2 because the sound had to travel *to* the object, and then bounce *back*. We only want the distance one-way!