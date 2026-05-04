// --- ARDUINO SETUP ---
// Define our motor pins
const int in1 = 5;
const int in2 = 6;

void setup() {
  // Start the serial monitor so we can see print statements
  Serial.begin(9600);
  
  // Tell the Arduino these pins will be pushing out power
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  
  // Ensure the motor is stopped on boot
  motorStop();
  
  Serial.println("⚙️ Arduino Motor Controller Online!");
  Serial.println("----------------------------------");
}

void loop() {
  // --- TEST SEQUENCE ---
  // In Arduino, the loop() function runs forever automatically
  
  motorForward();
  delay(2000); // Arduino uses milliseconds (2000ms = 2 seconds)
  
  motorStop();
  delay(1000);
  
  motorReverse();
  delay(2000);
  
  motorStop();
  delay(5000); // Wait 5 seconds before repeating the whole loop
}

// --- MOTOR FUNCTIONS ---
void motorForward() {
  digitalWrite(in1, HIGH); // HIGH is the Arduino equivalent of "1"
  digitalWrite(in2, LOW);  // LOW is the Arduino equivalent of "0"
  Serial.println("➡️ FORWARD");
}

void motorReverse() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, HIGH);
  Serial.println("⬅️ REVERSE");
}

void motorStop() {
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  Serial.println("🛑 STOP");
}