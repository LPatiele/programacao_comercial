# from django.shortcuts import render
# from django.http import HttpResponse
#
#
# def index(request):
#     context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
#     return render(request, 'licenca/index.html', context=context_dict)
#
# def about(request):
#     return HttpResponse("ABOUT PAGE.")

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from licenca.models import *
from licenca.forms import *

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
