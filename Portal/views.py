from django.http import Http404
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.html import format_html
from django.utils.dateparse import parse_date
from django.shortcuts import render
from django.http import HttpResponseRedirect

import datetime

from Portal.models import Noticia, Comentario, ArticulosFijos, Comentario_articulosFijos, Categoria, ArticuloBlog, Comentario_articuloBlog, ArticulosFijos, Galeria, Imagen_galeria, Videos, Informacion_contacto, Trabajo
from Portal.models import Ejemplos_trabajos, Comentario_ejemplosTrabajos, Sitios


def home(request, noticiasIni = 1):
	
	noticiasIni = int(noticiasIni)
	noticiasXPag = 4
	
	noticias = Noticia.objects.filter(categoria = 2, publicado = True)[(noticiasIni-1)*noticiasXPag : (noticiasIni-1)*noticiasXPag + noticiasXPag]
	total = Noticia.objects.filter(categoria = 2, publicado = True).count()	
	noticiasCant =  total/noticiasXPag
	if total%noticiasXPag:
		noticiasCant += 1
	if noticiasCant != 1:	
		noticiasCant = range(1, noticiasCant+1)	
	for noticia in noticias:
		noticia.imagen =  noticia.imagen.url.split('/')[4]
		noticia.codigo = format_html(noticia.codigo[0:250])
		
	relevantes = Noticia.objects.filter(categoria = 1, publicado = True)
	for relevante in relevantes:
		relevante.imagen =  relevante.imagen.url.split('/')[4]	
	
	total = total%noticiasXPag
	
	ejemplos = Ejemplos_trabajos.objects.filter(publicado = True)[:5]
	for ejemplo in ejemplos:
			ejemplo.portada = Imagen_galeria.objects.filter(galeria_id = ejemplo.galeria_id, portada = True)[0]
			ejemplo.portada = ejemplo.portada.imagen.url.split('/')[4]
			ejemplo.titulo = ejemplo.trabajo.nombre+' to '+ejemplo.modelo
	
	return render_to_response("home.html", {'relevantes' : relevantes, 'noticias': noticias, 'noticiasCant': noticiasCant, 'ejemplos': ejemplos})


def mostrar_noticia(request, noticia_id, name):
	if request.method == 'POST':
		#if request.POST['enviar']:
			nombre_usuario = request.POST['nombre_usuario']
			email = request.POST['email']
			comentario = request.POST['comentario']
			fecha_publicacion  = datetime.datetime.now()
			noticia = Noticia.objects.get(id= noticia_id)
			comentario = Comentario(nombre_usuario = nombre_usuario, email = email, comentario = comentario, fecha_publicacion = fecha_publicacion, noticia = noticia)
			comentario.save()
			
				
	noticia = get_object_or_404(Noticia, pk=noticia_id)
	noticia.codigo = format_html(noticia.codigo)
	noticia.imagen =  noticia.imagen.url.split('/')[3]+'/'+noticia.imagen.url.split('/')[4]
	if noticia.comentarios:
		noticia.listComentarios = Comentario.objects.filter(noticia_id = noticia_id, publicado = True)
	
	sitios = Sitios.objects.filter(publicado = True)
	noticia.sitios = sitios
	if name == 'new':
		relevantes = Noticia.objects.filter(categoria = 1, publicado = True)[:4]
	else :
		relevantes = Noticia.objects.filter(categoria = 2, publicado = True)[:4]	
	for relevante in relevantes:
		relevante.imagen =  relevante.imagen.url.split('/')[4]	
	noticia.relevantes = relevantes
	
	ejemplos = Ejemplos_trabajos.objects.filter(publicado = True)[:5]
	for ejemplo in ejemplos:
		ejemplo.portada = Imagen_galeria.objects.filter(galeria_id = ejemplo.galeria_id, portada = True)[0]
		ejemplo.portada = ejemplo.portada.imagen.url.split('/')[4]
		ejemplo.titulo = ejemplo.trabajo.nombre+' to '+ejemplo.modelo
	noticia.ejemplos = ejemplos
	
	#elementos = elementos_comunes()
	
	return render(request, 'articulo.html', {'articulo': noticia})
	

	
		
	
def devolverArticulosBlog(request, articulosIni = 1):
	
	articulosIni = int(articulosIni)
	articulosXPag = 4	
	articulos = ArticuloBlog.objects.filter(publicado = True)[(articulosIni-1)*articulosXPag : (articulosIni-1)*articulosXPag + articulosXPag]
	total = ArticuloBlog.objects.filter(publicado = True).count()	
	articulosCant =  total/articulosXPag
	if total%articulosXPag:
		articulosCant += 1
	if articulosCant != 1:	
		articulosCant = range(1, articulosCant+1)	
	
	
	for articulo in articulos:
		articulo.imagen =  articulo.imagen.url.split('/')[4]
		articulo.codigo = format_html(articulo.codigo[0:320])
	
	return render(request, 'blog.html', { 'articulo_blog': articulos, 'artCant' : articulosCant , 'urlManual' : '/Blogs/Art', 'urlImagen': '/articulosBlog'})



