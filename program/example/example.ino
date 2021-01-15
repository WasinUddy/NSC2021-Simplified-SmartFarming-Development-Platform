
    


#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C 16x2-I2C-LCD_0(0x27, 16, 2);
#include <OneWire.h>
#include <DallasTemperature.h>
OneWire oneWire(0);
DallasTemperature DS18B20_0(&oneWire);#include <DHT.h>
DHT DHT11_0(1, DHT11);#include <DHT.h>
DHT DHT22_0(2, DHT22);

    
float DS18B20_0_Temperature;

float DHT11_0_Temperature;

float DHT11_0_Humidity;

float DHT22_0_Temperature;

float DHT22_0_Humidity;

void setup()
{

DS18B20.begin();
DHT11_0.begin();
dht12_sensor_id.begin();

pinMode(3, OUTPUT);


pinMode(4, OUTPUT);


pinMode(5, OUTPUT);

}
    

void lcd16x2_print(LiquidCrystal lcd, String header, float value, int row){lcd.setCursor(0, row);lcd.print(header);lcd.setCursor(0, length(header)+1);lcd.print(value);lcd.clear();}float DS1820B_readTemperature(DallasTemperature DS18B20_sensor_id){DS18B20.requestTemperatures();return DS18B20.getTempCByIndex(0);}float dht11_readTemperature(DHT dht11_sensor){float t = dht11_sensor.readTemperature(); if(isnan(t)){return;}else{return t;}}
float dht11_readHumidity(DHT dht11_sensor){float h = dht11_sensor.readHumidity(); if(isnan(h)){return;}else{return h;}}
float dht22_readTemperature(DHT dht22_sensor){float t = dht22_sensor.readTemperature(); if(isnan(t)){return;}else{return t;}}float dht22_readHumidity(DHT dht22_sensor){float h = dht22_sensor.readHumidity(); if(isnan(h)){return;}else{return h;}}
void loop(){
    


DS18B20_0_Temperature = DS1820B_readTemperature(DS1820_sensor_id);
            
DHT11_0_Temperature = dht11_readTemperature(DHT11_0);
            
DHT11_0_Humidity = dht11_readHumidity(DHT11_0);
            
DHT22_0_Temperature = dht22_readTemperature(DHT22_0);
            
DHT22_0_Humidity = dht22_readHumidity(DHT22_0);
            

//Start of Condition : 0
        
if (DS18B20_0_Temperature > 50)
{
digitalWrite(3, HIGH);
        
}else{

digitalWrite(3, LOW);
        
}

//End of Condition : 0

//Start of Condition : 1
        
if (DS18B20_0_Temperature > 30)
{
digitalWrite(4, HIGH);
        
}else{

digitalWrite(4, LOW);
        
}

//End of Condition : 1

//Start of Condition : 2
        
if (DS18B20_0_Temperature == 30)
{
digitalWrite(5, HIGH);
        
}else{

digitalWrite(5, LOW);
        
}

//End of Condition : 2

}
    