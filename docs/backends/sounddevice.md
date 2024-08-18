The sounddevice backend needs `sounddevice`, `soundfile` and `numpy` in order to run. Run the following command to install these.

```shell title="Install requirements for sounddevice backend"
pip install sounddevice soundfile numpy
```

After that you can set up your backend like in the following.

```python title="Setup sounddevice backend"
from src.main import AudioPlayer
player = AudioPlayer("path/to/your/audio_file", "sounddevice")
```
