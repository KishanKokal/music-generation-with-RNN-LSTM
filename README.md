# music-generation-with-RNN-LSTM

## Basics of melody

![Squence and notes](./assets/fig-1.png) <br>
* A melody is a squence of notes and rests.
* On the y-axis you have the pitch (frequency), the higher it goes, the higher is the pitch. And, on the x-axis you have time.
* So, we are noting pitches of musical events in time.
* Because of that we can treat melody as a time series.
* Time series is a data structure where you have samples that are taken at equally spaced position in time.
* The whole melody generation now becomes a time-series prediction problem (Basically, we want to predict the next sample in a time series)
* First of all we will have to reduce all the notes to a given vocabulary of accepted musical events like pitches and rests which are moments of silence.

## The music generator (training)

For training our neural network what we do is basically we pass in chunks of music and then we ask the LSTM (Long Short-Term Memory) to predict the next notes in the music

## The music generator (inference)

* We start with a seed melody
* The model is going to give us a prediction. And, the prediction is going to be the next predicted notes in the music.
* We take that and append it to the initial seed and re-feed that again to the model and we expect yet another prediction from the model which is the next in the sequence.
* We continue with the third iteration we pass in the melody and now we get another prediction which is for the next note.
* So, we can basically a whole music starting from the seed just by going through each iteration.



## Tools and libraries
* [Keras/Tensorflow](https://keras.io/) (Deep Learning libraries)
* [Music21](https://web.mit.edu/music21/) (Python library for processing symbolic music data)
* [MuseScore](https://musescore.org/en) (For music notation)
