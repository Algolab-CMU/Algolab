from django import forms

# in the future maybe put this in a file called constants.py and import it here and in models.py
MAX_TITLE_LENGTH = 200
MAX_TEXT_LENGTH = 1000
MAX_CODE_LENGTH = 1000

class NewProblemForm(forms.Form):
  name = forms.CharField(label="Problem name", max_length=MAX_TITLE_LENGTH)
  description = forms.CharField(label="Description", max_length=MAX_TEXT_LENGTH)
