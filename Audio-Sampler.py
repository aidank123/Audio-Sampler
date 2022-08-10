from pydub import AudioSegment #import pydub library and AudioSegment module
import sys #import system to interact with files
import os
#collecting input variables

try:
    
    #getting the input file name and turning it into an audiosegment
    input_filename = sys.argv[1] #the audio file to be chopped up
    sf = AudioSegment.from_file(input_filename)
    
    #make the directory for the chopped files (filename + _chopped)
    os.mkdir(input_filename + "_chopped")
    
    #input the bpm of the track
    bpm = int(sys.argv[2]) #the bpm of the audio file
    
    #input the number of beats you want per chop
    num_beats = int(sys.argv[3]) #the number of beats per chopped sample
        
    #handle inputting the parameters incorrectly
except:
    print("The format of this terminal command is incorrect. Check the README file for the format.")
    exit()

#length of the song in seconds
song_length = sf.duration_seconds

beats_per_second = 60/bpm  #this will give you the number of seconds in each beat, which is important in chopping the sample

iterator = 0 #iterate the loop (and the naming of the chopped sample files)

#variables that will iterate through the audio and take out each chopped section
start_sample = 0
stop_sample = beats_per_second * num_beats

#while samples have not surpassed the length of the song
while stop_sample <= song_length:
    
    #multiply by 1000 because the extraction is in milliseconds rather than seconds
    to_milli_start = 1000 * start_sample
    to_milli_stop = 1000 * stop_sample
    #extract section of audio
    extract = sf[to_milli_start:to_milli_stop]
    #export the section of audio to the folder created earlier
    extract.export( input_filename + "_chopped/clip_num" + str(iterator) +".wav", format="wav")
    
    #iterate the sampling variables as well as the iterator value
    start_sample += (beats_per_second * num_beats)
    stop_sample += (beats_per_second * num_beats)
    iterator += 1
    
     