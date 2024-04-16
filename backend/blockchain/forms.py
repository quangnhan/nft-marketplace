# In forms.py within your Django app

from django import forms

class SmartContractDownloadForm(forms.Form):
    from_token_id = forms.IntegerField()
    to_token_id = forms.IntegerField()

    def clean(self):
        cleaned_data = super().clean()
        from_token_id = cleaned_data.get("from_token_id")
        to_token_id = cleaned_data.get("to_token_id")

        if from_token_id is not None and to_token_id is not None:
            if from_token_id > to_token_id:
                raise forms.ValidationError("From token ID must be greater than or equal to to token ID.")

        return cleaned_data
