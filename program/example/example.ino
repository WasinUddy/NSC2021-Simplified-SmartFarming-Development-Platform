





// Starting Header 1 of ALCD
#include <LiquidCrystal_I2C.h>
// Ending Header 1 of ALCD



// Starting Header 1 of DHT11
#include <DHT.h>
// Ending Header 1 of DHT11






//Starting header 2 of ALCD_0
LiquidCrystal_I2C ALCD_0(0x27, 16, 2);
//Ending header 2 of ALCD_0

//Starting header 2 of DHT11_0
DHT DHT11_0(0, DHT11);
//Ending header 2 of DHT11_0





    
float DHT11_0_Temperature;

float DHT11_0_Humidity;

int soilmoisture_0_SM;






// Starting Functino of ALCD
int ALCD_print(LiquidCrystal_I2C lcd, String header, float value, int row){lcd.setCursor(0, row);lcd.print(header);lcd.setCursor(header.length()+1, row+1);lcd.print(value);}
//Ending Function of ALCD



// Starting Functino of DHT11
float dht11_readTemperature(DHT dht11_sensor){float t = dht11_sensor.readTemperature(); if(isnan(t)){return;}else{return t;}}

//Ending Function of DHT11



// Starting Functino of DHT11
float dht11_readHumidity(DHT dht11_sensor){float h = dht11_sensor.readHumidity(); if(isnan(h)){return;}else{return h;}}

//Ending Function of DHT11



// Starting Functino of soilmoisture
int SM(int analog_pin){int range = map(analogRead(analog_pin), 0, 1024, 0, 100); return range
//Ending Function of soilmoisture




void setup()
{


ALCD_0.begin();

ALCD_0.backlight();

DHT11_0.begin();

}



void loop() {




DHT11_0_Temperature = dht11_readTemperature(DHT11_0);
            
DHT11_0_Humidity = dht11_readHumidity(DHT11_0);
            
soilmoisture_0_SM = SM(sm_custom_input);
            






    

}

    