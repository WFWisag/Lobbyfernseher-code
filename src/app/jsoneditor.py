import json


def load_json_file(file_path):
    with open(file_path, "r") as f:
        return json.load(f)


""" 
Pattern:
{
  "duration": 5000,
  "media": [
    {
      "type": "image",
      "filename": "image1.jpg"
    },
    {
      "type": "video",
      "filename": "video1.mp4"
    },
    {
      "type": "image",
      "filename": "image2.jpg"
    }
  ]
}


"""


def change_duration(file_path, new_duration):
    data = load_json_file(file_path)
    data["duration"] = new_duration
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def add_media(file_path, media_type, filename):
    data = load_json_file(file_path)
    data["media"].append({"type": media_type, "filename": filename})
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def remove_media(file_path, filename):
    data = load_json_file(file_path)
    data["media"] = [media for media in data["media"] if media["filename"] != filename]
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
