from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.forms.extras.widgets import SelectDateWidget
from .models import userDataBase

#this is for registration
class regForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)))
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30,render=False)))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render=False)))
    dob=forms.DateField(widget=SelectDateWidget())

    def clean_username(self):
        try:
            user=User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_('username already exist..'))


    def clean(self):
        try:
            if 'password'in self.cleaned_data and 'password2' in self.cleaned_data:
                if self.cleaned_data['password']!=self.cleaned_data['password2']:
                    raise forms.ValidationError(_("password dosen't match.."))
                return self.cleaned_data
        except:
            raise forms.ValidationError(_("some error occur"))

#this is for comic upload
class comicForm(forms.Form):
    author=forms.CharField(max_length=30)
    title=forms.CharField(max_length=50)
    fileup=forms.FileField()

    




