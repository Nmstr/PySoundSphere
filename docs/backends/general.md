# Playback Backends

---

## What are playback backends?

Playback backends determine which libraries will be used to actually play the sounds. PySoundSphere currently supports `sounddevice` and `pygame`, with plans to later add support for `PyAudio` and `ffplay`. Each backend has different requirements.

## Which one should I use?

This depends on your specific use case. If you are already using any of the required libraries, it will probably be best to go with that backend. For example, if your application already uses pygame, you should go with the pygame backend.
