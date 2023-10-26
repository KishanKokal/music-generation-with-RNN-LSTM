import os
import music21 as m21

DATASET_PATH = "deutschl/test"
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


def preprocess(dataset_path):
    print("Loading songs...")
    songs = load_songs(dataset_path)
    print("Loaded {} songs.".format(len(songs)))

    for song in songs:
        if not is_acceptable_song(song, ACCEPTABLE_DURATIONS):
            continue

        song = transpose(song)


if __name__ == "__main__":
    songs = load_songs(DATASET_PATH)
    print("Loaded {} songs.".format(len(songs)))
    song = songs[2]
    transposed_song = transpose(song)
    # song.show()
    transposed_song.show()
