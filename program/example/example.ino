
    
#include <DHT.h>
DHT DHT11_0(0, DHT11);
DHT DHT11_1(1, DHT11);

    
float DHT11_0_Temperature;

float DHT11_0_Humidity;

float DHT11_1_Temperature;

float DHT11_1_Humidity;

void setup()
{

DHT11_0.begin();
DHT11_1.begin();

pinMode(2, OUTPUT);


pinMode(3, OUTPUT);

}
    
    float dht11_readTemperature(DHT dht11_sensor){float t = dht11_sensor.readTemperature(); if(isnan(t)){return;}else{return t;}}
float dht11_readHumidity(DHT dht11_sensor){float h = dht11_sensor.readHumidity(); if(isnan(h)){return;}else{return h;}}

void loop(){
    


DHT11_0_Temperature = dht11_readTemperature(DHT11_0);
            
DHT11_0_Humidity = dht11_readHumidity(DHT11_0);
            
DHT11_1_Temperature = dht11_readTemperature(DHT11_1);
            
DHT11_1_Humidity = dht11_readHumidity(DHT11_1);
            

//Start of Condition : 0
        
if (DHT11_0_Temperature > 1)
{
digitalWrite(2, HIGH);
        
}else{

digitalWrite(2, LOW);
        
}

//End of Condition : 0

}
    