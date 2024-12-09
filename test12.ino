// Define motor control pins
#define ENA 5  // Left motor enable pin
#define IN1 8  // Left motor IN1
#define IN2 9  // Left motor IN2
#define ENB 6  // Right motor enable pin
#define IN3 10 // Right motor IN3
#define IN4 11 // Right motor IN4

// Define Raspberry Pi input pins
#define RPI_PIN1 2  // Connect to RPi GPIO 5
#define RPI_PIN2 3  // Connect to RPi GPIO 6
#define RPI_PIN3 4  // Connect to RPi GPIO 13
#define RPI_PIN4 7  // Connect to RPi GPIO 19

// Motor speed constants
const int NORMAL_SPEED = 200;  // Normal speed (0-255)
const int TURN_SPEED = 180;    // Turning speed (0-255)
const int SHARP_TURN_SPEED = 220;  // Speed for sharp turns

void setup() {
  // Configure motor control pins as outputs
  pinMode(ENA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENB, OUTPUT);
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT);
  
  // Configure Raspberry Pi input pins
  pinMode(RPI_PIN1, INPUT);
  pinMode(RPI_PIN2, INPUT);
  pinMode(RPI_PIN3, INPUT);
  pinMode(RPI_PIN4, INPUT);
  
  // Initialize with motors stopped
  stopMotors();
  
  // For debugging
  Serial.begin(9600);
}

void loop() {
  // Read control signals from Raspberry Pi
  int pin1 = digitalRead(RPI_PIN1);
  int pin2 = digitalRead(RPI_PIN2);
  int pin3 = digitalRead(RPI_PIN3);
  int pin4 = digitalRead(RPI_PIN4);
  
  // Control motors based on Raspberry Pi signals
  if (pin1 == LOW && pin2 == LOW && pin3 == LOW && pin4 == LOW) {
    // Forward
    moveForward(NORMAL_SPEED);
  }
  // Right turns with varying intensity
  else if (pin1 == HIGH && pin2 == LOW && pin3 == LOW && pin4 == LOW) {
    // Slight right
    turnRight(TURN_SPEED);
  }
  else if (pin1 == LOW && pin2 == HIGH && pin3 == LOW && pin4 == LOW) {
    // Medium right
    turnRight(SHARP_TURN_SPEED);
  }
  else if (pin1 == HIGH && pin2 == HIGH && pin3 == LOW && pin4 == LOW) {
    // Sharp right
    turnRightInPlace();
  }
  // Left turns with varying intensity
  else if (pin1 == LOW && pin2 == LOW && pin3 == HIGH && pin4 == LOW) {
    // Slight left
    turnLeft(TURN_SPEED);
  }
  else if (pin1 == HIGH && pin2 == LOW && pin3 == HIGH && pin4 == LOW) {
    // Medium left
    turnLeft(SHARP_TURN_SPEED);
  }
  else if (pin1 == LOW && pin2 == HIGH && pin3 == HIGH && pin4 == LOW) {
    // Sharp left
    turnLeftInPlace();
  }
  else {
    // Stop if undefined combination
    stopMotors();
  }
}

void moveForward(int speed) {
  // Left motor forward
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed);
  
  // Right motor forward
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, speed);
  
  Serial.println("Moving Forward");
}

void turnRight(int speed) {
  // Left motor at full speed
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed);
  
  // Right motor at reduced speed
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, speed * 0.4);
  
  Serial.println("Turning Right");
}

void turnLeft(int speed) {
  // Left motor at reduced speed
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, speed * 0.4);
  
  // Right motor at full speed
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, speed);
  
  Serial.println("Turning Left");
}

void turnRightInPlace() {
  // Left motor forward
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(ENA, SHARP_TURN_SPEED);
  
  // Right motor backward
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(ENB, SHARP_TURN_SPEED);
  
  Serial.println("Sharp Right Turn");
}

void turnLeftInPlace() {
  // Left motor backward
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  analogWrite(ENA, SHARP_TURN_SPEED);
  
  // Right motor forward
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(ENB, SHARP_TURN_SPEED);
  
  Serial.println("Sharp Left Turn");
}

void stopMotors() {
  // Stop both motors
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(ENA, 0);
  analogWrite(ENB, 0);
  
  Serial.println("Stopped");
}