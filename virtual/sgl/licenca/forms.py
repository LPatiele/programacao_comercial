# -*- coding: utf-8 -*-
from django import forms
from licenca.models import *
from django.utils.translation import ugettext_lazy as _

class FormularioTipoLicenca(forms.ModelForm):

    class Meta:
        model = TipoLicenca
        exclude = []


class FormularioLicenca(forms.ModelForm):

    class Meta:
        model = Licenca
        exclude = []

class FormularioRequerimentoLicenca(forms.ModelForm):

    class Meta:
        model = RequerimentoLicenca
        exclude = []
        labels = {
            'dataLicenca': _('Data Desejada'),
            'tipoLicenca': _('Licenca'),
            'status': _('Situacao')
        }
        # widgets = {
        #     'dataRequisicao': forms.SelectDateWidget(),
        #     'dataLicenca': forms.SelectDateWidget(),
        # }
