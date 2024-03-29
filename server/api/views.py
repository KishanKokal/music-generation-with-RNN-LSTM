from rest_framework.response import Response
from rest_framework.decorators import api_view
import uuid
from django.http import FileResponse
import os
import music21 as m21
from package.melodyGenerator import MelodyGenerator
from package.preprocess import (
    is_acceptable_song,
    transpose,
    encode_song,
    ACCEPTABLE_DURATIONS,
    SEQUENCE_LENGTH,
)


def load_song(file_path):
    song = m21.converter.parse(file_path)
    return song


def process_midi_file(file_path):
    try:
        print("Processing file: ", file_path)
        file_name = file_path.split("/")[-1]
        song = load_song(file_path)
        if is_acceptable_song(song, ACCEPTABLE_DURATIONS):
            song = transpose(song)
            encoded_song = encode_song(song)
            mg = MelodyGenerator()
            melody = mg.generate_melody(
                seed=encoded_song,
                num_steps=500,
                # max_sequence_length=SEQUENCE_LENGTH,
                max_sequence_length=256,
                temperature=0.5,
            )
            mg.save_melody(melody, filename="midi_files_output/" + file_name)
        status = "success"
    except Exception as e:
        print(e)
        status = "error"
    return status


def delete_midi_files(file_name):
    try:
        os.remove(f"midi_files/{file_name}")
        os.remove(f"midi_files_output/{file_name}")
    except Exception as e:
        print(e)
        pass


@api_view(["POST"])
def upload_file(request):
    file = request.FILES["file"]
    if not file.name.endswith(".mid"):
        return Response({"message": "Invalid file type"}, status=400)

    file.name = str(uuid.uuid4()) + ".mid"
    with open(f"midi_files/{file.name}", "wb") as f:
        f.write(file.read())

    status = process_midi_file(f"midi_files/{file.name}")
    
    if status == "error":
        delete_midi_files(file.name)
        return Response({"message": "An error occurred"}, status=500)
    else:
        response = FileResponse(
            open("midi_files_output/" + file.name, "rb"), content_type="audio/mid"
        )
        delete_midi_files(file.name)
        return response
