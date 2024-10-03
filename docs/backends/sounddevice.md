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
player = PySoundSphere.AudioPlayer("sounddevice")
```
View the [general usage](../../usage/) section for more information.

## Backend specific options

The following sections will cover all backend specific options available in the sounddevice backend.

### blocksize

The `sounddevice_blocksize` parameter is the size of the buffer the audio stream uses.

The default value `sounddevice_blocksize=0` is special, as it will use a (possibly varying) buffer size based on requirements of the host system.

On some systems and configurations the default value may cause issues. For example, there have been issues with stuttering audio when the playback was started while other applications were already using the audio device. This can often be fixed by increasing the blocksize.

Additional information:

```python title="Setup sounddevice backend with blocksize of 1024"
import PySoundSphere
player = PySoundSphere.AudioPlayer("sounddevice", sounddevice_blocksize=1024)
```

| Small Blocksize  | Larger Blocksize |
|------------------|------------------|
| Lower Latency    | Higher Latency   |
| Higher CPU Usage | Lower CPU Usage  |
