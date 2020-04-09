from django import forms
from models import Market



class consult(forms.ModelForm):
    ''' colects the infos for consulting the database'''
    date = forms.DateField(
        verbose_name='Data da consulta'
        )

    market = forms.MultipleChoiceField(
        queryset = Market.objects.all()
        )
    username = forms.CharField(
        verbose_name='Super Admin Username',
        max_length = 100
        )
    password = forms.CharField( 
        widget=forms.PasswordInput
        )

    class Meta:
        model = Market
        fields = ["date", "created_at", "market", "username", "password"]
