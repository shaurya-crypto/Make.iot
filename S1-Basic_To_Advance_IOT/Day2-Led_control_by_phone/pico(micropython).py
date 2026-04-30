import network
import socket
import time
from machine import Pin

# Setup Pins
led2 = Pin(2, Pin.OUT)
led3 = Pin(3, Pin.OUT)

# Wi-Fi Credentials
ssid = 'WorkPlace'
password = 'Whitefield1947'

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.status() != 3:  # 3 is the status for connected
        print('Waiting for connection...')
        time.sleep(1)
    print('Connected! IP:', wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

def webpage():
    html = """<!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Pico W Control</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1e1e2f, #2a2a4a);
                color: #ffffff;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                margin: 0;
            }
            .container {
                background: rgba(255, 255, 255, 0.05);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                text-align: center;
                max-width: 400px;
                width: 90%;
            }
            h1 {
                margin-top: 0;
                margin-bottom: 30px;
                font-weight: 300;
                letter-spacing: 2px;
                text-transform: uppercase;
                font-size: 24px;
            }
            .led-group {
                background: rgba(0, 0, 0, 0.2);
                margin: 20px 0;
                padding: 20px;
                border-radius: 15px;
            }
            .led-title {
                margin-bottom: 15px;
                font-size: 18px;
                font-weight: 600;
                color: #a8b2d1;
            }
            a { text-decoration: none; }
            button {
                border: none;
                color: white;
                padding: 12px 24px;
                text-align: center;
                font-size: 16px;
                font-weight: bold;
                margin: 5px;
                cursor: pointer;
                border-radius: 50px;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0,0,0,0.2);
            }
            button:hover {
                transform: translateY(-3px);
                box-shadow: 0 8px 25px rgba(0,0,0,0.4);
            }
            button:active {
                transform: translateY(1px);
                box-shadow: 0 2px 10px rgba(0,0,0,0.2);
            }
            
            /* Specific Button Colors */
            .btn-on { background: #00b894; }
            .btn-on:hover { background: #01e0b5; }
            
            .btn-off { background: #d63031; }
            .btn-off:hover { background: #ff4757; }
            
            /* Disco Button Animation */
            .btn-disco {
                background: linear-gradient(45deg, #ff00cc, #3333ff);
                background-size: 200% 200%;
                animation: gradientBG 3s ease infinite, pulse 1.5s infinite;
            }
            
            @keyframes gradientBG {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            @keyframes pulse {
                0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 204, 0.7); }
                70% { transform: scale(1.05); box-shadow: 0 0 0 15px rgba(255, 0, 204, 0); }
                100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 0, 204, 0); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Pico W Control</h1>
            
            <div class="led-group">
                <div class="led-title">GP2 (LED 1)</div>
                <a href="/2on"><button class="btn-on">ON</button></a> 
                <a href="/2off"><button class="btn-off">OFF</button></a>
            </div>
            
            <div class="led-group">
                <div class="led-title">GP3 (LED 2)</div>
                <a href="/3on"><button class="btn-on">ON</button></a> 
                <a href="/3off"><button class="btn-off">OFF</button></a> 
                <a href="/disco"><button class="btn-disco">DISCO</button></a>
            </div>
        </div>
    </body>
    </html>
    """
    return html

def disco_mode():
    for _ in range(20):
        led3.toggle()
        time.sleep(0.1)
    led3.off()

ip = connect()
s = socket.socket()
s.bind(('', 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    
    # Logic for routes
    if '/2on' in request:
        led2.on()
    elif '/2off' in request:
        led2.off()
    elif '/3on' in request:
        led3.on()
    elif '/3off' in request:
        led3.off()
    elif '/disco' in request:
        disco_mode()

    response = webpage()
    conn.send('HTTP/1.1 200 OK\nContent-Type: text/html\n\n' + response)
    conn.close()
