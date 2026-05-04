# 🏎️ Universal Motor Controller Guide

Welcome to the Universal Motor Controller project! This repository contains the wiring diagrams and code required to control a dual-channel DC Motor Driver (like the MX1508 or L298N Mini) using three of the most popular microcontrollers in the world:

1. **Raspberry Pi Pico / Pico W** (MicroPython)
2. **ESP32 / ESP8266** (MicroPython)
3. **Arduino Uno / Nano** (C++)

## ⚠️ CRITICAL POWER WARNING
**Do not power DC motors directly from your microcontroller when the robot is on the ground!** 
While you can use the `VBUS` (5V) pin for a quick test while holding the motors in the air, putting the robot on the floor will cause the motors to pull too much current. This will instantly crash your microcontroller or permanently fry your USB port. 

**Best Practice:** Always connect a separate battery pack (like a 4x AA holder) directly to the `+` and `-` pins of the motor module. Ensure you connect the battery's `-` (Ground) wire to the Motor Module AND the Microcontroller so they share a common ground!

---

## 🔌 Hardware Wiring Guides

### 1. Raspberry Pi Pico / Pico W
* **Language:** MicroPython
* **Code File:** [`pico(micropython).py`](pico(micropython).py)

| Motor Module Pin | Connects to Pico W |
| :--- | :--- |
| **+** (Power) | External Battery `+` (or Pico `VBUS` Pin 40 for air-testing) |
| **-** (Ground) | External Battery `-` **AND** Pico `GND` (Physical Pin 38) |
| **IN1** | **GPIO 0** (Physical Pin 1) |
| **IN2** | **GPIO 1** (Physical Pin 2) |

---

### 2. ESP32 / ESP8266
* **Language:** MicroPython
* **Code File:** [`esp(micropython).py`](esp(micropython).py)

*Note: We avoid GPIO 0 and 1 on ESP boards as they are often reserved for the internal boot sequence. We use safe pins 4 and 5 instead.*

| Motor Module Pin | Connects to ESP Board |
| :--- | :--- |
| **+** (Power) | External Battery `+` (or ESP `VIN`/`5V` for air-testing) |
| **-** (Ground) | External Battery `-` **AND** ESP `GND` |
| **IN1** | **GPIO 4** (Pin D2 on some ESP8266 boards) |
| **IN2** | **GPIO 5** (Pin D1 on some ESP8266 boards) |

---

### 3. Arduino Uno / Nano / Mega
* **Language:** C++
* **Code File:** ['arduino.ino`](arduino.ino)

| Motor Module Pin | Connects to Arduino |
| :--- | :--- |
| **+** (Power) | External Battery `+` (or Arduino `5V` for air-testing) |
| **-** (Ground) | External Battery `-` **AND** Arduino `GND` |
| **IN1** | **Digital Pin 5** (`D5`) |
| **IN2** | **Digital Pin 6** (`D6`) |

---
