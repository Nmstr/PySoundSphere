import threading
import pygame
import time

class PygameBackend:
    def __init__(self) -> None:
        pygame.init()
        pygame.mixer.init()
        self._callback_function = None
        self.is_playing = False
        self.MUSIC_END_EVENT = pygame.USEREVENT + 10
        self.event_thread = threading.Thread(target=self._listen_for_callback, daemon=True)
        self.event_thread.start()

    def load(self, file_path: str) -> None:
        """
        Load the song.
        """
        pygame.mixer.music.load(file_path)

    def play(self, start_time: float = 0) -> None:
        """
        Play the song.

        Parameters:
            start_time (float): Position in the song in seconds.
        """
        pygame.mixer.music.play(start=start_time)
        self.is_playing = True
        pygame.mixer.music.set_endevent(self.MUSIC_END_EVENT)

    def pause(self) -> None:
        """
        Pause the song.
        """
        pygame.mixer.music.pause()

    def unpause(self) -> None:
        """
        Unpause the song.
        """
        pygame.mixer.music.unpause()

    def stop(self) -> None:
        """
        Stop the song.
        """
        self.is_playing = False
        pygame.mixer.music.stop()

    def set_volume(self, volume: float) -> None:
        """
        Set the volume between 0 and 1.

        Parameters:
            volume (float): Volume between 0 and 1.
        """
        pygame.mixer.music.set_volume(volume)

    def get_busy(self) -> bool:
        """
        Check if the song is playing.
        """
        return pygame.mixer.music.get_busy()

    def set_callback(self, function: callable) -> None:
        """
        Sets a single callback function to be called when the music stops.

        Parameters:
            function (callable): The callback function to be called.
        """
        self._callback_function = function

    def _listen_for_callback(self) -> None:
        """
        Listens for pygame events and triggers the callback function if needed
        """
        try:
            while True:
                for event in pygame.event.get():
                    if event.type == self.MUSIC_END_EVENT and not pygame.mixer.music.get_busy():
                        if self._callback_function:
                            self._callback_function()
                time.sleep(0.01)
        except Exception:
            """
            This error occurs when the users code ended.
            It is save to ignore.
            This is mainly here to allow the tests to run properly.
            """
