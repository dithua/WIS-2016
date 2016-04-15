from django import forms


class CreateUserForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100, required=True)
    lastName = forms.CharField(label='Last Name', max_length=100, required=True)
