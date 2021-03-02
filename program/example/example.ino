





// Starting Header 1 of ALCD
#include <LiquidCrystal_I2C.h>
// Ending Header 1 of ALCD






//Starting header 2 of ALCD_0
LiquidCrystal_I2C ALCD_0(0x27, 16, 2);
//Ending header 2 of ALCD_0

//Starting header 2 of soilmoisture_0
int soilmoisture_0 = 14;
//Ending header 2 of soilmoisture_0





    
int soilmoisture_0_SM;






// Starting Functino of ALCD
int ALCD_print(LiquidCrystal_I2C lcd, String header, float value, int row){lcd.setCursor(0, row);lcd.print(header);lcd.setCursor(header.length()+1, row+1);lcd.print(value);}
//Ending Function of ALCD



// Starting Functino of soilmoisture
int soilmoisture(int analog_pin){int range = map(analogRead(analog_pin), 0, 1024, 0, 100); return range}
//Ending Function of soilmoisture




void setup()
{


ALCD_0.begin();

ALCD_0.backlight();

}



void loop() {




soilmoisture_0_SM = soilmoisture(soilmoisture_custom_input);
            






    

}

    