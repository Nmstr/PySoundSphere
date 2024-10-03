## Installation

The pygame backend is part of the optional dependency group `pygame-backend`. Either install it or install the required libraries manually.

=== "Automatic"
    ```shell title="Install with the group"
    pip install PySoundSphere[pygame-backend]
    ```

=== "Manual"
    ```shell title="Install the libraries manually"
    pip install PySoundSphere pygame
    ```

## Usage

After that you can use the backend like in the following.

```python title="Setup pygame backend"
import PySoundSphere
player = PySoundSphere.AudioPlayer("pygame")
```
View the [general usage](../../usage/) section for more information.

## Backend specific options

The pygame backend does not have any backend specific options.
