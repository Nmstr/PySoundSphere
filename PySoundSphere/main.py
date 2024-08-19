from .playback_backend.backend_loader import load_backend
import time

class AudioPlayer:
    def __init__(self, _file_path: str, playback_backend) -> None:
        self._playback_backend = load_backend(playback_backend)
        self._file_path = _file_path
        self._is_paused = False
        self._start_time = 0
        self._pause_time = 0
        self._volume = 1.0

    def play(self) -> None:
        """
        Play the song.
        """
        if self._is_paused:
            self._playback_backend.unpause()
            self._is_paused = False
        else:
            self._playback_backend.load(self._file_path)
            self._playback_backend.play()
            self._start_time = time.time()

    def pause(self) -> None:
        """
        Pause the song.
        """
        if self._playback_backend.get_busy():
            self._playback_backend.pause()
            self._pause_time = time.time() - self._start_time
            self._is_paused = True

    def stop(self) -> None:
        """
        Stop the song.
        """
        if self._playback_backend.get_busy():
            self._playback_backend.stop()
            self._is_paused = False
            self._pause_time = 0

    @property
    def position(self) -> float:
        """
        Position in the song in seconds.
        """
        if self._is_paused:
            return self._pause_time
        elif self._playback_backend.get_busy():
            return time.time() - self._start_time
        else:
            return 0

    @position.setter
    def position(self, position: float) -> None:
        if self._playback_backend.get_busy() or self._is_paused:
            self._playback_backend.stop()
            self._playback_backend.play(start_time=position)
            self._start_time = time.time() - position
            if self._is_paused:
                self._playback_backend.pause()

    @property
    def volume(self) -> float:
        """
        Volume from 0 to 1.
        """
        return self._volume

    @volume.setter
    def volume(self, volume: float) -> None:
        self._playback_backend.set_volume(volume)
        self._volume = volume
