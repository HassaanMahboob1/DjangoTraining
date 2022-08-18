from django import forms
from .models import Betting


# creating a form
class BettingForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Betting

		# specify fields to be used
		fields = [
			"Betting_id",
			"Betting_amount"
           
		]
