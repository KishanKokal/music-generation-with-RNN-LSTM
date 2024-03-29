import tensorflow.keras as keras
import json
import numpy as np
from .preprocess import SEQUENCE_LENGTH, MAPPING_PATH
import music21 as m21


class MelodyGenerator:
    def __init__(self, model_path="models/model.h5"):

        self.model_path = model_path
        self.model = keras.models.load_model(model_path)

        with open(MAPPING_PATH, "r") as fp:
            self._mappings = json.load(fp)

        self._start_symbols = ["/"] * SEQUENCE_LENGTH

    def _sample_with_temperature(self, probabilities, temperature):
        predictions = np.log(probabilities) / temperature
        probabilities = np.exp(predictions) / np.sum(np.exp(predictions))

        choices = range(len(probabilities))
        index = np.random.choice(choices, p=probabilities)

        return index

    def generate_melody(self, seed, num_steps, max_sequence_length, temperature):
        # create seed with start symbols
        seed = seed.split()
        melody = seed
        seed = self._start_symbols + seed

        # map seed to int
        seed = [self._mappings[symbol] for symbol in seed]

        for _ in range(num_steps):
            # limit the seed to max_sequence_length
            seed = seed[-max_sequence_length:]

            # one-hot encode the seed
            onehot_seed = keras.utils.to_categorical(
                seed, num_classes=len(self._mappings)
            )
            # (1, max_sequence_length, num of symbols in the mapping)
            onehot_seed = onehot_seed[np.newaxis, ...]

            # make a prediction
            probabilities = self.model.predict(onehot_seed)[0]
            # use a multinomial distribution to sample
            output_int = self._sample_with_temperature(probabilities, temperature)
            # update the seed
            seed.append(output_int)
            # map int to our encoding
            output_symbol = [
                key for key, value in self._mappings.items() if value == output_int
            ][0]
            # check whether at the end of the melody
            if output_symbol == "/":
                break
            # update the melody
            melody.append(output_symbol)

        return melody

    def save_melody(
        self, melody, step_duration=0.25, format="midi", filename="mel.mid"
    ):
        # create a music21 stream
        stream = m21.stream.Stream()

        start_symbol = None
        step_counter = 1

        # parse all the symbols in the melody and create note/rest objects
        for i, symbol in enumerate(melody):
            # handle case in which we have a note/rest
            if symbol != "_" or i + 1 == len(melody):
                # ensure we're dealing with note/rest beyond the first one
                if start_symbol is not None:
                    quarter_length_duration = step_duration * step_counter
                    # handle rest
                    if start_symbol == "r":
                        m21_event = m21.note.Rest(quarterLength=quarter_length_duration)
                    # handle note
                    else:
                        m21_event = m21.note.Note(
                            int(start_symbol), quarterLength=quarter_length_duration
                        )
                    stream.append(m21_event)
                    # reset the step counter
                    step_counter = 1
                start_symbol = symbol
            # handle case in which we have a prolongation sign
            else:
                step_counter += 1

        # write the m21 stream to a file
        stream.write("midi", fp=filename)


if __name__ == "__main__":
    mg = MelodyGenerator()
    melody = mg.generate_melody(
        seed="55 _ _ _ 60 _ _ _ 60 _ 62 _ 60 _ 59 _ 57 _ 55 _ 60 _ _ _ 60 _ 64 _ 62 _ _ _ _ _ _ _ 60 _ _ _ _ _ 59 _ 57 _ _ _ 62 _ _ _ 60",
        num_steps=5000,
        # max_sequence_length=SEQUENCE_LENGTH,
        max_sequence_length=1024,
        temperature=0.7,
    )
    print(melody)
    mg.save_melody(melody)
