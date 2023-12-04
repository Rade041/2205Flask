from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField,PasswordField, BooleanField, SubmitField, HiddenField, DateTimeField
from wtforms import TextAreaField, FileField, DecimalField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange
from app.models import User, Articles, Jobs, Courses 

class JobForm(FlaskForm) :
    job_title = StringField('Job Title', validators=[DataRequired()])
    salary = IntegerField('Salary', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    industry = StringField('Industry', validators=[DataRequired()])
    sector = StringField('Sector', validators=[DataRequired()])
    submit = SubmitField('Save')

class ArticlesForm(FlaskForm) :
    title = StringField('Title', validators=[DataRequired()])
    author_name = StringField('Author Name', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    submit = SubmitField('Save')

class CoursesForm(FlaskForm) :
    course_title = StringField('Title', validators=[DataRequired()])
    course_leader = StringField('Course Leader', validators=[DataRequired()])
    start_date = IntegerField('Start Date',validators=[DataRequired()])
    end_date = IntegerField('End Date', validators=[DataRequired()] )
    venue_name_address = StringField('Venue & Address', validators=[DataRequired()])
    contact_phone = StringField('Contact Phone', validators=[DataRequired()])
    contact_email = StringField('Contact Email', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()] )
    submit = SubmitField('Save')
