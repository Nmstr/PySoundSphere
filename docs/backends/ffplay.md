---

## This backend should only be used as a fallback. 
### Due to limitations in ffplay volume can not be changed seamlessly, resulting in stutters.

---

## Installation

On most systems no further installation is required. The ffplay backend only needs `ffplay`, which is part of ffmpeg. So make sure you have ffmpeg installed.

## Usage

The backend can be used like in the following.

```python title="Setup ffplay backend"
import PySoundSphere
player = PySoundSphere.AudioPlayer("ffplay")
```
View the [general usage](../../usage/) section for more information.

## Backend specific options

The ffplay backend does not have any backend specific options.
