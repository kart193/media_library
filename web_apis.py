from flask import Blueprint, render_template, request, redirect
from util import *
app = Blueprint('media_library', __name__)


@app.route("/dashboard/<file_type>")
def render_dashboard(file_type):
    """
    This method is called from UI to render media library dashboard. It takes file_type as path
    param. Accepted vales: Video, Audio, Game, all.
    :param file_type:
    :return: render media library dashboard with media files from database
    """
    files = get_media_files(file_type)
    return render_template('basic.html', files=files)


@app.route("/upload", methods=['POST'])
def upload():
    """ This is to upload files into the database """
    if request.method == "POST":
        save_files(request)
        return redirect("/dashboard/all")


@app.route("/delete", methods=['POST'])
def delete():
    """ Delete single or multiple table entries """
    if request.method == "POST":
        delete_files(request)
        return redirect("/dashboard/all")


@app.route("/delete_row/<val>", methods=['POST', 'GET'])
def delete_row(val):
    """ To delete single row entry """
    delete_row_files(val)
    return redirect("/dashboard/all")


@app.route("/update_row/<row_id>/<val>")
def edit_name(row_id, val):
    """ To edit file name in the database """
    edit_title_in_db(row_id, val)
    return redirect("/dashboard/all")

