from django.conf.urls import url
from licenca import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
    #url(r'^novo/$', views.LicencaNew.as_view(), name='novo-licenca'),
    url(r'^novo/$', views.RequerimentoLicencaNew.as_view(), name='novo-licenca'),
    #url(r'^$', views.TipoLicencaList.as_view(), name='listar-licenca'),
    url(r'^$', views.RequerimentoLicencaList.as_view(), name='listar-licenca'),
    #url(r'^novo/$', views.TipoLicencaNew.as_view(), name='novo-licenca'),
    url(r'^(?P<pk>[0-9]+)/$', views.RequerimentoLicencaEdit.as_view(), name='editar-licenca'),
    url(r'^excluir/(?P<pk>[0-9]+)/$', views.RequerimentoLicencaDelete.as_view(), name='deletar-licenca'),
]
