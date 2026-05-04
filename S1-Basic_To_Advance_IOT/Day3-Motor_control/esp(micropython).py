from machine import Pin
import time

# --- ESP32 / ESP8266 Setup ---
# Using safe GPIO pins 4 and 5
in1 = Pin(4, Pin.OUT)
in2 = Pin(5, Pin.OUT)

# Ensure the motor is off to start
in1.value(0)
in2.value(0)

print("⚙️ ESP Motor Controller Online!")
print("-" * 30)

def motor_forward():
    in1.value(1)
    in2.value(0)
    print("➡️ FORWARD")

def motor_reverse():
    in1.value(0)
    in2.value(1)
    print("⬅️ REVERSE")

def motor_stop():
    in1.value(0)
    in2.value(0)
    print("🛑 STOP")

# --- TEST SEQUENCE ---
try:
    motor_forward()
    time.sleep(2)
    
    motor_stop()
    time.sleep(1)
    
    motor_reverse()
    time.sleep(2)
    
    motor_stop()
    print("\nTest complete.")

except KeyboardInterrupt:
    motor_stop()
    print("\nSystem shut down safely.")