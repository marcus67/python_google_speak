# python_google_speak
This is a little Python module that uses a Google Translate online web service to convert short 
texts into high quality MP3 tracks.

## Source Repository ##

See https://github.com/marcus67/python_google_speak

## CircleCI Continuous Integration Status

<A HREF="https://circleci.com/gh/marcus67/python_google_speak/tree/master"><IMG SRC="https://img.shields.io/circleci/project/github/marcus67/python_google_speak.svg?label=Python3%20master"></A> 

## GitHub Status

<A HREF="https://github.com/marcus67/python_google_speak"><IMG SRC="https://img.shields.io/github/forks/marcus67/python_google_speak.svg?label=forks"></A> <A HREF="https://github.com/marcus67/python_google_speak/stargazers"><IMG SRC="https://img.shields.io/github/stars/marcus67/python_google_speak.svg?label=stars"></A> <A HREF="https://github.com/marcus67/python_google_speak/watchers"><IMG SRC="https://img.shields.io/github/watchers/marcus67/python_google_speak.svg?label=watchers"></A> <A HREF="https://github.com/marcus67/python_google_speak/issues"><IMG SRC="https://img.shields.io/github/issues/marcus67/python_google_speak.svg"></A> <A HREF="https://github.com/marcus67/python_google_speak/pulls"><IMG SRC="https://img.shields.io/github/issues-pr/marcus67/python_google_speak.svg"></A>
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
