# PySoundSphere

PySoundSphere is a high level audio playback library written in python.

---

# Installation

The installation process is straight forward. Most people will want to install the `sounddevice` [backend](./backends/general/). You can always install any backend later as well.

=== "Sounddevice"
    ```shell title="Install with the sounddevice backend"
    pip install PySoundSphere[sounddevice-backend]
    ```

=== "Pygame"
    ```shell title="Install with the pygame backend"
    pip install PySoundSphere[pygame-backend]
    ```

=== "ffplay"
    ```shell title="Install with the ffplay backend"
    pip install PySoundSphere
    ```
