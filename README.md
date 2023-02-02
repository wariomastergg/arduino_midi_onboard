# arduino_midi_onboard

you need python3, arduinoIDE and maybe a midi editor http://www.midieditor.org/ is a good one

put this stuff in the terminal before use:

pip install pretty_midi

pip install clipboard


make sure the midi youre using has no more than one note playing at at time
place the midi you want to use in the same dir as the python file name "arduino" and change the name of the string labeled in the comments to the name of the midi.
after you run the script, the info should be put onto your clipboard

after that make an arduino sketch using "my_tones.ino" and "tones.h".

paste the automaticailly copied data onto the labeles area in the INO file.
assuming your midi only plays one note at a time on channel 0, it should work albeit a little buggy, i kinda made it in 2 days.


put this stuff in the terminal before use:

pip install pretty_midi

pip install clipboard


                                                                                                                                                             

   ___      __  __   _____    _____              _    _    _____    ____    ______   _______     _____   _   _    _____ 
  / _ \    |  \/  | |_   _|  / ____|     /\     | |  | |  / ____|  / __ \  |  ____| |__   __|   |_   _| | \ | |  / ____|
 | |_| |   | \  / |   | |   | |         /  \    | |__| | | (___   | |  | | | |__       | |        | |   |  \| | | |     
 |  _  |   | |\/| |   | |   | |        / /\ \   |  __  |  \___ \  | |  | | |  __|      | |        | |   | . ` | | |     
 | |_| |   | |  | |  _| |_  | |____   / ____ \  | |  | |  ____) | | |__| | | |         | |       _| |_  | |\  | | |____ 
  \___/    |_|  |_| |_____|  \_____| /_/    \_\ |_|  |_| |_____/   \____/  |_|         |_|      |_____| |_| \_|  \_____|
  
  
  
                                                                                                                       
                                                                                                                        
                                                                                                                        

