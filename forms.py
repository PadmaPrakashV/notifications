from wtforms import Form
from wtforms import SelectField,TextField, SubmitField
from wtforms.validators import DataRequired

class FindStatusForm(Form):
    category = SelectField('Category',choices=[(0,'Team 1'),(1,'Team 2'),(2,'Team 3'),(3,'Team 4')],validators=[DataRequired()])
    notification = TextField('Notification',validators=[DataRequired()])
    search = SubmitField('Search Notification Status')