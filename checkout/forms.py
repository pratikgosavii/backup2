from django import forms
from .models import *


class user_address_detail_form(forms.ModelForm):
    
    name =                  forms.CharField(widget=forms.TextInput())
    mobilenumber =          forms.IntegerField() 
    pincode =               forms.IntegerField() 
    address_full =          forms.CharField(widget=forms.TextInput())
    landmark =              forms.CharField(widget=forms.TextInput())
    addresstype =           forms.CharField(widget=forms.TextInput())
   
    
    class Meta():
        model = user_address_detail
        fields = ['name', 'mobilenumber', 'pincode', 'address_full', 'landmark', 'addresstype']


class CouponApplyForm(forms.Form):

    code = forms.CharField()

    
    


