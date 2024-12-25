## Change History 

This document lists all changes of `python_google_speak` with the most recent changes at the top.

### Version 0.2.2 (December 26th, 2024)

* Use `playsound3` instead of `playsound` since the latter was not longer maintained and resulted in errors
  during pip installation 
* Explicitly use temporary files with a given extension
* Restrict comparison of samples to the first 500 bytes

### Version 0.2.1 (July 3rd, 2022)

* Remove fixed dependencies for PIP packages

### Version 0.2.0 (June 18th, 2022)

* Remove package `pygi` from requirements
* Read requirements and long package description from files 
* Update test mpgs to reflect current Google speech synthesis
* Correct test cases (separate German and English test cases)
* Remove Eclipse configuration file
* Supply `.gitlab-ci.yaml`
* Update `.circleci/config.yml`
* Optionally skip test case for audio comparison using `SKIP_AUDIO_COMPARISON` 
* Switch to package manager `poetry`
* Push wheel to PyPi

### Version 0.1 (September 18th, 2018)

*   Initial full version
