from flask_wtf import FlaskForm
from wtforms import StringField, FileField


class ImageUploadForm(FlaskForm):
    picture = FileField("Upload picture")
