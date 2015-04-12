from django.contrib import admin

from Portal.models import Noticia, Comentario, ArticulosFijos, Comentario_articulosFijos, Categoria, ArticuloBlog
from Portal.models import Comentario_articuloBlog, Galeria, Videos, Imagen_galeria, Informacion_contacto, Trabajo, Ejemplos_trabajos, Comentario_ejemplosTrabajos
from Portal.models import Sitios

admin.site.register(Noticia)
admin.site.register(Comentario)


class ArticulosFijosAdmin(admin.ModelAdmin):	 
	
	 class Media:
		 js = ['pluggins/tinymce/jquery-1.7.2.js',
			'pluggins/tinymce/tinymce.min.js',
            'pluggins/tinymce/basic_config.js',] 

admin.site.register(ArticulosFijos, ArticulosFijosAdmin)

admin.site.register(Comentario_articulosFijos)
admin.site.register(Categoria)
admin.site.register(ArticuloBlog)
admin.site.register(Comentario_articuloBlog)

class Imagen_galeriaInline(admin.TabularInline):
    model = Imagen_galeria
    extra = 0
	#formfield_overrides = { models.ImageField: {'widget': YourPreviewWidget}}
	
class GaleriaAdmin(admin.ModelAdmin):    
    inlines = [Imagen_galeriaInline]

admin.site.register(Galeria, GaleriaAdmin)

from django.utils.html import format_html



#from django import forms
#from django.db import models

#class MiImageField(forms.Textarea):  
    #def __init__(self, *args, **kwargs):  
		#attrs = kwargs.setdefault('attrs', {})
		#attrs.setdefault('cols', 80)  
		#attrs.setdefault('rows', 1) 
		
		#super(MiImageField, self).__init__(*args, **kwargs) 
	#def render(self, name, value, attrs=None):
        #substitutions = {
            #initial_text': self.initial_text,
            #'input_text': self.input_text,
            #'clear_template': '',
            #'clear_checkbox_label': self.clear_checkbox_label,
        #}	

def imagenPrevia(obj):
		  #return obj.src
		  #return obj.src.file
	return format_html('<img class="imagen_listado" src="/static/images/galerias/'+obj.imagen.url.split('/')[4]+'"/>')


from django.db import models

class Imagen_galeriaAdmin(admin.ModelAdmin):
	#fields = ('galeria', 'formatoImg')
	list_display = ('galeria', 'fotografo', imagenPrevia)
	#formfield_overrides = {
        #models.ImageField: {'widget': imagenPrevia},
    #} 
	 
	#def formatoImg(obj):
		  #return obj.src
		  #return obj.src.file
		#return format_html('<img class="imagen_listado" src="/static/images/galerias/'+obj.imagen.url.split('/')[4]+'"/>') 
	 #formfield_overrides = { models.ImageField: {'widget': MiImageField}, }
	 
	 #def image_img(self, obj):
		#if self.imagen:
		#return u'<img src="%s" />' % obj.imagen.url 
        ##else:
            #return '(No image found)'
    #image_img.short_description = 'Thumb'
    #image_img.allow_tags = True
	

#admin.site.register(Imagen_galeria, Imagen_galeriaAdmin)
admin.site.register(Informacion_contacto)
admin.site.register(Trabajo)
admin.site.register(Videos)
admin.site.register(Ejemplos_trabajos)
admin.site.register(Comentario_ejemplosTrabajos)
admin.site.register(Sitios)



