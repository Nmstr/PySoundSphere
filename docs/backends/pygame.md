The pygame backend only needs `pygame` in order to run. Run the following command to install it.

```shell title="Install requirements for pygame backend"
pip install pygame
```

After that you can set up your backend like in the following.

```python title="Setup pygame backend"
from src.main import AudioPlayer
player = AudioPlayer("path/to/your/audio_file", "pygame")
```
