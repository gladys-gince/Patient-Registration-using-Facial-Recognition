from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'date': DateInput(),
            'shift':TimeInput()
        }
        exclude = ['present','updated']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['ranking'].widget.attrs['class'] = 'form-control'
        self.fields['profession'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        #self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['shift'].widget.attrs['class'] = 'form-control'

        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['bg'].widget.attrs['class'] = 'form-control'
        self.fields['ephone'].widget.attrs['class'] = 'form-control'
        self.fields['address'].widget.attrs['class'] = 'form-control'
        self.fields['aadhar'].widget.attrs['class'] = 'form-control'

        self.fields['languages'].widget.attrs['class'] = 'form-control'
        self.fields['physician'].widget.attrs['class'] = 'form-control'
        self.fields['allergies'].widget.attrs['class'] = 'form-control'
        self.fields['height'].widget.attrs['class'] = 'form-control'
        
        self.fields['weight'].widget.attrs['class'] = 'form-control'
        self.fields['condition'].widget.attrs['class'] = 'form-control'
        self.fields['drugs'].widget.attrs['class'] = 'form-control'




