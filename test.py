from pydub import AudioSegment

sound = AudioSegment.from_file("./mel.mid", format="mid")
sound.export("./mel.krn", format="krn")
