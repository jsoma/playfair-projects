// **************
// Include for WLAN
// **************

#include <ESP8266WiFi.h>

const char* ssid1     = "Columbia University";
const char* password1 = "";
const char* ssid2     = "Mathiass iPhone";
const char* password2 = "usenet11";

const char* host = "borniert.com";
const char* streamId   = "templog.php";


// **************
// Include for the Sensor
// **************

#include <Arduino.h>
#include <Wire.h>
#include "Adafruit_SHT31.h"

Adafruit_SHT31 sht31 = Adafruit_SHT31();

#if defined(ARDUINO_ARCH_SAMD)
// for Zero, output on USB Serial console, remove line below if using programming port to program the Zero!
   #define Serial SerialUSB
#endif

// **************
// Include for the Clock
// **************

#include "RTClib.h"

#if defined(ARDUINO_ARCH_SAMD)
// for Zero, output on USB Serial console, remove line below if using programming port to program the Zero!
   #define Serial SerialUSB
#endif

RTC_Millis rtc;

// **************
// Definition for noise level monitoring
// **************

const int sampleWindow = 25; // Sample window width in mS (50 mS = 20Hz)
unsigned int sample;

void setup() {

// **************
// Setup for WLAN
// **************

  Serial.begin(57600);
  delay(10);

  // We start by connecting to a WiFi network

  Serial.println();
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid2);

  
  WiFi.begin(ssid2, password2);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");  
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());

int value = 0;

// **************
// Setup for the Sensor
// **************

#ifndef ESP8266
  while (!Serial);     // will pause Zero, Leonardo, etc until serial console opens
#endif
  Serial.println("SHT31 test");
  if (! sht31.begin(0x44)) {   // Set to 0x45 for alternate i2c addr
    Serial.println("Couldn't find SHT31");
    while (1) delay(1);
  }

// **************
// Setup for the Clock
// **************

    rtc.begin(DateTime(F(__DATE__), F(__TIME__)));
}

void loop() {

// **************
// Read the values from the sensor
// **************
  
  float temp = sht31.readTemperature();
  float humidity = sht31.readHumidity();
  
  // Get the date and time

  DateTime now = rtc.now();
  char dt[16];
  char tm[16];

  sprintf(dt, "%02d-%02d-%02d", now.year(),now.month(),now.day());
  sprintf(tm, "%02d:%02d:%02d", now.hour(),now.minute(),now.second());


// **************
// Mesure the noise level
// **************

   unsigned long startMillis= millis();  // Start of sample window
   unsigned int peakToPeak = 0;   // peak-to-peak level

   unsigned int signalMax = 0;
   unsigned int signalMin = 1024;

   // collect data for 50 mS
   while (millis() - startMillis < sampleWindow)
   {
      sample = analogRead(0);
      if (sample < 1024)  // toss out spurious readings
      {
         if (sample > signalMax)
         {
            signalMax = sample;  // save just the max levels
         }
         else if (sample < signalMin)
         {
            signalMin = sample;  // save just the min levels
         }
      }
   }
   peakToPeak = signalMax - signalMin;  // max - min = peak-peak amplitude
   double volts = (peakToPeak * 3.3) / 1024;  // convert to volts

   float noise = (100 * volts);
   Serial.println(100 * volts);

// **************
// Send the data over the Wifi to the server
// **************

  Serial.print("connecting to ");
  Serial.println(host);
  
  // Use WiFiClient class to create TCP connections
  WiFiClient client;
  const int httpPort = 80;
  if (!client.connect(host, httpPort)) {
    Serial.println("connection failed");
    return;
  }

  // We now create a URI for the request
  String url = "/tourilogger/";
  url += streamId;
  url += "?date=";
  url += dt;
  url += "_";
  url += tm;
  url += "&temp=";
  url += temp;
  url += "&humidity=";
  url += humidity;
  url += "&noise=";
  url += noise;

  Serial.print("Requesting URL: ");
  Serial.println(url);
  
  // This will send the request to the server
  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
               "Host: " + host + "\r\n" + 
               "Connection: close\r\n\r\n");
  unsigned long timeout = millis();
  while (client.available() == 0) {
    if (millis() - timeout > 5000) {
      Serial.println(">>> Client Timeout !");
      client.stop();
      return;
    }
  }
  
  // Read all the lines of the reply from server and print them to Serial
  while(client.available()){
    String line = client.readStringUntil('\r');
    Serial.print(line);
  }
  
  Serial.println();
  Serial.println("closing connection");

  delay(27300);
}
