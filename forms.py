from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


# local order form
class LocalOrderForm(FlaskForm):
    date = StringField('Date (YYYY-MM-DD)', validators=[DataRequired()])
    amount = StringField('Order Cost USD', validators=[DataRequired()])
    markup = StringField('Mark Up', validators=[DataRequired()])
    my_rtgs_rate = StringField('Bus. Rate (RTGS)', validators=[DataRequired()])
    changer_rate = StringField('Changer Rate (RTGS)', validators=[DataRequired()])
    submit = SubmitField(label='Submit Order')
