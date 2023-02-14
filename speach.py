from TTS.utils.manage import ModelManager
from TTS.utils.synthesizer import Synthesizer
import wave

path = r"C:\Users\Mark\PycharmProjects\AI_youtube_creator\venv\Lib\site-packages\TTS/.models.json"

model_manager = ModelManager(path)

model_path, config_path, model_item = model_manager.download_model("tts_models/en/ljspeech/vits--neon")

if model_item.get("default_vocoder"):
    voc_path, voc_config_path, _ = model_manager.download_model(model_item["default_vocoder"])

    syn = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
        vocoder_checkpoint=voc_path,
        vocoder_config=voc_config_path
    )
else:
    syn = Synthesizer(
        tts_checkpoint=model_path,
        tts_config_path=config_path,
    )


def make_voice(text_dub, filename="voice-audio.wav"):
    outputs = syn.tts(text_dub)
    syn.save_wav(outputs, filename)
    with wave.open(filename) as mywav:
        return round(mywav.getnframes() / mywav.getframerate())



if __name__ == "__main__":
    text = """
    The veteran tech company is reorganising its advertising unit, which will lose more than half of the department by the end of the year.
    """
    print(make_voice(text))

