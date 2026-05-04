from machine import Pin
import time

# Set up the motor pins
in1 = Pin(0, Pin.OUT)
in2 = Pin(1, Pin.OUT)

# Ensure the motor is off to start
in1.value(0)
in2.value(0)

print("⚙️ Motor Controller Online!")
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
    time.sleep(2)  # Run forward for 2 seconds
    
    motor_stop()
    time.sleep(1)  # Pause for 1 second
    
    motor_reverse()
    time.sleep(2)  # Run in reverse for 2 seconds
    
    motor_stop()
    print("\nTest complete.")

except KeyboardInterrupt:
    # This ensures the motor doesn't keep spinning if you hit the Stop button
    motor_stop()
    print("\nSystem shut down safely.")