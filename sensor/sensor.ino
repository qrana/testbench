const int SIGNAL_PIN = 3;
unsigned long int previous_time;
unsigned long int new_time;
int count;

void setup() {
  Serial.begin(115200);
  digitalWrite(SIGNAL_PIN, HIGH); 
  //Serial.println("Heimoi");
  previous_time = 0;
  new_time = 0;
  count = 0;
  attachInterrupt(digitalPinToInterrupt(SIGNAL_PIN), isr_counter, RISING);
  pinMode(13, OUTPUT);
}

void loop() {
  if (new_time != previous_time)
  {
    digitalWrite(13, HIGH);
    Serial.print((unsigned int) new_time - previous_time);
    Serial.println();
    previous_time = new_time;
    digitalWrite(13, LOW);
  }
}

// interrupt service routine
void isr_counter(){
  ++count;
  if (count >= 2)
  {
    new_time = micros();
    count = 0;
  }
}

