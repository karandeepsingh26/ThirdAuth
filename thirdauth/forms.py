from django import forms
from .models import FbStatus
class StatusForm(forms.ModelForm):
	class Meta:
		model=FbStatus
		fields=['text']
def clean_text(self):
	text=self.cleaned_data.get('text')
	return text