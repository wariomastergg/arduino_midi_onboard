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


                                                                                                                                                             
  ,,..                                                                                                                                                       
,6P`'Yb.     `7MMM.     ,MMF'`7MMF'  .g8"""bgd       db      `7MMF'  `7MMF' .M"""bgd   .g8""8q.   `7MM"""YMM MMP""MM""YMM     `7MMF'`7MN.   `7MF'  .g8"""bgd 
6M'  `Mb       MMMb    dPMM    MM  .dP'     `M      ;MM:       MM      MM  ,MI    "Y .dP'    `YM.   MM    `7 P'   MM   `7       MM    MMN.    M  .dP'     `M 
MM    MM       M YM   ,M MM    MM  dM'       `     ,V^MM.      MM      MM  `MMb.     dM'      `MM   MM   d        MM            MM    M YMb   M  dM'       ` 
MM""""MM       M  Mb  M' MM    MM  MM             ,M  `MM      MMmmmmmmMM    `YMMNq. MM        MM   MM""MM        MM            MM    M  `MN. M  MM          
YM    JM'      M  YM.P'  MM    MM  MM.            AbmmmqMA     MM      MM  .     `MM MM.      ,MP   MM   Y        MM            MM    M   `MM.M  MM.         
`M.  ,M9       M  `YM'   MM    MM  `Mb.     ,'   A'     VML    MM      MM  Mb     dM `Mb.    ,dP'   MM            MM            MM    M     YMM  `Mb.     ,' 
 `YbdP'      .JML. `'  .JMML..JMML.  `"bmmmd'  .AMA.   .AMMA..JMML.  .JMML.P"Ybmmd"    `"bmmd"'   .JMML.        .JMML.        .JMML..JML.    YM    `"bmmmd'  
