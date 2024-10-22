#include <MeMegaPi.h>

// Create motor objects
MeMegaPiDCMotor motor1(PORT1B); 
MeMegaPiDCMotor motor2(PORT2B); 
MeMegaPiDCMotor motor3(PORT3B); 
MeMegaPiDCMotor motor4(PORT4B); 

MeUltrasonicSensor ultrasonic(PORT7); 

float distance = 0;

void setup() {
  Serial.begin(9600);
  motor1.stop();
  motor2.stop();
  motor3.stop();
  motor4.stop();
}

void loop() {
  distance = ultrasonic.distanceCm();
  Serial.print("Distance: ");
  Serial.println(distance);

  if (distance > 50) {
    motor1.run(-100);  
    motor2.run(100);
    motor3.run(-100); 
  } 
  else if (distance > 20 && distance <= 50) {
    motor1.run(50);
    motor2.run(50);
    motor3.run(50);   
  } 
  else if (distance <= 20) {
    motor1.stop();
    motor2.stop();
    motor3.stop();

 
    motor4.run(-100);
    delay(1200);
    motor4.run(100);
    delay(1200);             
    motor4.stop(); 
    delay(2000);
    motor4.run(-100);
    delay(1200);  
    motor4.run(100);
    delay(1200);
    motor4.stop();
    delay(2000);
    
  }

  delay(100); 
}
