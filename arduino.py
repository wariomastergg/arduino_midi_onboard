import pretty_midi
from math import *
from clipboard import *

h,l = 0,80

#int melody[] = {
#
#  NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4
#};

scale = ['C','CS','D','DS','E','F','FS','G','GS','A','AS','B']

pasta = ''

pasta1,pasta2,pasta3 = '','',''

twn,drt,nt = [],[],[]

pause_st = 0

setup = True 

midi_data = pretty_midi.PrettyMIDI('cats.mid')
print("duration:",midi_data.get_end_time())
print(f'{"note":>10} {"start":>10} {"end":>10}')
#for instrument in midi_data.instruments:
for j in range(len(midi_data.instruments)):
    instrument = midi_data.instruments[0]
    print("instrument:", instrument.program)
    for i in range(0,round(len(instrument.notes)),1):
        note = instrument.notes[i]
        if note.pitch > h:
            h = note.pitch
        if note.pitch < l:
            l = note.pitch
        print(f"NOTE_{scale[(note.pitch%12)]}{floor(note.pitch/12)},")
        

        tween = (note.start-pause_st)*1000
        if tween < 0:
            tween = 0
        twn.append(tween)
        tween = f",{round(tween)}"
        print(tween)
        pasta2 = pasta2 + tween
        

        nt.append(f"NOTE_{scale[(note.pitch%12)]}{floor(note.pitch/12)}") 
        print(f",NOTE_{scale[(note.pitch%12)]}{floor(note.pitch/12)}")
        pasta1 = pasta1 + f",NOTE_{scale[(note.pitch%12)]}{floor(note.pitch/12)}"
        #print(f'{note.pitch:10} {(note.start-note.end)*1000} ')#{note.end:10}
        


        durat = abs(((note.start-note.end)*1000))
        pause_st = note.end

        drt.append(durat)
        durat = f",{round(durat)}"
        #print(durat)
        pasta3 = pasta3 + durat
        #print(f'{note.pitch:10} {(note.start-note.end)*1000} ')#{note.end:10}
        

pasta = pasta + "int melody[] = {"+str(pasta1[1:])+"};\n" + "int noteDurations[] = {"+str(pasta3[1:])+"};\n" + "int pauseBetweenNotes[] = {"+str(pasta2[1:])+"};"



print(pasta)


print(len(twn))
print(len(drt))
print(len(nt))
#print(h,l)
copy(pasta)



#31
#33
#35
#37
#39
#41
#44
#46
#49
#52
#55
#58
#62
#65
#69
#73
#78
#82
#87
#93
#98
#104
#110
#117
#123
#131
#139
#147
#156
#165
#175
#185
#196
#208
#220
#233
#247
#262
#277
#294
#311
#330
#349
#370
#392
#415
#440
#466
#494
#523
#554
#587
#622
#659
#698
#740
#784
#831
#880
#932
#988
#1047
#1109
#1175
#1245
#1319
#1397
#1480
#1568
#1661
#1760
#1865
#1976
#2093
#2217
#2349
#2489
#2637
#2794
#2960
#3136
#3322
#3520
#3729
#3951
#4186
#4435
#4699
#4978

#0
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12
#13
#14
#15
#16
#17
#18
#19
#20
#21
#22
#23
#24
#25
#26
#27
#28
#29
#30
#31
#32
#33
#34
#35
#36
#37
#38
#39
#40
#41
#42
#43
#44
#45
#46
#47
#48
#49
#50
#51
#52
#53
#54
#55
#56
#57
#58
#59
#60
#61
#62
#63
#64
#65
#66
#67
#68
#69
#70
#71
#72
#73
#74
#75
#76
#77
#78
#79
#80
#81
#82
#83
#84
#85
#86
#87
#88