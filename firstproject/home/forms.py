from django import forms
from home.models import Student

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=15)
    DOB = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

class StudentFormModel(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        # exclude = ['created_at', 'updated_at']
        # fields = ['name', 'age', 'email', 'mobile_number', 'DOB']