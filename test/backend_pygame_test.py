from src.main import AudioPlayer
import tempfile
import pytest
import wave

@pytest.fixture(params=['wav'])
def audio_file(request):
    format = request.param
    with tempfile.NamedTemporaryFile(suffix=f'.{format}') as tmp_file:
        if format == 'wav':
            wav_file = wave.open(tmp_file.name, 'wb')
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(44100)
            wav_file.writeframes(b'\x00\x00' * 44100)  # 1 second of silence
            wav_file.close()
        yield tmp_file.name

def test_audio_player_play(audio_file):
    player = AudioPlayer(audio_file, 'pygame')
    player.play()
    assert player._playback_backend.get_busy() == True
    assert player._is_paused == False

def test_audio_player_pause(audio_file):
    player = AudioPlayer(audio_file, 'pygame')
    player.play()
    player.pause()
    assert player._playback_backend.get_busy() == False
    assert player._is_paused == True

def test_audio_player_stop(audio_file):
    player = AudioPlayer(audio_file, 'pygame')
    player.play()
    player.stop()
    assert player._playback_backend.get_busy() == False
    assert player._is_paused == False

def test_audio_player_position(audio_file):
    player = AudioPlayer(audio_file, 'pygame')
    player.play()
    assert player.position > 0

def test_audio_player_volume(audio_file):
    player = AudioPlayer(audio_file, 'pygame')
    assert player.volume == 1.0
    player.volume = 0.5
    assert player.volume == 0.5
