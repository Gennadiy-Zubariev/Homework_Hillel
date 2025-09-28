from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, Optional

class MediaForm(FlaskForm):
    title = StringField('Назва', validators=[DataRequired()])
    type = HiddenField('Тип')
    submit = SubmitField('Додати')


class ReviewForm(FlaskForm):
    impressions = TextAreaField('Враження', validators=[Optional()])
    submit = SubmitField('Зберегти')