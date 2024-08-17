def load_backend(backend_name: str) -> object:
    if backend_name == "pygame":
        try:
            from .pygame_backend import PygameBackend
            return PygameBackend()
        except ImportError as e:
            raise ValueError(f'Failed to load backend "{backend_name}" with error: "{e}"')
    else:
        raise ValueError(f'Backend "{backend_name}" not found')
