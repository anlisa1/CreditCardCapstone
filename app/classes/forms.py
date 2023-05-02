# This file is where data entry forms are created. Forms are placed on templates 
# and users fill them out.  Each form is an instance of a class. Forms are managed by the 
# Flask-WTForms library.



from flask_wtf import FlaskForm
import mongoengine.errors
from wtforms.validators import URL, Email, DataRequired, NumberRange
from wtforms.fields.html5 import URLField
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField, FileField, BooleanField, RadioField
# fields that user can edit, create update
from flask_ckeditor import CKEditorField

class ProfileForm(FlaskForm):
    fname = StringField('First Name', validators=[DataRequired()])
    lname = StringField('Last Name', validators=[DataRequired()]) 
    role = SelectField('Role',choices=[("Teacher","Teacher"),("Student","Student")])
    age = IntegerField('Age')
    image = FileField("Image") 
    submit = SubmitField('Post')

class PersonalityQuizForm(FlaskForm):
    # RadioField('Label', choices=[('value','description'),('value_two','whatever')])
    creditcard = RadioField('Have you ever had a credit card?', choices=[('Yes','Yes'),('No','No')])
    student = RadioField('Are you a student?', choices=[('Yes','Yes'),('No','No')])
    business = RadioField('Do you have a business?', choices=[('Yes','Yes'),('No','No')])
    travel = RadioField('Do you frequently travel overseas?', choices=[('Yes','Yes'),('Sometimes','Sometimes'),('No','No')])
    dine = RadioField('Do you dine out often?', choices=[('Yes','Yes'),('Sometimes','Sometimes'),('No','No')])
    cashback = RadioField('Is getting a high cashback reward important to you?', choices=[('Yes','Yes'),('Sometimes','Sometimes'),('No','No')])
    submit = SubmitField('Answer')
    
# class MarkasCompleteForm(FlaskForm):
#     mark_completion = SubmitField('Mark as Complete')

# class verifyCourseForm(FlaskForm):
#     verify_course = SubmitField('Validate Course')

class BlogForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired()])
    content = CKEditorField('Blog', validators=[DataRequired()])
    tag = StringField('Tag', validators=[DataRequired()])
    tag2 = StringField('Tag2', validators=[DataRequired()])
    submit = SubmitField('Blog')

class ModulesForm(FlaskForm):
    title =  StringField('Title Here', validators = [DataRequired()])
    cover_image = FileField('Cover image here, will not be in the module but rather will appear in the modules page')
    content1 = CKEditorField('Leave empty if you have styling preferences')
    image1 = FileField('optional image, no image will be shown if empty')
    image1size=IntegerField('Number between 20 and 100 for the image sizes, put random number if none for the above image', validators=[NumberRange(min=20, max=100)], )
    video1 = StringField('please input link to youtube video here, leave empty if none')
    content2 = CKEditorField('for formatting')
    image2 = FileField('optional image')
    video2 = StringField('please input link to youtube video here, leave empty if none')
    content3 = CKEditorField('for formatting')
    image3 = FileField('optional image')
    content4 = CKEditorField('for formatting')
    video3 = StringField('please input link to youtube video here, leave empty if none')
    submit = SubmitField('Make Module')
    # user_display = SelectField('Display Author', choices=[(),()], validators =[DataRequired()])
    

class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    submit = SubmitField('Comment')

