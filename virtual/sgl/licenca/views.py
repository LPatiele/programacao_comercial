from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from licenca.models import *
from licenca.forms import *



class LicencaList(LoginRequiredMixin, ListView):
    model = Licenca
    template_name = 'licenca/listar.html'

class LicencaNew(LoginRequiredMixin, CreateView):
    model = Licenca
    form_class = FormularioLicenca
    template_name = 'licenca/novo.html'
    success_url = reverse_lazy('listar-licenca')

class TipoLicencaList(LoginRequiredMixin, ListView):
    model = TipoLicenca
    template_name = 'licenca/listar.html'

class TipoLicencaNew(LoginRequiredMixin, CreateView):
    model = TipoLicenca
    form_class = FormularioTipoLicenca
    template_name = 'licenca/novo.html'
    success_url = reverse_lazy('listar-licenca')

class TipoLicencaEdit(LoginRequiredMixin, UpdateView):
    model = TipoLicenca
    form_class = FormularioTipoLicenca
    template_name = 'licenca/editar.html'
    success_url = reverse_lazy('listar-licenca')

class TipoLicencaDelete(LoginRequiredMixin, DeleteView):
    model = TipoLicenca
    template_name = 'licenca/deletar.html'
    success_url = reverse_lazy('listar-licenca')

class RequerimentoLicencaNew(LoginRequiredMixin, CreateView):
    model = RequerimentoLicenca
    form_class = FormularioRequerimentoLicenca
    template_name = 'licenca/novo.html'
    success_url = reverse_lazy('listar-licenca')

class RequerimentoLicencaList(LoginRequiredMixin, ListView):
    model = RequerimentoLicenca
    template_name = 'licenca/listar.html'


class RequerimentoLicencaEdit(LoginRequiredMixin, UpdateView):
    model = RequerimentoLicenca
    form_class = FormularioRequerimentoLicenca
    template_name = 'licenca/editar.html'
    success_url = reverse_lazy('listar-licenca')


class RequerimentoLicencaDelete(LoginRequiredMixin, DeleteView):
    model = RequerimentoLicenca
    template_name = 'licenca/deletar.html'
    success_url = reverse_lazy('listar-licenca')
