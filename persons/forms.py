from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your Name', max_length=100)

class ContactForm(forms.Form):
    subject = forms.CharField(max_length = 100, initial ='initial text')#http://stackoverflow.com/questions/604266/django-set-default-form-values
    message = forms.CharField(widget = forms.Textarea)
    sender = forms.EmailField(help_text='A valid email address, please.')
    cc_myself = forms.BooleanField(required=False)
