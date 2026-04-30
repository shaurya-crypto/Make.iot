#include <WiFi.h>
#include <WebServer.h>

// --- Configuration ---
const char* ssid = "WorkPlace";
const char* password = "Whitefield1947";

// --- Hardware Setup ---
const int led1Pin = 12;
const int led2Pin = 14;

WebServer server(80);

// --- HTML & CSS UI ---
// The R"rawliteral(...)rawliteral" allows us to paste multi-line HTML safely in C++
const char htmlPage[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>IoT Web Control</title>
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
        
        .btn-on { background: #00b894; }
        .btn-on:hover { background: #01e0b5; }
        
        .btn-off { background: #d63031; }
        .btn-off:hover { background: #ff4757; }
        
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
        <h1>Web Dashboard</h1>
        
        <div class="led-group">
            <div class="led-title">LED 1 (GPIO 12)</div>
            <a href="/1on"><button class="btn-on">ON</button></a> 
            <a href="/1off"><button class="btn-off">OFF</button></a>
        </div>
        
        <div class="led-group">
            <div class="led-title">LED 2 (GPIO 14)</div>
            <a href="/2on"><button class="btn-on">ON</button></a> 
            <a href="/2off"><button class="btn-off">OFF</button></a> 
            <a href="/disco"><button class="btn-disco">DISCO</button></a>
        </div>
    </div>
</body>
</html>
)rawliteral";

// --- Route Handlers ---
void handleRoot() {
  server.send(200, "text/html", htmlPage);
}

void handle1On() {
  digitalWrite(led1Pin, HIGH);
  server.send(200, "text/html", htmlPage);
}

void handle1Off() {
  digitalWrite(led1Pin, LOW);
  server.send(200, "text/html", htmlPage);
}

void handle2On() {
  digitalWrite(led2Pin, HIGH);
  server.send(200, "text/html", htmlPage);
}

void handle2Off() {
  digitalWrite(led2Pin, LOW);
  server.send(200, "text/html", htmlPage);
}

void handleDisco() {
  for (int i = 0; i < 20; i++) {
    digitalWrite(led2Pin, !digitalRead(led2Pin)); // Toggle state
    delay(100);
  }
  digitalWrite(led2Pin, LOW); // Turn off after disco
  server.send(200, "text/html", htmlPage);
}

void setup() {
  Serial.begin(115200);
  
  pinMode(led1Pin, OUTPUT);
  pinMode(led2Pin, OUTPUT);
  digitalWrite(led1Pin, LOW);
  digitalWrite(led2Pin, LOW);

  // Connect to Wi-Fi
  Serial.print("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi connected.");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  // Define Server Routes
  server.on("/", handleRoot);
  server.on("/1on", handle1On);
  server.on("/1off", handle1Off);
  server.on("/2on", handle2On);
  server.on("/2off", handle2Off);
  server.on("/disco", handleDisco);

  server.begin();
  Serial.println("HTTP server started");
}

void loop() {
  server.handleClient();
}