#include <DigiUSB.h>

#define PIN_SENS 0
#define PIN_LED  1

#define MESSAGE_LEN 13
uint8_t CMD_ON [MESSAGE_LEN] = {"a2ce4f368c4b"};
uint8_t CMD_OFF[MESSAGE_LEN] = {"67faacf02530"};

int state = 0;

void setup() {
  DigiUSB.begin();
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_SENS, INPUT);

  DigiUSB.println(F("Hello!"));
}

void loop() {
  int state0 = !digitalRead(PIN_SENS);
  if (state0 != state) {
    led_on();
    send_state(state0);
    led_off();
    state = state0;
  }
  DigiUSB.delay(10);
}

void send_state(int state) {
  uint8_t* msg = state ? CMD_ON : CMD_OFF;
  for (int i = 0; i < MESSAGE_LEN; i++) {
    DigiUSB.write(msg[i]);
  }
}

void led_on() {
  digitalWrite(PIN_LED, HIGH);
}

void led_off() {
  digitalWrite(PIN_LED, LOW);
}
