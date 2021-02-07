from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class HelloForm(FlaskForm):
    msg_name = StringField(label='Name',
                           validators=[DataRequired(), Length(1, 32)])
    body = TextAreaField(label='Message',
                         validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()
