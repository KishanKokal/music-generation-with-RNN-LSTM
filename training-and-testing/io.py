from package.preprocess import (
    is_acceptable_song,
    transpose,
    encode_song,
    ACCEPTABLE_DURATIONS,
    SEQUENCE_LENGTH,
)
from package.melodyGenerator import MelodyGenerator
import music21 as m21
import os


def load_song():
    song = m21.converter.parse("./saregama.mid")
    return song


song = load_song()
if is_acceptable_song(song, ACCEPTABLE_DURATIONS):
    song = transpose(song)
    encoded_song = encode_song(song)
    print(encoded_song)
    mg = MelodyGenerator()
    melody = mg.generate_melody(
        seed=encoded_song,
        num_steps=500,
        # max_sequence_length=SEQUENCE_LENGTH,
        max_sequence_length=256,
        temperature=0.5,
    )
    mg.save_melody(melody)
    print(" ".join(melody))
else:
    print("Not acceptable!!!")
