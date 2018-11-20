from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    post = StringField('Your name',validators=[Required()])
    body = TextAreaField('Pitch')
    category_id = SelectField('Pick Category',choices=[('PRODUCT', 'PRODUCT'),('INTERVIEW', 'INTERVIEW'),('PICK-UP', 'PICK-UP'),
                                   ('PROMOTION', 'PROMOTION')],
                          validators=[Required()])
    content = StringField('content', validators=[Required()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):

    poster = StringField('Your name',validators=[Required()])

    comment = TextAreaField('Your comment',validators=[Required()])
    
    submit = SubmitField('Comment')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [Required()])
    submit = SubmitField('Submit')
