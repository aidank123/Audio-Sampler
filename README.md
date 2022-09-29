This project is to be used for chopping up audio into smaller segments, based upon the projects bpm, length, and desired audio segment length (all in seconds). It should chop the song up on beat and to the desired length of each segment. This is useful for sampling songs in music projects. The example wav file provided and the folder containing the chopped up audio are just an example of how the script will handle the files. It will take in the original file and create a folder in the same directory containing a numbered list of all the audio segments, all labeled with the name of the original audio file.

DEPENDENCIES:

-pydub library


COMMAND LINE:

Example formatting for the terminal command that will run the script and chop up the audio file:

	python3 Audio-Sampler.py {audio file} {bpm of the song} {length of audio segment}
