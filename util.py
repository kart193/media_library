import os
import logging

from werkzeug.utils import secure_filename

from database.session import session
from database.models import Medias

UPLOAD_FOLDER = "/opt/everyangle/my_app/media_files"
MUSIC_FORMATS = ["mp3", "wav", "aac"]
VIDEO_FORMATS = ["mp4", "mov"]
GAME_FORMATS = ["sav", "gam"]
AUDIO_STR = "Audio"
VIDEO_STR = "Video"
GAME_STR = "Game"
UNKNOWN_STR = "Unknown"


def get_media_files(file_type):
    """
    Return media files based on the file type provided in the corresponding API path parameter.
    :param file_type:
    :return: Media list
    """

    query = session.query(Medias)

    if file_type == "all":
        records = query.all()
    else:
        records = query.filter(Medias.type == file_type).all()

    # Loop and List Implementation
    medias_list = []
    for rec in records:
        medias_list.append({"title": rec.title, "id": rec.id,
                            "type": rec.type})
    return medias_list


def save_files(request):
    """
    This method is for two operations - one is to store single file or multiple files reference
    into database and second is to store the actual file into the directory defined.
    :param request: Media Files uploaded by user
    """
    file_names = []
    dir_list = os.listdir(UPLOAD_FOLDER)
    files = request.files.getlist('file')

    for file in files:
        name = file.filename
        if name in dir_list:
            logging.error("Name already existing")
            return
        if name == '':
            logging.error("No file selected to upload")
            return
        if get_file_type(name) is "Unknown":
            logging.error("File format not supported")
            return
        else:
            file_names = save_to_dir(file, file_names, name)

    if file_names:
        update_db(file_names)

    logging.info("Files saved successfully")
    return


def save_to_dir(file, file_names, name):
    file.save(os.path.join(UPLOAD_FOLDER, secure_filename(name)))
    file_names.append(name)
    return file_names


def update_db(filenames):
    for name in filenames:
        media = Medias(
            title=name,
            type=get_file_type(name),
        )
        session.add(media)
    session.commit()
    return


def get_file_type(filename):
    split_file_name = filename.split(".")
    file_extension = split_file_name[-1]
    if file_extension in MUSIC_FORMATS:
        return AUDIO_STR
    elif file_extension in VIDEO_FORMATS:
        return VIDEO_STR
    elif file_extension in GAME_FORMATS:
        return GAME_STR
    else:
        return UNKNOWN_STR


def delete_files(request):
    dir_list = os.listdir(UPLOAD_FOLDER)
    for getid in request.form.getlist('mycheckbox'):
        media = session.query(Medias).filter(Medias.id == getid).first()
        file = media.title
        delete_file_from_dir(dir_list, file)
        session.delete(media)
    session.commit()
    return


def delete_file_from_dir(dir_list, file):
    if file in dir_list:
        path = os.path.join(UPLOAD_FOLDER, file)
        os.remove(path)


def delete_row_files(val):
    dir_list = os.listdir(UPLOAD_FOLDER)
    delete_file_from_dir(dir_list, val)
    media = session.query(Medias).filter(Medias.title == val).first()
    session.delete(media)
    session.commit()
    return


def edit_title_in_db(row_id, val):
    media = session.query(Medias).filter(Medias.id == row_id).first()
    existing_title = media.title
    media.title = val
    session.add(media)
    session.commit()
    edit_in_dir(existing_title, val)
    return


def edit_in_dir(existing_title, val):
    os.rename(os.path.join(UPLOAD_FOLDER, existing_title), os.path.join(UPLOAD_FOLDER, val))
