import sounddevice as sd
import soundfile as sf

class SounddeviceBackend:
    def __init__(self, blocksize: int = 0) -> None:
        self._data = None
        self._original_data = None
        self._samplerate = None
        self._stream = None
        self._volume = 0.5
        self._is_busy = False
        self._block_size = blocksize
    
    def load(self, file_path: str) -> None:
        """
        Load the song.

        Parameters:
            file_path (str): Path to the song.
        """
        self._original_data, self._samplerate = sf.read(file_path, dtype='float32')

    def pause(self) -> None:
        """
        Pause the song.
        """
        if self._stream is not None:
            self._stream.stop()
            self._is_busy = False

    def unpause(self) -> None:
        """
        Unpause the song.
        """
        if self._stream is not None:
            self._stream.start()
            self._is_busy = True

    def play(self, start_time: float = 0) -> None:
        """
        Play the song.

        Parameters:
            start_time (float): Position in the song in seconds.
        """
        start_frame = int(start_time * self._samplerate)
        self._data = self._original_data[start_frame:]
        self._stream = sd.OutputStream(
            callback=self._audio_callback,
            samplerate=self._samplerate,
            channels=self._data.shape[1],
            blocksize=self._block_size)
        self._stream.start()
        self._is_busy = True

    def stop(self) -> None:
        """
        Stop the song.
        """
        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None
            self._is_busy = False

    def set_volume(self, new_volume: float) -> None:
        """
        Set the volume between 0 and 1.

        Parameters:
            volume (float): Volume between 0 and 1.
        """
        self._volume = new_volume
    
    def get_busy(self) -> bool:
        """
        Check if the song is playing.
        """
        return self._is_busy
    
    def _audio_callback(self, outdata, frames, time, status) -> None:
        """
        Callback function for sounddevice.
        """
        if status:
            print(status)
        if self._data is not None:
            if len(self._data) < frames:
                outdata[:len(self._data)] = self._volume * self._data
                outdata[len(self._data):] = 0
                self._is_busy = False
            else:
                outdata[:] = self._volume * self._data[:frames]
                self._data = self._data[frames:]
