def load_backend(backend_name: str, sounddevice_blocksize: int = 0) -> object:
    """
    Load the backend.

    Parameters:
        backend_name (str): Name of the backend. Possible values:
        - sounddevice
        - pygame
        - ffplay
        sounddevice_blocksize (int): The blocksize the sounddevice backend should use

    Returns:
        object: Backend object.
    """
    if backend_name == "sounddevice":
        try:
            from .sounddevice_backend import SounddeviceBackend
            return SounddeviceBackend(blocksize = sounddevice_blocksize)
        except ImportError as e:
            raise ValueError(f'Failed to load backend "{backend_name}" with error: "{e}". Is it installed?')

    elif backend_name == "pygame":
        try:
            from .pygame_backend import PygameBackend
            return PygameBackend()
        except ImportError as e:
            raise ValueError(f'Failed to load backend "{backend_name}" with error: "{e}". Is it installed?')
        
    elif backend_name == "ffplay":
        try:
            from .ffplay_backend import FfplayBackend
            return FfplayBackend()
        except ImportError as e:
            raise ValueError(f'Failed to load backend "{backend_name}" with error: "{e}". Is it installed?')

    else:
        raise ValueError(f'Backend "{backend_name}" not found')
