#include "pitches.h"

// the pin its outputting to
int pin = 7;




//place the values here 
int melody[] = {};
int noteDurations[] = {};
int pauseBetweenNotes[] = {};
//place the values here 


void setup() {
  
}

void loop() {
  for (int thisNote = 0; thisNote <= sizeof(melody)-1; thisNote++) {
    if (pauseBetweenNotes[thisNote] >= 0){
    delay(pauseBetweenNotes[thisNote]);
    tone(pin, melody[thisNote]);
    delay(noteDurations[thisNote]);
    noTone(pin);
    }

    }
    noTone(pin);
    loop();
  
}
