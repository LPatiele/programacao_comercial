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
        # funcionario = forms.ModelChoiceField(RequerimentoLicenca.objects.filter(status = 'AV'), to_field_name="nome")
        labels = {
            'dataLicenca': _('Data Desejada'),
            'tipoLicenca': _('Licenca'),
            'status': _('Situacao')
        }

    def __init__( self, *args, **kwargs ):
        super( FormularioRequerimentoLicenca, self ).__init__( *args, **kwargs )
        print kwargs['initial']['user']
        self.fields['funcionario'].queryset= Funcionario.objects.filter(usuario__id=kwargs['initial']['user'])
        self.fields['status'].choices= [('AV', 'AVALIACAO')]
