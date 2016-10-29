from django.conf.urls import url
from licenca import views

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    # url(r'^about/$', views.about, name='about'),
    url(r'^$', views.TipoLicencaList.as_view(), name='listar-licenca'),
    url(r'^novo/$', views.TipoLicencaNew.as_view(), name='novo-licenca'),
    url(r'^(?P<pk>[0-9]+)/$', views.TipoLicencaEdit.as_view(), name='editar-licenca'),
    url(r'^excluir/(?P<pk>[0-9]+)/$', views.TipoLicencaDelete.as_view(), name='deletar-licenca'),
]
