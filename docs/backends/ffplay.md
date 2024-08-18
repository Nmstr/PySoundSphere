---

## This backend should be seen as a fallback backend. 
### Due to limitations in ffplay volume can not be changed seamlessly, resulting in a minor stutter.

---

The ffplay backend only needs `ffplay`, which is part of ffmpeg.

It can be used like this.

```python title="Setup ffplay backend"
from src.main import AudioPlayer
player = AudioPlayer("path/to/your/audio_file", "ffplay")
```
