# -*- coding: utf-8 -*-
# This file is part of https://github.com/marcus67/python_google_speak

import sys
import argparse
import io

from python_google_speak import speech_generator
from python_google_speak import speech_output

def get_parser():

    parser = argparse.ArgumentParser()
    parser.add_argument("--locale", help="Locale to be used for speech generation", default="en_US")
    parser.add_argument("texts", nargs="+")
    parser.add_argument("--outfile", help="filename to be used to store the audio data in (otherwise it will be sent to the default audio device)")

    return parser.parse_args()

def main():

    try:
        arguments = get_parser()

        generator = speech_generator.SpeechGenerator(p_locale=arguments.locale)

        for text in arguments.texts:

            audio_blob = generator.generate_audio_data(p_text=text)

            if arguments.outfile is not None:
                with io.open(arguments.outfile, "wb") as f:
                    f.write(audio_blob)

            else:
                speech_output.playback_audio_data(p_audio_blob=audio_blob)

    except Exception as e:
        sys.stderr.write("ERROR '{}' while processing texts".format(str(e)))

if __name__ == '__main__':
    sys.exit(main())
