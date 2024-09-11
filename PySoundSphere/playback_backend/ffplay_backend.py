import subprocess
import threading
import time

class FfplayBackend:
    def __init__(self) -> None:
        self._file_path = None
        self._playback_process = None
        self._song_started_at = 0
        self._song_stopped_at = 0
        self._song_started_ahead = 0
        self._volume = 5.0
        self._is_busy = False

    def load(self, file_path: str) -> None:
        """
        Load the song.
        """
        self._file_path = file_path

    def play(self, start_time: float = 0) -> None:
        """
        Play the song.

        Parameters:
            start_time (float): Position in the song in seconds.
        """
        self._song_started_at = time.time()
        self._song_started_ahead = start_time
        self._playback_process = subprocess.Popen(['ffplay', '-nodisp', '-autoexit', '-ss', str(start_time), '-volume', str(self._volume), self._file_path],
                                                  stdout=subprocess.DEVNULL,
                                                  stderr=subprocess.DEVNULL)
        self._is_busy = True
        threading.Thread(target=self._playback_done).start()

    def _playback_done(self):
        self._playback_process.wait()
        self._is_busy = False

    def pause(self) -> None:
        """
        Pause the song.
        """
        self._song_stopped_at = time.time()
        self._playback_process.kill()
        self._is_busy = False

    def unpause(self) -> None:
        """
        Unpause the song.
        """
        start_time = self._song_stopped_at - self._song_started_at + self._song_started_ahead
        self.play(start_time)
        self._is_busy = True

    def stop(self) -> None:
        """
        Stop the song.
        """
        self._playback_process.kill()
        self._is_busy = False

    def set_volume(self, volume: float) -> None:
        """
        Set the volume between 0 and 1.

        Parameters:
            volume (float): Volume between 0 and 1.
        """
        volume = max(0, min(round(volume * 100), 100))
        self._volume = volume
        if self._is_busy:
            self.pause()
            self.unpause()

    def get_busy(self) -> bool:
        """
        Check if the song is playing.
        """
        return self._is_busy
