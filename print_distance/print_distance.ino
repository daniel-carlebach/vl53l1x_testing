#include <Wire.h>
#include "SparkFun_VL53L1X.h"

SFEVL53L1X distanceSensor;

void setup() {
  // put your setup code here, to run once:
  Wire.begin();
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  distanceSensor.startRanging(); //Write configuration bytes to initiate measurement
  while (!distanceSensor.checkForDataReady())
  {
    delay(1);
  }
  int distance = distanceSensor.getDistance(); //Get the result of the measurement from the sensor
  distanceSensor.clearInterrupt();
  distanceSensor.stopRanging();

  Serial.println(distance);
}
