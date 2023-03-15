# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.

from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField
# fields that user can edit, create update
class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])
    age = IntegerField('Age')
    image = FileField("Image") 
    submit = SubmitField('Post')
    
class MarkasCompleteForm(FlaskForm):
    mark_completion = SubmitField('Mark as Complete')

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = TextAreaField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    tag2 = StringField('Tag2', validators=[DataRequired()])
    submit = SubmitField('Blog')

class ModulesForm(FlaskForm):
    # author = StringField()
    title =  StringField('Title Here', validators = [DataRequired()])
    intro = StringField('Introduction here (put some other content if no intro)',validators=[DataRequired()])
    content1 = StringField('Leave empty if you have styling preferences')
    image1 = FileField('optional image, no image will be shown if empty')
    content2 = StringField('for formatting')
    image2 = FileField('optional image')
    content3 = StringField('for formatting')
    image3 = FileField('optional image')
    content4 = StringField('for formatting')
    recap_info = StringField('Summary or Recap Here', validators=[DataRequired()])
    user_display = SelectField('Display Author', choices=[(),()], validators =[DataRequired()])
    

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

