from django import forms
from .models import UserProfile

class UserForm(forms.ModelForm):
	class Meta:
		model=UserProfile
		fields='__all__'

	def clean_age(self):
		cd =self.cleaned_data
		age =cd.get('age' or None)
		if age is not None:
			if int(age) >120:
				raise forms.ValidationErro("The age your entered is beyond limit")
			return age