from PySoundSphere.main import AudioPlayer
import pytest

@pytest.fixture(params=['wav', 'mp3', 'flac'])
def audio_file(request):
    format = request.param
    base_file_name = "test/audio_files/75hz_stereo"
    yield base_file_name + "." + format

def test_audio_player_play(audio_file: str) -> None:
    player = AudioPlayer('pygame', debug_allow_multiple_playbacks=True)
    player.load(audio_file)
    player.play()
    assert player._playback_backend.get_busy() == True
    assert player._is_paused == False

def test_audio_player_pause(audio_file: str) -> None:
    player = AudioPlayer('pygame', debug_allow_multiple_playbacks=True)
    player.load(audio_file)
    player.play()
    player.pause()
    assert player._playback_backend.get_busy() == False
    assert player._is_paused == True

def test_audio_player_stop(audio_file: str) -> None:
    player = AudioPlayer('pygame', debug_allow_multiple_playbacks=True)
    player.load(audio_file)
    player.play()
    player.stop()
    assert player._playback_backend.get_busy() == False
    assert player._is_paused == False

def test_audio_player_position(audio_file: str) -> None:
    player = AudioPlayer('pygame', debug_allow_multiple_playbacks=True)
    player.load(audio_file)
    player.play()
    assert player.position > 0

def test_audio_player_volume(audio_file: str) -> None:
    player = AudioPlayer('pygame', debug_allow_multiple_playbacks=True)
    assert player.volume == 0.5
    player.volume = 0.25
    assert player.volume == 0.25

def test_audio_player_volume_running(audio_file: str) -> None:
    player = AudioPlayer('pygame', debug_allow_multiple_playbacks=True)
    player.load(audio_file)
    player.play()
    assert player.volume == 0.5
    player.volume = 0.25
    assert player.volume == 0.25
