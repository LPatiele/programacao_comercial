from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView, View
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from licenca.models import *
from licenca.forms import *


class RequerimentoLicencaNew(LoginRequiredMixin, CreateView):
    model = RequerimentoLicenca
    form_class = FormularioRequerimentoLicenca
    template_name = 'licenca/novo.html'
    success_url = reverse_lazy('listar-licenca')
    exclude=['funcionario']

    def get_initial(self):
        self.initial.update({'user': self.request.user.id})
        return self.initial


class RequerimentoLicencaList(LoginRequiredMixin, ListView):
    model = RequerimentoLicenca
    template_name = 'licenca/listar.html'

class RequerimentoLicencaDetail(LoginRequiredMixin, DetailView):
    model = RequerimentoLicenca
    template_name = 'licenca/detalhar.html'


class RequerimentoLicencaEdit(PermissionRequiredMixin, UpdateView):
    permission_required = 'licenca.change_requerimentolicenca'
    model = RequerimentoLicenca
    form_class = FormularioRequerimentoLicenca
    template_name = 'licenca/editar.html'
    success_url = reverse_lazy('listar-licenca')


class RequerimentoLicencaDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'licenca.change_requerimentolicenca'
    model = RequerimentoLicenca
    template_name = 'licenca/deletar.html'
    success_url = reverse_lazy('listar-licenca')
