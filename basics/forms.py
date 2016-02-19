from django import forms

# in the future maybe put this in a file called constants.py and import it here and in models.py
MAX_TITLE_LENGTH = 200
MAX_TEXT_LENGTH = 1000
MAX_CODE_LENGTH = 1000

class ProblemForm(forms.Form):
  title = forms.CharField(label="Problem title", max_length=MAX_TITLE_LENGTH)
  description = forms.CharField(label="Description", max_length=MAX_TEXT_LENGTH)