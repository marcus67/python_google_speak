# python_google_speak

This is a little Python module that uses a Google Translate online web service to convert short 
texts into high quality MP3 tracks.

## Source Repository ##

See https://github.com/marcus67/python_google_speak

## Sample Usage ##
<PRE>
from python_google_speak import speech_generator
from python_google_speak import speech_output

sound_generator = speech_generator.SpeechGenerator(p_locale="en_US")
sound_data = sound_generator.generate_audio_data("hello.")
speech_output.playback_audio_data(sound_data) 

</PRE>

## Caveats ##
* Google limits the length of the text to a few hundred characters.
* The library `playsound` which is used by `speech_output` has issues when called from within 
a virtual environment.

## Command Line Interface

The tool can be called from the command line as follows:

<PRE>
# To output to the standard audio device:
> google_speak --locale "en_US" "hello!"

# To write audio data to a file
> google_speak --locale "en_US" --outfile "hello.mp3" "hello!"
</PRE>
