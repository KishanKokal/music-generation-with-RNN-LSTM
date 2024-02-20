import os
import music21 as m21
import json
import tensorflow.keras as keras
import numpy as np

DATASET_PATH = "deutschl/erk"
SAVE_DIR = "data"
SINGLE_FILE_DATASET = "file_dataset"
SEQUENCE_LENGTH = 64
MAPPING_PATH = "mapping.json"
ACCEPTABLE_DURATIONS = [
    0.25,
    0.5,
    0.75,
    1.0,
    1.5,
    2,
    3,
    4,
]


def load_songs(dataset_path):
    songs = []
    for path, subdirs, files in os.walk(dataset_path):
        for file in files:
            if file[-3:] == "krn":
                song = m21.converter.parse(os.path.join(dataset_path, file))
                songs.append(song)
    song = songs[3]
    song.show()
    return songs


def is_acceptable_song(song, acceptable_durations):
    for note in song.flat.notesAndRests:
        if note.duration.quarterLength not in acceptable_durations:
            return False
    return True


def transpose(song):
    # Get key from the song
    parts = song.getElementsByClass(m21.stream.Part)
    measures_part0 = parts[0].getElementsByClass(m21.stream.Measure)
    key = measures_part0[0][4]

    # Estimate key using music21
    if not isinstance(key, m21.key.Key):
        key = song.analyze("key")

    # Get interval for transposition. E.g., Bmaj -> Cmaj
    if key.mode == "major":
        interval = m21.interval.Interval(key.tonic, m21.pitch.Pitch("C"))
    elif key.mode == "minor":
        interval = m21.interval.Interval(key.tonic, m21.pitch.Pitch("A"))

    # Transpose song by calculated interval
    tranposed_song = song.transpose(interval)

    return tranposed_song


def encode_song(song, time_step=0.25):
    # p = 60, d = 1.0 -> [60, "_", "_", "_"]
    encoded_song = []

    for event in song.flat.notesAndRests:
        if isinstance(event, m21.note.Note):
            symbol = event.pitch.midi
        elif isinstance(event, m21.note.Rest):
            symbol = "r"

        # Convert the note/rest into time series notation
        steps = int(event.duration.quarterLength / time_step)
        for i in range(steps):
            if i == 0:
                encoded_song.append(symbol)
            else:
                encoded_song.append("_")

    return " ".join(map(str, encoded_song))


def preprocess(dataset_path):
    print("Loading songs...")
    songs = load_songs(dataset_path)
    print("Loaded {} songs.".format(len(songs)))

    for i, song in enumerate(songs):
        if not is_acceptable_song(song, ACCEPTABLE_DURATIONS):
            continue

        song = transpose(song)

        encoded_song = encode_song(song)
        save_path = os.path.join(SAVE_DIR, str(i))
        with open(save_path, "w") as fp:
            fp.write(encoded_song)


def load(file_path):
    with open(file_path, "r") as fp:
        song = fp.read()
        return song


def create_single_file_dataset(dataset_path, file_dataset_path, sequence_length):
    new_song_delimiter = "/ " * sequence_length
    songs = ""

    # Load encoded songs and add delimiters
    for path, _, files in os.walk(dataset_path):
        for file in files:
            file_path = os.path.join(path, file)
            song = load(file_path)
            songs += song + " " + new_song_delimiter

    songs = songs[:-1]

    # Save string that contains all dataset
    with open(file_dataset_path, "w") as fp:
        fp.write(songs)

    return songs


def create_mapping(songs, mapping_path):
    mappings = {}
    # Identify the vocabulary
    songs = songs.split()
    vocabulary = list(set(songs))

    # Create mappings
    for i, symbol in enumerate(vocabulary):
        mappings[symbol] = i

    with open(mapping_path, "w") as fp:
        json.dump(mappings, fp, indent=4)


def convert_songs_to_int(songs):
    int_songs = []
    # Load mappings
    with open(MAPPING_PATH, "r") as fp:
        mappings = json.load(fp)

    # Map songs to int
    songs = songs.split()
    for symbol in songs:
        int_songs.append(mappings[symbol])

    return int_songs


def generate_training_sequences(sequence_length):
    songs = load(SINGLE_FILE_DATASET)
    int_songs = convert_songs_to_int(songs)
    num_sequences = len(int_songs) - sequence_length

    inputs = []
    targets = []

    for i in range(num_sequences):
        inputs.append(int_songs[i : i + sequence_length])
        targets.append(int_songs[i + sequence_length])

    vocabulary_size = len(set(int_songs))
    inputs = keras.utils.to_categorical(inputs, num_classes=vocabulary_size)
    targets = np.array(targets)

    return inputs, targets


if __name__ == "__main__":
    preprocess(DATASET_PATH)
    songs = create_single_file_dataset(SAVE_DIR, SINGLE_FILE_DATASET, SEQUENCE_LENGTH)
    create_mapping(songs, MAPPING_PATH)
    inputs, targets = generate_training_sequences(SEQUENCE_LENGTH)
