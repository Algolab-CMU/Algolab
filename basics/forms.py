from django import forms

# in the future maybe put this in a file called constants.py and import it here and in models.py
MAX_TITLE_LENGTH = 200
MAX_TEXT_LENGTH = 1000
MAX_CODE_LENGTH = 1000

MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
FREE_RESPONSE = "FREE_RESPONSE"

typeChoices = [(FREE_RESPONSE,"Free response"),(MULTIPLE_CHOICE,"Multiple choice")]

class ProblemForm(forms.Form):
  title = forms.CharField(label="Problem title", max_length=MAX_TITLE_LENGTH)
  description = forms.CharField(label="Description", max_length=MAX_TEXT_LENGTH)
  problemType = forms.ChoiceField(label="Type", choices=typeChoices)


class ClassForm(forms.Form):
  classNumber = forms.CharField(label="Class number")
  classTitle = forms.CharField(label="Class title")
  classDescription = forms.CharField(label="Class description")