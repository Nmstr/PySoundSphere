## Play Audio

=== "Sounddevice"
    ```python title="Play audio using sounddevice"
    from src.main import AudioPlayer

    player = AudioPlayer("path/to/your/audio_file", "sounddevice")
    player.play()
    ```

=== "Pygame"
    ```python title="Play audio using pygame"
    from src.main import AudioPlayer

    player = AudioPlayer("path/to/your/audio_file", "pygame")
    player.play()
    ```

## Pause Audio

=== "All"
    ```python title="Pause audio playback"
    from src.main import AudioPlayer
    ...
    player.pause()
    ```

## Resume / Unpause Audio

=== "All"
    ```python title="Resume audio playback"
    from src.main import AudioPlayer
    ...
    player.play()
    ```

## Stop Audio

=== "All"
    ```python title="Stop audio playback"
    from src.main import AudioPlayer
    ...
    player.stop()
    ```

## Position

=== "Get"
    ```python title="Get current position in audio"
    from src.main import AudioPlayer
    ...
    current_position = player.position
    print(current_position)
    ```

=== "Set"
    ```python title="Set current position in audio"
    from src.main import AudioPlayer
    ...
    new_position = 60
    player.position = new_position
    ```

## Volume

=== "Get"
    ```python title="Get current volume"
    from src.main import AudioPlayer
    ...
    current_volume = player.volume
    print(current_volume)
    ```

=== "Set"
    ```python title="Set current volume"
    from src.main import AudioPlayer
    ...
    new_volume = 0.25
    player.volume = new_volume
    ```
