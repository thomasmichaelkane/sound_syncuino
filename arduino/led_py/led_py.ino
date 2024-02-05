void setup() {

  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);

}

void loop() {

  // put your main code here, to run repeatedly:
 if (Serial.available() > 0) {
   String msg = Serial.readStringUntil('\n');

   int duration = msg.toInt();

    digitalWrite(LED_BUILTIN, HIGH);
    delay(duration);
    digitalWrite(LED_BUILTIN, LOW);

 }
}