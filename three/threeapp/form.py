from django import forms
from threeapp.models import Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class EmpRegister(forms.Form):

    name=forms.CharField()
    email=forms.EmailField()
    mobile=forms.CharField()
    address=forms.CharField()

class Emp(forms.Form):

    empname=forms.CharField()
    empmobile=forms.CharField()
    empaddress=forms.CharField()

class stud(forms.Form):

    name=forms.CharField()
    stu_class=forms.CharField()
    stu_address=forms.CharField()
    stu_marks=forms.CharField()


class CourseForm(forms.ModelForm):
    Course_name=forms.CharField()
    Course_duration=forms.IntegerField()
    Course_category=forms.CharField()
    Course_fees=forms.FloatField()

    class Meta:
        model=Course
        #fields="__all__"
        #fields=['Course_name']
        fields=["Course_name",'Course_duration','Course_category']


class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']