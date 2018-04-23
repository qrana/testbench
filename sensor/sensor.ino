#include <util/atomic.h>

const int SIGNAL_PIN = 3;
const int ANALOG_PIN = 1;
volatile unsigned long int previous_time;
volatile unsigned long int new_time;
volatile int count;

void setup() {
  Serial.begin(115200);
  digitalWrite(SIGNAL_PIN, HIGH); 
  previous_time = 0;
  new_time = 0;
  count = 0;
  attachInterrupt(digitalPinToInterrupt(SIGNAL_PIN), isr_counter, RISING);
  pinMode(13, OUTPUT);
}

void loop() {
  unsigned int diff;
  
  ATOMIC_BLOCK(ATOMIC_RESTORESTATE) {
  diff = (unsigned int) new_time - previous_time;
  }
  
  if (diff != 0)
  {
    previous_time = new_time;
    uint8_t lambda = (uint8_t)analogRead(ANALOG_PIN) / 4;
    Serial.println();
    Serial.print(diff);
    Serial.println();
    Serial.print(lambda);
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

