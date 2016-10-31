from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from licenca.models import *
from licenca.forms import *


class LicencaList(ListView):
    model = Licenca
    template_name = 'licenca/listar.html'

class LicencaNew(CreateView):
    model = Licenca
    form_class = FormularioLicenca
    template_name = 'licenca/novo.html'
    success_url = reverse_lazy('listar-licenca')

class TipoLicencaList(ListView):
    model = TipoLicenca
    template_name = 'licenca/listar.html'

class TipoLicencaNew(CreateView):
    model = TipoLicenca
    form_class = FormularioTipoLicenca
    template_name = 'licenca/novo.html'
    success_url = reverse_lazy('listar-licenca')

class TipoLicencaEdit(UpdateView):
    model = TipoLicenca
    form_class = FormularioTipoLicenca
    template_name = 'licenca/editar.html'
    success_url = reverse_lazy('listar-licenca')

class TipoLicencaDelete(DeleteView):
    model = TipoLicenca
    template_name = 'licenca/deletar.html'
    success_url = reverse_lazy('listar-licenca')

class RequerimentoLicencaNew(CreateView):
    model = RequerimentoLicenca
    form_class = FormularioRequerimentoLicenca
    template_name = 'licenca/novo.html'
    success_url = reverse_lazy('listar-licenca')

class RequerimentoLicencaList(ListView):
    model = RequerimentoLicenca
    template_name = 'licenca/listar.html'

class RequerimentoLicencaEdit(UpdateView):
    model = RequerimentoLicenca
    form_class = FormularioRequerimentoLicenca
    template_name = 'licenca/editar.html'
    success_url = reverse_lazy('listar-licenca')


class RequerimentoLicencaDelete(DeleteView):
    model = RequerimentoLicenca
    template_name = 'licenca/deletar.html'
    success_url = reverse_lazy('listar-licenca')
