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
If audio playback is paused while a new song is being loaded, it must first be stopped for the new song to be played. Otherwise, the old song will resume playing the next time `play` is called.

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

## Played Time

Played time is the time the current song has been playing for, with disregard to the current songs position.

```python title="Get the time audio has played for"
import PySoundSphere
...
played_time = player.played_time
print(played_time)
```

It is important to distinguish played_time from position. The difference is made clear in the following example.

=== "Played Time"
    ```python title="Example using played time"
    import PySoundSphere
    import time
    player = PySoundSphere.AudioPlayer("sounddevice")
    player.load("path/to/your/audio_file")
    player.play()
    player.position = 10
    time.sleep(1)

    print(player.played_time)
    # This will print 1
    ```

=== "Position"
    ```python title="Example using position"
    import PySoundSphere
    import time
    player = PySoundSphere.AudioPlayer("sounddevice")
    player.load("path/to/your/audio_file")
    player.play()
    player.position = 10
    time.sleep(1)

    print(player.position)
    # This will print 11
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
