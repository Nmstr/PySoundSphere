from .playback_backend.backend_loader import load_backend
import time
import os

class AudioPlayer:
    def __init__(self, playback_backend, *, debug_allow_multiple_playbacks: bool = False) -> None:
        self._debug_allow_multiple_playbacks = debug_allow_multiple_playbacks
        self._playback_backend = load_backend(playback_backend)
        self._file_path = None
        self._is_paused = False
        self._start_time = 0
        self._pause_time = 0
        self._volume = 0.5
        self._paused_at = 0
        self._paused_seconds = 0

    def load(self, file_path: str) -> None:
        """
        Load the song.
        """
        if not os.path.exists(file_path):
            raise ValueError(f'File "{file_path}" does not exist.')
        self._file_path = file_path

    def play(self) -> None:
        """
        Play the song.
        """
        if self._is_paused:
            self._playback_backend.unpause()
            self._paused_seconds += time.time() - self._paused_at
            self._is_paused = False
        elif self._playback_backend.get_busy() and not self._debug_allow_multiple_playbacks:
            raise RuntimeError('Audio is already playing.')
        else:
            if not self._file_path:
                raise ValueError('No audio file loaded.')
            self._playback_backend.load(self._file_path)
            self._playback_backend.play()
            self._start_time = time.time()

    def pause(self) -> None:
        """
        Pause the song.
        """
        if self._playback_backend.get_busy():
            self._playback_backend.pause()
            self._pause_time = time.time() - self._start_time - self._paused_seconds
            self._paused_at = time.time()
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
            return time.time() - self._start_time - self._paused_seconds
        else:
            return 0

    @position.setter
    def position(self, position: float) -> None:
        if self._playback_backend.get_busy() or self._is_paused:
            self._playback_backend.stop()
            self._playback_backend.play(start_time=position)
            self._start_time = time.time() - position
            self._paused_seconds = 0
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
        if not isinstance(volume, float):
            raise TypeError('Volume must be a float.')
        self._playback_backend.set_volume(volume)
        self._volume = volume
