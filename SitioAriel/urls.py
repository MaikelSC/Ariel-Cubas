from django.conf.urls import patterns, include, url

from django.contrib import admin

from Portal.views import home, mostrar_noticia, devolverArticulosBlog, mostrar_noticia_blog, articuloFijo, galerias, jobs, imagenes_galeria, contacto
from Portal.views import mostrar_ejemplo, devolverEjemplosTrabajos, devolverGaleriasTrabajo
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SitioAriel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^Home/$', home),
	url(r'^Home/(\d{1})$', home),
	url(r'^News/(\d{1})$', mostrar_noticia, kwargs={'name':'new'}),
	url(r'^Relevant/(\d{1})$', mostrar_noticia, kwargs={'name':'relevant'}),
	url(r'^Aboutme/$', articuloFijo,  kwargs={'name':'aboutme'}),
	url(r'^Blog/$', devolverArticulosBlog),
	url(r'^Examples/$', devolverEjemplosTrabajos),
	url(r'^Gallery/$', galerias),
	url(r'^Gallery/(\d{1})$', imagenes_galeria),
	url(r'^Gallery/Jobs/(\d{1})$', devolverGaleriasTrabajo),
	url(r'^Job/$', jobs),
	url(r'^Blogs/Art/(\d{1})$', mostrar_noticia_blog),
	url(r'^Blog/(\d{1})$', devolverArticulosBlog),
	url(r'^Example/(\d{1})$', mostrar_ejemplo),
	
	url(r'^Contact/$', contacto),
	
	
    url(r'^admin/', include(admin.site.urls)),
)
