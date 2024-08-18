# Playback Backends

---

## What are playback backends?

Playback backends determine which libraries will be used to actually play the sounds. PySoundSphere currently supports `sounddevice`, `pygame` and `ffplay`, with plans to later add support for `PyAudio` as well. Each backend has different requirements and different advantages/disadvantages.

## Which one should I use?

Generally it is recommended to use `sounddevice`. If you encounter problems with it or you already use `pygame` somewhere in your project, it might be better to use that instead. `ffplay` is only meant as a fallback when nothing else works and thus should be avoided. There is more information on its dedicated [page](../ffplay).
