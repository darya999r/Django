from django import forms


class UserForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone = forms.CharField(max_length=10)
    address = forms.CharField(max_length=200)
