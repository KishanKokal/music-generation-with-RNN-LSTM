from rest_framework.response import Response
from rest_framework.decorators import api_view
import uuid
from django.http import FileResponse
import os


def process_midi_file(file_path):
    try:
        file_name = file_path.split("/")[-1]
        # copy the file to the output folder
        with open(file_path, "rb") as f:
            with open(f"midi_files_output/{file_name}", "wb") as f2:
                f2.write(f.read())
        status = "success"
    except Exception as e:
        status = "error"
    return status


def delete_midi_files(file_name):
    try:
        os.remove(f"midi_files/{file_name}")
        os.remove(f"midi_files_output/{file_name}")
    except Exception as e:
        print(error)
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