def mostrar_noticia_blog(request, articuloblog_id):
	if request.method == 'POST':
		#if request.POST['enviar']:
			nombre_usuario = request.POST['nombre_usuario']
			email = request.POST['email']
			comentario = request.POST['comentario']
			fecha_publicacion  = datetime.datetime.now()
			articuloBlog = ArticuloBlog.objects.get(id= articuloblog_id)
			comentario = Comentario_articuloBlog(nombre_usuario = nombre_usuario, email = email, comentario = comentario, fecha_publicacion = fecha_publicacion, articuloBlog = articuloBlog)
			comentario.save()
			
				
	articuloBlog = get_object_or_404(ArticuloBlog, pk=articuloblog_id)
	articuloBlog.codigo = format_html(articuloBlog.codigo)
	articuloBlog.imagen =  articuloBlog.imagen.url.split('/')[3]+'/'+articuloBlog.imagen.url.split('/')[4]
	if articuloBlog.comentarios:
		articuloBlog.listComentarios = Comentario_articuloBlog.objects.filter(articuloBlog_id = articuloblog_id, publicado = True)
	
		
	
	sitios = Sitios.objects.filter(publicado = True)
	articuloBlog.sitios = sitios
	
	relevantes = Noticia.objects.filter(categoria = 1, publicado = True)[:4]	
	for relevante in relevantes:
		relevante.imagen =  relevante.imagen.url.split('/')[4]	
	articuloBlog.relevantes = relevantes
	
	ejemplos = Ejemplos_trabajos.objects.filter(publicado = True)[:5]
	for ejemplo in ejemplos:
		ejemplo.portada = Imagen_galeria.objects.filter(galeria_id = ejemplo.galeria_id, portada = True)[0]
		ejemplo.portada = ejemplo.portada.imagen.url.split('/')[4]
		ejemplo.titulo = ejemplo.trabajo.nombre+' to '+ejemplo.modelo
	articuloBlog.ejemplos = ejemplos
	
	return render(request, 'articulo.html', {'articulo': articuloBlog})


def galerias(request):
	galerias = Galeria.objects.all()
	videos = Videos.objects.all()
	for galeria in galerias:
		galeria.portada = Imagen_galeria.objects.filter(galeria_id = galeria.id, portada = True)
		if galeria.portada.count() > 0:
				galeria.portada = galeria.portada[0].imagen.url.split('/')[4]
	
	return render(request, 'gallery.html', {'galerias': galerias, 'videos':videos})


def imagenes_galeria(request, galeria_id):
	imagenes = Imagen_galeria.objects.filter(galeria_id = galeria_id)	
	for imagen in imagenes:
		imagen.imagen =  imagen.imagen.url.split('/')[3]+'/'+imagen.imagen.url.split('/')[4]
	galeria = Galeria.objects.get(id = galeria_id).nombre
	return render(request, 'images_gallery.html', {'imagenes': imagenes, 'galeria' : galeria})	
	

def devolverGaleriasTrabajo(request, trabajo_id):
	galerias = Galeria.objects.filter(id = trabajo_id)
	for galeria in galerias:
		galeria.portada = Imagen_galeria.objects.filter(galeria_id = galeria.id, portada = True)
		if galeria.portada.count() > 0:
				galeria.portada = galeria.portada[0].imagen.url.split('/')[4]
	
	return render(request, 'gallery.html', {'galerias': galerias})

	

def jobs(request):
	trabajos = Trabajo.objects.filter(publicado = True)
	
	for trabajo in trabajos:
		trabajo.portada = Imagen_galeria.objects.filter(galeria_id = trabajo.galeria_id, portada = True)[0]
		trabajo.portada = trabajo.portada.imagen.url.split('/')[4]
		trabajo.codigo = format_html(trabajo.codigo[0:320])
	
	return render(request, 'job.html', {'trabajos': trabajos})
	
def contacto(request):
	contacto = Informacion_contacto.objects.all()[0]
	contacto.imagen =  contacto.imagen.url.split('/')[4]
	
	
	ejemplos = Ejemplos_trabajos.objects.filter(publicado = True)
	for ejemplo in ejemplos:
			ejemplo.portada = Imagen_galeria.objects.filter(galeria_id = ejemplo.galeria_id, portada = True)[0]
			ejemplo.portada = ejemplo.portada.imagen.url.split('/')[4]
			ejemplo.titulo = ejemplo.trabajo.nombre+' to '+ejemplo.modelo
	contacto.ejemplos = ejemplos		
	
	sitios = Sitios.objects.filter(publicado = True)
	contacto.sitios = sitios
	
	return render(request, 'contacto.html', {'articulo': contacto})	

