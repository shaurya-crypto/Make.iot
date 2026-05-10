// Setup Pins - Change these to match your wiring
const int trigPin = 12; // Connected to Trigger on HC-SR04
const int echoPin = 14; // Connected to Echo on HC-SR04

// Variables to store the raw time and the calculated distance
long duration;
float distance;

void setup() {
  // Start the Serial Monitor to see the distance values
  Serial.begin(115200); 
  
  pinMode(trigPin, OUTPUT); // Trigger fires the sound
  pinMode(echoPin, INPUT);  // Echo listens for the sound
}

void loop() {
  // 1. Ensure the trigger is OFF initially
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // 2. Fire the invisible sound wave (10 microsecond pulse)
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // 3. Catch the echo and measure the time it took
  duration = pulseIn(echoPin, HIGH);

  // 4. Math: Speed of sound is 0.0343 cm/microsecond
  // We divide by 2 because the sound travels there AND back
  distance = (duration * 0.0343) / 2;

  // Print the result to the Serial Monitor
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");

  // Wait half a second before pinging again
  delay(500); 
}