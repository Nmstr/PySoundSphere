## Getting started.

The following code is an example to get some audio playback started.

```python title="Getting it working"
import PySoundSphere
import time

player = PySoundSphere.AudioPlayer("sounddevice")
player.load("path/to/your/audio_file")
player.volume = 0.025
player.play()

time.sleep(10)
```

## Choosing a backend

Make sure to have the backend you choose installed. Further instructions can be found [here](../backends/general) and [here](../).

=== "Sounddevice"
    ```python title="Choose the sounddevice backend"
    import PySoundSphere
    player = PySoundSphere.AudioPlayer("sounddevice")
    ```

=== "Pygame"
    ```python title="Choose the pygame backend"
    import PySoundSphere
    player = PySoundSphere.AudioPlayer("pygame")
    ```

=== "ffplay"
    ```python title="Choose the ffplay backend"
    import PySoundSphere
    player = PySoundSphere.AudioPlayer("ffplay")
    ```

## Load Audio

```python title="Load audio"
import PySoundSphere
...  # A backend needs to be chosen somewhere here
player.load("path/to/your/audio_file")
```

## Play Audio

```python title="Play audio"
import PySoundSphere
...  # The audio must have been loaded somewhere here
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

## Callback function

A callback function is a function that gets executed once the current audio file finished playing.
```python title="Set a callback function"
import PySoundSphere
...
def on_audio_finished():
    # Your logic goes here
    print("Done!")
    
player.set_callback_function(on_audio_finished)
```
