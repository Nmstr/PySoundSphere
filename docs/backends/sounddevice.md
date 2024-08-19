## Installation

The sounddevice backend is part of the optional dependency group `sounddevice-backend`. Either install it or install the required libraries manually.

=== "Automatic"
    ```shell title="Install with the group"
    pip install PySoundSphere[sounddevice-backend]
    ```

=== "Manual"
    ```shell title="Install the libraries manually"
    pip install PySoundSphere sounddevice soundfile numpy
    ```

## Usage

After that you can use the backend like in the following.

```python title="Setup sounddevice backend"
import PySoundSphere
player = PySoundSphere.AudioPlayer("path/to/your/audio_file", "sounddevice")
```