def articuloFijo(request, name):	
	if request.method == 'POST':
		#if request.POST['enviar']:
			nombre_usuario = request.POST['nombre_usuario']
			email = request.POST['email']
			comentario = request.POST['comentario']
			fecha_publicacion  = datetime.datetime.now()
			articuloFijo = ArticulosFijos.objects.get(nombre= name)
			comentario = Comentario_articulosFijos(nombre_usuario = nombre_usuario, email = email, comentario = comentario, fecha_publicacion = fecha_publicacion, articuloFijo = articuloFijo)
			comentario.save()
	
	articulo = ArticulosFijos.objects.get(nombre = name)
	articulo.codigo = format_html(articulo.codigo)
	articulo.imagen =  articulo.imagen.url.split('/')[3]+'/'+articulo.imagen.url.split('/')[4]
	if articulo.comentarios:
		articulo.listComentarios = Comentario_articulosFijos.objects.filter(articuloFijo_id = articulo.id, publicado = True)
		articulo.noAction = True
	
	if name == 'aboutme':
		sitios = Sitios.objects.filter(publicado = True)
		articulo.sitios = sitios
		relevantes = Noticia.objects.filter(categoria = 1, publicado = True)
		for relevante in relevantes:
			relevante.imagen =  relevante.imagen.url.split('/')[4]	
		articulo.relevantes = relevantes	
	
	return render(request, 'articulo.html', { 'articulo': articulo})



def devolverEjemplosTrabajos(request, articulosIni = 1):
	
	articulosIni = int(articulosIni)
	articulosXPag = 4	
	articulos = Ejemplos_trabajos.objects.filter(publicado = True)[(articulosIni-1)*articulosXPag : (articulosIni-1)*articulosXPag + articulosXPag]
	total = Ejemplos_trabajos.objects.filter(publicado = True).count()	
	articulosCant =  total/articulosXPag
	if total%articulosXPag:
		articulosCant += 1
	if articulosCant != 1:	
		articulosCant = range(1, articulosCant+1)	
	
	
	for articulo in articulos:
		articulo.imagen =  Imagen_galeria.objects.filter(galeria_id = articulo.galeria_id)[0]
		articulo.galeria = Galeria.objects.get(id = articulo.galeria_id)
		articulo.imagen = articulo.imagen.imagen.url.split('/')[4]
		articulo.codigo = format_html(articulo.codigo[0:320])
	
	return render(request, 'blog.html', { 'articulo_blog': articulos, 'artCant' : articulosCant , 'urlManual' : '/Example', 'urlImagen': '/galerias'})





def mostrar_ejemplo(request, ejemplo_id):
	if request.method == 'POST':
		#if request.POST['enviar']:
			nombre_usuario = request.POST['nombre_usuario']
			email = request.POST['email']
			comentario = request.POST['comentario']
			fecha_publicacion  = datetime.datetime.now()
			ejemplo_trabajo = Ejemplos_trabajos.objects.get(id= ejemplo_id)
			comentario = Comentario_ejemplosTrabajos(nombre_usuario = nombre_usuario, email = email, comentario = comentario, fecha_publicacion = fecha_publicacion, ejemplosTrabajos = ejemplo_trabajo)
			comentario.save()
			
				
	ejemplo = get_object_or_404(Ejemplos_trabajos, pk=ejemplo_id)
	ejemplo.codigo = format_html(ejemplo.codigo)
	ejemplo.opinion = format_html(ejemplo.opinion)
	ejemplo.galeria.imagenes = Imagen_galeria.objects.filter(galeria_id = ejemplo.galeria.id)
	for imagen in ejemplo.galeria.imagenes:
		imagen.imagen = imagen.imagen.url.split('/')[4]
	
	#ejemplo.imagen =  ejemplo.imagen.url.split('/')[3]+'/'+ejemplo.imagen.url.split('/')[4]
	if ejemplo.comentarios:
		ejemplo.listComentarios = Comentario_ejemplosTrabajos.objects.filter(ejemplosTrabajos_id = ejemplo_id, publicado = True)
	
	
	sitios = Sitios.objects.filter(publicado = True)
	ejemplo.sitios = sitios
	
	relevantes = Noticia.objects.filter(categoria = 1, publicado = True)[:4]	
	for relevante in relevantes:
		relevante.imagen =  relevante.imagen.url.split('/')[4]	
	ejemplo.relevantes = relevantes
	
	ejemplos1 = ArticuloBlog.objects.filter(publicado = True)[:5]
	for ejemplo1 in ejemplos1:
		ejemplo1.portada = ejemplo1.imagen.url.split('/')[4]
	ejemplo.ejemplos = ejemplos1
	
	#elementos = elementos_comunes()
	
	return render(request, 'articulo_galeria.html', {'articulo': ejemplo})
	
