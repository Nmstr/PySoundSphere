def load_backend(backend_name: str) -> object:
    """
    Load the backend.

    Parameters:
        backend_name (str): Name of the backend. Possible values:
        - sounddevice
        - pygame
        - ffplay

    Returns:
        object: Backend object.
    """
    if backend_name == "sounddevice":
        try:
            from .sounddevice_backend import SounddeviceBackend
            return SounddeviceBackend()
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
