# -*- coding: utf-8 -*-
from django import forms
from licenca.models import *
class FormularioTipoLicenca(forms.ModelForm):

    class Meta:
        model = TipoLicenca
        exclude = []
