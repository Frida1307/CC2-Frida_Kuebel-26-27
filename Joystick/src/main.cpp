#include <Arduino.h>

constexpr uint8_t JOYSTICK_X_PIN = 34;
constexpr uint8_t JOYSTICK_Y_PIN = 35;
constexpr unsigned long REPORT_INTERVAL_MS = 30;

void setup() {
    Serial.begin(115200);
    analogReadResolution(12);
    Serial.println("Joystick stream ready.");
}

void loop() {
    static unsigned long lastReportTime = 0;
    const unsigned long now = millis();

    if (now - lastReportTime >= REPORT_INTERVAL_MS) {
        lastReportTime = now;
        Serial.print("X: ");
        Serial.print(analogRead(JOYSTICK_X_PIN));
        Serial.print("  Y: ");
        Serial.println(analogRead(JOYSTICK_Y_PIN));
    }
}
