from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from app.models import User
from flask_babel import _, lazy_gettext as _l
from flask import request


class SearchForm(FlaskForm):
    q = StringField(_l('Search'), validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)


class EditProfileForm(FlaskForm):
    username = StringField(_('Username'), validators=[DataRequired()])
    about_me = TextAreaField(_('About me'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_('Submit'))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
    
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError(_('Please use another username!'))


class PostForm(FlaskForm):
    post = TextAreaField(_('Say something'), validators=[
        DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_('Submit'))