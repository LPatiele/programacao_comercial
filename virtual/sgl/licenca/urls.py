from django.conf.urls import url
from licenca import views

urlpatterns = [
    url(r'^novo/$', views.RequerimentoLicencaNew.as_view(), name='novo-licenca'),
    url(r'^$', views.RequerimentoLicencaList.as_view(), name='listar-licenca'),
    url(r'^(?P<pk>[0-9]+)/$', views.RequerimentoLicencaEdit.as_view(), name='editar-licenca'),
    url(r'^detalhar/(?P<pk>[0-9]+)/$', views.RequerimentoLicencaDetail.as_view(), name='detalhar-licenca'),
    url(r'^excluir/(?P<pk>[0-9]+)/$', views.RequerimentoLicencaDelete.as_view(), name='deletar-licenca'),
]
