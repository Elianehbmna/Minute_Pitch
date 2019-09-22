from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField, TextAreaField,ValidationError,RadioField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description = TextAreaField("What would you like to pitch ?",validators=[Required()])
    category = RadioField('Label', choices=[ ('Educational','Educational'), ('Musical','Musical'),('Religion','Religion'),('Comedy','Comedy')],validators=[Required()])
    submit = SubmitField('Submit')
class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
class CommentForm(FlaskForm):
	description = TextAreaField('Add comment',validators=[Required()])
	submit = SubmitField()
class UpvoteForm(FlaskForm):
	submit = SubmitField()

class DownvoteForm(FlaskForm):
	submit = SubmitField()


