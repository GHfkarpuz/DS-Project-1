from .converter import convert_mp3_to_wav


def main():
    convert_mp3_to_wav("data/audio/song1.mp3")
    convert_mp3_to_wav("data/audio/song2.mp3")
    convert_mp3_to_wav("data/audio/song3.mp3")
    convert_mp3_to_wav("data/audio/song4.mp3")

if __name__ == "__main__":
    main()