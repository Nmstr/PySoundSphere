# Playback Backends

---

## What are playback backends?

Playback backends determine which libraries will be used to actually play the sounds. PySoundSphere currently supports `sounddevice`, `pygame` and `ffplay`, with plans to later add support for `PyAudio` as well. Each backend has different requirements and different advantages/disadvantages. The vast majority of features is shared between all backends. Some more specific options are only available in certain backends though. More information about that can be found on their own pages.

## Which one should I use?

Generally it is recommended to use `sounddevice`. If you encounter problems with it, or you already use `pygame` somewhere in your project, it might be better to use that instead. `ffplay` is only meant as a fallback when nothing else works and thus should be avoided. There is more information on their dedicated pages. Links to the pages are listed below, or can be found on the left-hand side.

## How can I install them?

For each backend there is a dedicated page. Installation instructions can be found on there. Alternatively you will most likely have installed one backend during the installation PySoundSphere itself. Here are the links for all the dedicated pages:

- [sounddevice backend](../sounddevice)
- [sounddevice pygame](../pygame)
- [sounddevice ffplay](../ffplay)
