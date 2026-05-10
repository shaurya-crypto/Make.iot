from machine import Pin, time_pulse_us
import time

# Setup Pins - Change these to match your wiring
TRIGGER_PIN = 16 # Connected to Trigger on HC-SR04
ECHO_PIN = 17     # Connected to Echo on HC-SR04

trigger = Pin(TRIGGER_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)

def get_distance():
    # 1. Ensure the trigger is OFF initially
    trigger.value(0)
    time.sleep_us(2)
    
    # 2. Fire the invisible sound wave (10 microsecond pulse)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)
    
    # 3. Catch the echo and measure how long it took (in microseconds)
    # 30000us timeout prevents the board from freezing if nothing is detected
    duration = time_pulse_us(echo, 1, 30000) 
    
    if duration < 0:
        return -1  # Signal lost or out of range
        
    # 4. Math: Speed of sound is 0.0343 cm/microsecond
    # We divide by 2 because the sound travels there AND back
    distance = (duration * 0.0343) / 2
    
    return distance

# Main loop
while True:
    dist = get_distance()
    
    if dist > 0:
        print(f"Distance: {dist:.1f} cm")
    else:
        print("Distance: Out of range")
        
    time.sleep(0.5) # Wait half a second before pinging again