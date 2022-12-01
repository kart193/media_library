import os

from database.models import Medias
from database.session import session
import pytest

from util import get_file_type, get_media_files, delete_file_from_dir, UPLOAD_FOLDER, delete_files, \
    edit_title_in_db, update_db, AUDIO_STR, GAME_STR, delete_row_files

MEDIA_LIST = [{"title": "sample.mov"}]


def setup():
    title = MEDIA_LIST[0]["title"]
    media = Medias(title=title, type=get_file_type(title),
                   )
    session.add(media)
    session.commit()


def teardown():
    session.query(Medias).delete()
    delete_file_from_dir(os.listdir(UPLOAD_FOLDER), MEDIA_LIST[0]["title"])
    session.commit()


@pytest.fixture(scope="function")
def run_around_tests():
    # Cleanup before test run
    teardown()
    # Add test data
    setup()
    yield
    teardown()


# Used function scope fixture in this test case
@pytest.mark.parametrize("file_type, count", [("all", 1), ("Video", 1), ("Audio", 0)])
def test_get_media_files(run_around_tests, file_type, count):
    media_list = get_media_files(file_type)
    assert len(media_list) == count


# User mocker patch in this test case
def test_edit_title_in_db(mocker):
    setup()
    medias = session.query(Medias).all()
    media_id = None
    existing_title = None
    for media in medias:
        existing_title = media.title
        media_id = media.id

    # Pre check database before name edit
    assert existing_title == "sample.mov"
    mocker.patch("util.edit_in_dir", return_value=None)

    edit_title_in_db(media_id, "new.mov")

    # Check database after name edit
    media = session.query(Medias).filter(Medias.id == media_id).first()
    editted_title = media.title
    assert editted_title != existing_title
    assert editted_title == "new.mov"


@pytest.mark.parametrize("new_file, file_type", [("new.mp3", AUDIO_STR), ("new.gam", GAME_STR)])
def test_update_db_with_type_check(run_around_tests, new_file, file_type):
    update_db([new_file])
    # Check if db is updated
    media = session.query(Medias).filter(Medias.title == new_file).first()
    assert media.title == new_file
    assert media.type == file_type


# Used count query in this test case
def test_delete_files(run_around_tests):
    count = session.query(Medias).count()
    assert count == 1
    delete_row_files("sample.mov")

    count = session.query(Medias).count()
    assert count == 0

