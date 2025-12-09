from pydub import AudioSegment


def convert_mp3_to_wav(mp3_file, output_file=None):
    """
    Converts a MP3-file in WAV with 44.1 kHz Mono.
    
    Args:
        mp3_file (str): path to the MP3-file.
        output_file (str, optional): patht to the WAV-file. If there is none, then mp3_file.wav is made.
    """
    if output_file is None:
        output_file = mp3_file.rsplit(".", 1)[0] + ".wav"
    
    audio = AudioSegment.from_mp3(mp3_file)
    audio = audio.set_frame_rate(44100).set_channels(1)
    audio.export(output_file, format="wav")
    print(f"{mp3_file} -> {output_file}")
