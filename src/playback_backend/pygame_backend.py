import pygame

class PygameBackend:
    def __init__(self):
        pygame.mixer.init()

    def load(self, file_path: str):
        """
        Load the song.
        """
        pygame.mixer.music.load(file_path)

    def play(self, start_time: float = 0):
        """
        Play the song.

        Parameters:
            start_time (float): Position in the song in seconds.
        """
        pygame.mixer.music.play(start=start_time)

    def pause(self):
        """
        Pause the song.
        """
        pygame.mixer.music.pause()

    def unpause(self):
        """
        Unpause the song.
        """
        pygame.mixer.music.unpause()

    def stop(self):
        """
        Stop the song.
        """
        pygame.mixer.music.stop()

    def set_volume(self, volume: float):
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
