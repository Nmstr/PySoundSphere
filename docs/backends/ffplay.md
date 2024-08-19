---

## This backend should be seen as a fallback backend. 
### Due to limitations in ffplay volume can not be changed seamlessly, resulting in a minor stutter.

---

## Installation

On most systems no further installation is required. The ffplay backend only needs `ffplay`, which is part of ffmpeg. So make sure to have ffmpeg installed.

## Usage

The backend can be used like in the following.

```python title="Setup ffplay backend"
import PySoundSphere
player = PySoundSphere.AudioPlayer("path/to/your/audio_file", "ffplay")
```
