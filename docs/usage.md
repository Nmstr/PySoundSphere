## Choosing a backend

Make sure to have the backend you choose installed. Further instructions can be found [here](../backends/general) and [here](../).

=== "Sounddevice"
    ```python title="Choose the sounddevice backend"
    import PySoundSphere
    player = PySoundSphere.AudioPlayer("path/to/your/audio_file", "sounddevice")
    ```

=== "Pygame"
    ```python title="Choose the pygame backend"
    import PySoundSphere
    player = PySoundSphere.AudioPlayer("path/to/your/audio_file", "pygame")
    ```

=== "ffplay"
    ```python title="Choose the ffplay backend"
    import PySoundSphere
    player = PySoundSphere.AudioPlayer("path/to/your/audio_file", "ffplay")
    ```

## Play Audio

```python title="Play audio using sounddevice"
import PySoundSphere
...
player.play()
...
# PySoundSphere will not play audio if your script ends immediately. 
# In the case it does, uncomment the following:
# import time
# time.sleep(60)
```

## Pause Audio

```python title="Pause audio playback"
import PySoundSphere
...
player.pause()
```

## Resume / Unpause Audio

```python title="Resume audio playback"
import PySoundSphere
...
player.play()
```

## Stop Audio

```python title="Stop audio playback"
import PySoundSphere
...
player.stop()
```

## Position

=== "Get"
    ```python title="Get current position in audio"
    import PySoundSphere
    ...
    current_position = player.position
    print(current_position)
    ```

=== "Set"
    ```python title="Set current position in audio"
    import PySoundSphere
    ...
    new_position = 60
    player.position = new_position
    ```

## Volume

=== "Get"
    ```python title="Get current volume"
    import PySoundSphere
    ...
    current_volume = player.volume
    print(current_volume)
    ```

=== "Set"
    ```python title="Set current volume"
    import PySoundSphere
    ...
    new_volume = 0.25
    player.volume = new_volume
    ```
